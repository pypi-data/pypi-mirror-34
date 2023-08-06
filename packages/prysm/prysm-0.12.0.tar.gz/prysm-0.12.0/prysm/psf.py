"""A base point spread function interface."""
from scipy import interpolate

from mpl_toolkits.axes_grid1.axes_rgb import make_rgb_axes
from matplotlib import colors, patches

from .coordinates import cart_to_polar
from .util import share_fig_ax, rms
from .convolution import Convolvable
from .propagation import (
    prop_pupil_plane_to_psf_plane,
    prop_pupil_plane_to_psf_plane_units,
)

from prysm import mathops as m


class PSF(Convolvable):
    """A Point Spread Function.

    Attributes
    ----------
    center_x : `int`
        center sample along x
    center_y : `int`
        center sample along y
    data : `numpy.ndarray`
        PSF normalized intensity data
    sample_spacing : `float`
        center to center spacing of samples
    unit_x : `numpy.ndarray`
        x Cartesian axis locations of samples, 1D ndarray
    unit_y `numpy.ndarray`
        y Cartesian axis locations of samples, 1D ndarray

    """
    def __init__(self, data, unit_x, unit_y):
        """Create a PSF object.

        Parameters
        ----------
        data : `numpy.ndarray`
            intensity data for the PSF
        unit_x : `numpy.ndarray`
            1D ndarray defining x data grid
        unit_y  : `numpy.ndarray`
            1D ndarray defining y data grid
        sample_spacing : `float`
            center-to-center spacing of samples, expressed in microns

        """
        super().__init__(data, unit_x, unit_y, has_analytic_ft=False)
        self.data /= self.data.max()
        self._ee = {}

    # quick-access slices ------------------------------------------------------

    @property
    def slice_x(self):
        """Retrieve a slice through the x axis of the PSF.

        Returns
        -------
        self.unit_x : `numpy.ndarray`
            ordinate data
        self.data : `numpy.ndarray`
            coordinate data

        """
        return self.unit_y, self.data[:, self.center_x]

    @property
    def slice_y(self):
        """Retrieve a slice through the y axis of the PSF.

        Returns
        -------
        self.unit_y : `numpy.ndarray`
            ordinate data
        self.data : `numpy.ndarray`
            coordinate data

        """
        return self.unit_x, self.data[self.center_y, :]

    def encircled_energy(self, radius):
        """Compute the encircled energy of the PSF

        Parameters
        ----------
        radius : `float` or iterable
            radius or radii to evaluate encircled energy at

        Returns
        -------
        encircled energy
            if radius is a float, returns a float, else returns a list.

        Notes
        -----
        implementation of "Simplified Method for Calculating Encircled Energy,"
        Baliga, J. V. and Cohn, B. D., doi: 10.1117/12.944334

        """
        # TODO: look if Notes should be above or below returns to be consistent
        # with the rest of prysm
        from .otf import MTF

        if hasattr(radius, '__iter__'):
            # user wants multiple points
            # um to mm, cy/mm assumed in Fourier plane
            radius = m.asarray(radius) / 1e3
            radius_is_array = True
        else:
            radius /= 1e3
            radius_is_array = False

        # compute MTF from the PSF
        mtf = MTF.from_psf(self)
        ny, nx = m.meshgrid(mtf.unit_y, mtf.unit_x)
        nu_p = m.sqrt(nx ** 2 + ny ** 2)
        dy, dx = nx[1, 0] - nx[0, 0], ny[0, 1] - ny[0, 0]

        if radius_is_array:
            for r in radius:
                out = []
                if round(r, 4) not in self._ee:
                    self._ee[round(r, 4)] = _encircled_energy_core(mtf.data,
                                                                   r,
                                                                   nu_p,
                                                                   dx,
                                                                   dy)
                out.append(self._ee[round(r, 4)])
            return [out]
        else:
            if round(r, 4) not in self._ee:
                self._ee[round(radius, 4)] = _encircled_energy_core(mtf.data,
                                                                    radius,
                                                                    nu_p,
                                                                    dx,
                                                                    dy)
            return self._ee[round(radius, 4)]

    # quick-access slices ------------------------------------------------------

    # plotting -----------------------------------------------------------------

    def plot2d(self, axlim=25, power=1, interp_method='lanczos',
               pix_grid=None, fig=None, ax=None,
               show_axlabels=True, show_colorbar=True,
               circle_ee=None):
        """Create a 2D plot of the PSF.

        Parameters
        ----------
        axlim : `float`
            limits of axis, symmetric. xlim=(-axlim,axlim), ylim=(-axlim, axlim)
        power : `float`
            power to stretch the data by for plotting
        interp_method : `string`
            method used to interpolate the image between samples of the PSF
        pix_grid : `float`
            if not None, overlays gridlines with spacing equal to pix_grid.
            Intended to show the collection into camera pixels while still in
            the oversampled domain
        fig : `matplotlib.figure.Figure`, optional:
            Figure containing the plot
        ax : `matplotlib.axes.Axis`, optional:
            Axis containing the plot
        show_axlabels : `bool`
            whether or not to show the axis labels
        show_colorbar : `bool`
            whether or not to show the colorbar
        circle_ee : `float`, optional
            percent encircled energy to draw a circle at, in addition to
            diffraction limited airy radius (1.22*λ*F#)

        Returns
        -------
        fig : `matplotlib.figure.Figure`, optional
            Figure containing the plot
        ax : `matplotlib.axes.Axis`, optional
            Axis containing the plot

        """
        label_str = 'Normalized Intensity [a.u.]'
        lims = (0, 1)

        left, right = self.unit_x[0], self.unit_x[-1]
        bottom, top = self.unit_y[0], self.unit_y[-1]

        fig, ax = share_fig_ax(fig, ax)

        im = ax.imshow(self.data,
                       extent=[left, right, bottom, top],
                       origin='lower',
                       cmap='Greys_r',
                       norm=colors.PowerNorm(1/power),
                       interpolation=interp_method,
                       clim=lims)
        if show_colorbar:
            cb = fig.colorbar(im, label=label_str, ax=ax, fraction=0.046)
            cb.outline.set_edgecolor('k')
            cb.outline.set_linewidth(0.5)
        if show_axlabels:
            ax.set(xlabel=r'Image Plane $x$ [$\mu m$]',
                   ylabel=r'Image Plane $y$ [$\mu m$]')

        ax.set(xlim=(-axlim, axlim),
               ylim=(-axlim, axlim))

        if pix_grid is not None:
            # if pixel grid is desired, add it
            mult = m.floor(axlim / pix_grid)
            gmin, gmax = -mult * pix_grid, mult * pix_grid
            pts = m.arange(gmin, gmax, pix_grid)
            ax.set_yticks(pts, minor=True)
            ax.set_xticks(pts, minor=True)
            ax.yaxis.grid(True, which='minor', color='white', alpha=0.25)
            ax.xaxis.grid(True, which='minor', color='white', alpha=0.25)

        if circle_ee is not None:
            if self.fno is None:
                raise ValueError('F/# must be known to compute EE, set self.fno')
            elif self.wavelength is None:
                raise ValueError('wavelength must be known to compute EE, set self.wavelength')

            first_null = 1.22 * self.wavelength * self.fno
            rms = getattr(self, 'rmswfe', 0)
            if rms < 0.1:
                factor = 3
            elif rms < 0.25:
                factor = 4
            elif rms < 0.5:
                factor = 5
            elif rms < 0.75:
                factor = 8
            elif rms < 2:
                factor = 10
            else:
                factor = 20

            pts = m.linspace(0, factor * first_null, 100)
            ee = self.encircled_energy(pts)

            c = circle_ee / 100
            radius = pts[m.searchsorted(ee, c)]
            analytic = _analytical_encircled_energy(self.fno, self.wavelength, pts)
            rad_analytic = pts[m.searchsorted(analytic, c)]
            c_diff = patches.Circle((0, 0), rad_analytic, fill=False, color='r', ls='--')
            c_true = patches.Circle((0, 0), radius, fill=False, color='r')
            ax.add_artist(c_diff)
            ax.add_artist(c_true)

        return fig, ax

    def plot_slice_xy(self, axlim=20, fig=None, ax=None):
        """Create a plot of slices through the X and Y axes of the `PSF`.

        Parameters
        ----------
        axlim : `float` or `int`
            axis limits, in microns
        fig : `matplotlib.figure.Figure`, optional
            Figure to draw plot in
        ax : `matplotlib.axes.Axis`
            Axis to draw plot in

        Returns
        -------
        fig : `matplotlib.figure.Figure`, optional
            Figure containing the plot
        ax : `matplotlib.axes.Axis`, optional
            Axis containing the plot

        """
        ux, x = self.slice_x
        uy, y = self.slice_y
        label_str = 'Normalized Intensity [a.u.]'
        lims = (0, 1)

        fig, ax = share_fig_ax(fig, ax)

        ax.plot(ux, x, label='Slice X', lw=3)
        ax.plot(uy, y, label='Slice Y', lw=3)
        ax.set(xlabel=r'Image Plane X [$\mu m$]',
               ylabel=label_str,
               xlim=(-axlim, axlim),
               ylim=lims)
        ax.legend(loc='upper right')
        return fig, ax

    def plot_encircled_energy(self, azimuth=None, axlim=20, fig=None, ax=None):
        """Make a 1D plot of the encircled energy at the given azimuth.

        Parameters
        ----------
        azimuth : `float`
            azimuth to plot at, in degrees
        axlim : `float`
            limits of axis, will plot [0, axlim]
        fig : `matplotlib.figure.Figure`, optional
            Figure containing the plot
        ax : `matplotlib.axes.Axis`, optional:
            Axis containing the plot

        Returns
        -------
        fig : `matplotlib.figure.Figure`, optional
            Figure containing the plot
        ax : `matplotlib.axes.Axis`, optional:
            Axis containing the plot

        """
        unit, data = self.encircled_energy(azimuth)

        fig, ax = share_fig_ax(fig, ax)
        ax.plot(unit, data, lw=3)
        ax.set(xlabel=r'Image Plane Distance [$\mu m$]',
               ylabel=r'Encircled Energy [Rel 1.0]',
               xlim=(0, axlim))
        return fig, ax

    # plotting -----------------------------------------------------------------

    # helpers ------------------------------------------------------------------

    def _renorm(self, to='peak'):
        """Renormalize the PSF to unit peak intensity.

        Parameters
        ----------
        to : `string`, {'peak', 'total'}
            renormalization target; produces a PSF of unit peak or total intensity

        Returns
        -------
        `PSF`
            a renormalized PSF instance

        """
        if to.lower() == 'peak':
            self.data /= self.data.max()
        elif to.lower() == 'total':
            ttl = self.data.sum()
            self.data /= ttl
        return self

    # helpers ------------------------------------------------------------------

    @staticmethod
    def from_pupil(pupil, efl, Q=2):
        """Use scalar diffraction propogation to generate a PSF from a pupil.

        Parameters
        ----------
        pupil : `Pupil`
            Pupil, with OPD data and wavefunction
        efl : `int` or `float`
            effective focal length of the optical system
        Q : `int` or `float`
            ratio of pupil sample count to PSF sample count; Q > 2 satisfies nyquist

        Returns
        -------
        `PSF`
            A new PSF instance

        """
        # propagate PSF data
        fcn, ss, wvl = pupil.fcn, pupil.sample_spacing, pupil.wavelength
        data = prop_pupil_plane_to_psf_plane(fcn, ss, efl, wvl, Q)
        ux, uy = prop_pupil_plane_to_psf_plane_units(fcn, ss, efl, wvl, Q)
        psf = PSF(data, ux, uy)

        # determine the F/#, assumes:
        # - pupil fills x or y width of array
        # - pupil is not elliptical at an odd angle
        s = pupil.fcn.shape
        if s[1] > s[0]:
            u = pupil.unit_x
        else:
            u = pupil.unit_y

        if u[0] == -1 * u[-1]:
            epd = u[-1] * 2
        else:
            epd = u[-1]

        psf.fno = efl / epd
        psf.wavelength = wvl

        # finally, store the RMS WFE
        psf.rmswfe = rms(pupil.change_phase_unit(to='waves', inplace=False))
        return psf


class MultispectralPSF(PSF):
    """A PSF which includes multiple wavelength components.
    """
    def __init__(self, psfs, weights=None):
        '''Create a new `MultispectralPSF` instance.

        Parameters
        ----------
        psfs : iterable
            iterable of PSFs
        weights : iterable
            iterable of weights associated with each PSF

        '''
        if weights is None:
            weights = [1] * len(psfs)

        # find the most densely sampled PSF
        min_spacing = 1e99
        ref_idx = None
        ref_unit_x = None
        ref_unit_y = None
        ref_samples_x = None
        ref_samples_y = None
        for idx, psf in enumerate(psfs):
            if psf.sample_spacing < min_spacing:
                min_spacing = psf.sample_spacing
                ref_idx = idx
                ref_unit_x = psf.unit_x
                ref_unit_y = psf.unit_y
                ref_samples_x = psf.samples_x
                ref_samples_y = psf.samples_y

        merge_data = m.zeros((ref_samples_x, ref_samples_y, len(psfs)))
        for idx, psf in enumerate(psfs):
            # don't do anything to our reference PSF
            if idx is ref_idx:
                merge_data[:, :, idx] = psf.data * weights[idx]
            else:
                xv, yv = m.meshgrid(ref_unit_x, ref_unit_y)
                interpf = interpolate.RegularGridInterpolator((psf.unit_x, psf.unit_y), psf.data)
                merge_data[:, :, idx] = interpf((xv, yv), method='linear') * weights[idx]

        self.weights = weights
        super().__init__(merge_data.sum(axis=2), min_spacing)
        self._renorm()


class RGBPSF(object):
    """Trichromatic PSF, intended to show chromatic aberrations."""
    def __init__(self, r_psf, g_psf, b_psf):
        '''Create a new `RGBPSF` instance.

        Parameters
        ----------
        r_psf : `PSF`
            PSF for the red channel
        g_psf : `PSF`
            PSF for the green channel
        b_psf : `PSF`
            PSF for the blue channel

        '''
        if m.array_equal(r_psf.unit_x, g_psf.unit_x) and \
           m.array_equal(g_psf.unit_x, b_psf.unit_x) and \
           m.array_equal(r_psf.unit_y, g_psf.unit_y) and \
           m.array_equal(g_psf.unit_y, b_psf.unit_y):
            # do not need to interpolate the arrays
            self.R = r_psf.data
            self.G = g_psf.data
            self.B = b_psf.data
        else:
            # need to interpolate the arrays.  Blue tends to be most densely
            # sampled, use it to define our grid
            self.B = b_psf.data

            xv, yv = m.meshgrid(b_psf.unit_x, b_psf.unit_y)
            interpf_r = interpolate.RegularGridInterpolator((r_psf.unit_y, r_psf.unit_x), r_psf.data)
            interpf_g = interpolate.RegularGridInterpolator((g_psf.unit_y, g_psf.unit_x), g_psf.data)
            self.R = interpf_r((yv, xv), method='linear')
            self.G = interpf_g((yv, xv), method='linear')

        self.sample_spacing = b_psf.sample_spacing
        self.samples_x = b_psf.samples_x
        self.samples_y = b_psf.samples_y
        self.unit_x = b_psf.unit_x
        self.unit_y = b_psf.unit_y
        self.center_x = b_psf.center_x
        self.center_y = b_psf.center_y

    def _renorm(self, to='peak'):
        """Renormalize the PSF to unit peak intensity.

        Parameters
        ----------
        to : `string`, {'peak', 'total'}
            renormalization target; produces a PSF of unit peak or total intensity

        Returns
        -------
        `PSF`
            a renormalized PSF instance

        """
        if to.lower() == 'peak':
            self.R /= self.R.max()
            self.G /= self.G.max()
            self.B /= self.B.max()
        elif to.lower() == 'total':
            # scale to energy of the green channel.  First, make all unit peak
            self.R /= self.R.max()
            self.G /= self.G.max()
            self.B /= self.B.max()

            # compute energy of green, scale all to this value
            ttl = self.G.sum()
            self.R /= ttl
            self.G /= ttl
            self.B /= ttl
        return self

    @property
    def r_psf(self):
        """R color plane PSF.

        Returns
        -------
        `PSF`
            A PSF instance

        """
        return PSF(self.R, self.sample_spacing)

    @property
    def g_psf(self):
        """G color plane PSF.

        Returns
        -------
        `PSF`
            A PSF instance

        """
        return PSF(self.G, self.sample_spacing)

    @property
    def b_psf(self):
        """B color plane PSF.

        Returns
        -------
        `PSF`
            A PSf instance

        """
        return PSF(self.B, self.sample_spacing)

    def plot2d(self, axlim=25, interp_method='lanczos', pix_grid=None, fig=None, ax=None):
        '''Create a 2D color plot of the PSF.

        Parameters
        ----------
        axlim : `float`
            limits of axis, symmetric. xlim=(-axlim,axlim), ylim=(-axlim, axlim)
        interp_method : `str`
            method used to interpolate the image between samples of the PSF
        pix_grid : `float`
            if not None, overlays gridlines with spacing equal to pix_grid.
            Intended to show the collection into camera pixels while still in
            the oversampled domain
        fig : `matplotlib.figure.Figure`, optional
            Figure containing the plot
        ax : `matplotlib.axes.Axis`, optional:
            Axis containing the plot

        Returns
        -------
        fig : `matplotlib.figure.Figure`, optional
            Figure containing the plot
        ax : `matplotlib.axes.Axis`, optional:
            Axis containing the plot

        '''
        dat = m.empty((self.samples_x, self.samples_y, 3))
        dat[:, :, 0] = self.R
        dat[:, :, 1] = self.G
        dat[:, :, 2] = self.B

        left, right = self.unit_y[0], self.unit_y[-1]
        bottom, top = self.unit_x[0], self.unit_x[-1]

        fig, ax = share_fig_ax(fig, ax)

        ax.imshow(dat,
                  extent=[left, right, bottom, top],
                  interpolation=interp_method,
                  origin='lower')
        ax.set(xlabel=r'Image Plane X [$\mu m$]',
               ylabel=r'Image Plane Y [$\mu m$]',
               xlim=(-axlim, axlim),
               ylim=(-axlim, axlim))

        if pix_grid is not None:
            # if pixel grid is desired, add it
            mult = m.floor(axlim / pix_grid)
            gmin, gmax = -mult * pix_grid, mult * pix_grid
            pts = m.arange(gmin, gmax, pix_grid)
            ax.set_yticks(pts, minor=True)
            ax.set_xticks(pts, minor=True)
            ax.yaxis.grid(True, which='minor')
            ax.xaxis.grid(True, which='minor')

        return fig, ax

    def plot2d_rgbgrid(self, axlim=25, interp_method='lanczos',
                       pix_grid=None, fig=None, ax=None):
        """Create a 2D color plot of the PSF and R,G,B components.

        Parameters
        ----------
        axlim : `float`
            limits of axis, symmetric. xlim=(-axlim,axlim), ylim=(-axlim, axlim)
        interp_method : `str`
            method used to interpolate the image between samples of the PSF
        pix_grid : float
            if not None, overlays gridlines with spacing equal to pix_grid.
            Intended to show the collection into camera pixels while still in
            the oversampled domain
        fig : `matplotlib.figure.Figure`, optional
            Figure containing the plot
        ax : `matplotlib.axes.Axis`, optional:
            Axis containing the plot

        fig : `matplotlib.figure.Figure`, optional
            Figure containing the plot
        ax : `matplotlib.axes.Axis`, optional:
            Axis containing the plot

        Notes
        -----
        Need to refine internal workings at some point.

        """
        # make the arrays for the RGB images
        dat = m.empty((self.samples_y, self.samples_x, 3))
        datr = m.zeros((self.samples_y, self.samples_x, 3))
        datg = m.zeros((self.samples_y, self.samples_x, 3))
        datb = m.zeros((self.samples_y, self.samples_x, 3))
        dat[:, :, 0] = self.R
        dat[:, :, 1] = self.G
        dat[:, :, 2] = self.B
        datr[:, :, 0] = self.R
        datg[:, :, 1] = self.G
        datb[:, :, 2] = self.B

        left, right = self.unit[0], self.unit[-1]
        ax_width = 2 * axlim

        # generate a figure and axes to plot in
        fig, ax = share_fig_ax(fig, ax)
        axr, axg, axb = make_rgb_axes(ax)

        ax.imshow(dat,
                  extent=[left, right, left, right],
                  interpolation=interp_method,
                  origin='lower')

        axr.imshow(datr,
                   extent=[left, right, left, right],
                   interpolation=interp_method,
                   origin='lower')
        axg.imshow(datg,
                   extent=[left, right, left, right],
                   interpolation=interp_method,
                   origin='lower')
        axb.imshow(datb,
                   extent=[left, right, left, right],
                   interpolation=interp_method,
                   origin='lower')

        for axs in (ax, axr, axg, axb):
            ax.set(xlim=(-axlim, axlim), ylim=(-axlim, axlim))
            if pix_grid is not None:
                # if pixel grid is desired, add it
                mult = m.m.floor(axlim / pix_grid)
                gmin, gmax = -mult * pix_grid, mult * pix_grid
                pts = m.arange(gmin, gmax, pix_grid)
                ax.set_yticks(pts, minor=True)
                ax.set_xticks(pts, minor=True)
                ax.yaxis.grid(True, which='minor')
                ax.xaxis.grid(True, which='minor')
        ax.set(xlabel=r'Image Plane X [$\mu m$]', ylabel=r'Image Plane Y [$\mu m$]')
        axr.text(-axlim + 0.1 * ax_width, axlim - 0.2 * ax_width, 'R', color='white')
        axg.text(-axlim + 0.1 * ax_width, axlim - 0.2 * ax_width, 'G', color='white')
        axb.text(-axlim + 0.1 * ax_width, axlim - 0.2 * ax_width, 'B', color='white')
        return fig, ax


class AiryDisk(PSF):
    """An airy disk, the PSF of a circular aperture."""
    def __init__(self, fno, wavelength, extent, samples):
        """Create a new AiryDisk.

        Parameters
        ----------
        fno : `float`
            F/# associated with the PSF
        wavelength : `float`
            wavelength of light, in microns
        extent : `float`
            cartesian window half-width, e.g. 10 will make an RoI 20x20 microns wide
        samples : `int`
            number of samples across full width

        """
        x = m.linspace(-extent, extent, samples)
        y = m.linspace(-extent, extent, samples)
        xx, yy = m.meshgrid(x, y)
        rho, phi = cart_to_polar(xx, yy)
        data = _airydisk(rho, fno, wavelength)
        self.fno = fno
        self.wavelength = wavelength
        super().__init__(data, x, y)


def _airydisk(unit_r, fno, wavelength):
    """Compute the airy disk function over a given spatial distance.

    Parameters
    ----------
    unit_r : `numpy.ndarray`
        ndarray with units of um
    fno : `float`
        F/# of the system
    wavelength : `float`
        wavelength of light, um

    Returns
    -------
    `numpy.ndarray`
        ndarray containing the airy pattern

    """
    u_eff = unit_r * m.pi / wavelength / fno
    return abs(2 * m.jinc(u_eff)) ** 2


def _encircled_energy_core(mtf_data, radius, nu_p, dx, dy):
    """Core computation of encircled energy, based on Baliga 1988.

    Parameters
    ----------
    mtf_data : `numpy.ndarray`
        unaliased MTF data
    radius : `float`
        radius of "detector"
    nu_p : `numpy.ndarray`
        radial spatial frequencies
    dx : `float`
        x frequency delta
    dy : `float`
        y frequency delta

    Returns
    -------
    `float`
        encircled energy for given radius

    """
    integration_fourier = m.j1(2 * m.pi * radius * nu_p) / nu_p
    # division by nu_p will cause a NaN at the origin, 0.5 is the
    # analytical value of jinc there
    integration_fourier[m.isnan(integration_fourier)] = 0.5
    dat = mtf_data * integration_fourier
    return radius * dat.sum() * dx * dy


def _analytical_encircled_energy(fno, wavelength, points):
    """Compute the analytical encircled energy for a diffraction limited circular aperture

    Parameters
    ----------
    fno : `float`
        F/#
    wavelength : `float`
        wavelength of light
    points : `numpy.ndarray`
        radii of "detector"

    Returns
    -------
    `numpy.ndarray`
        encircled energy values

    """
    p = points * m.pi / fno / wavelength
    return 1 - m.j0(p)**2 - m.j1(p)**2

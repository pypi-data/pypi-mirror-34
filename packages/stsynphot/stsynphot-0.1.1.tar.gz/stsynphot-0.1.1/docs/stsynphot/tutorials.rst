.. doctest-skip-all

.. _stsynphot-tutorials:

Tutorials
=========

This page contains tutorials of specific **stsynphot** functionality not
explicitly covered in other sections.


.. _tutorial_countrate_multi_aper:

Count Rates for Multiple Apertures
----------------------------------

In this tutorial, you will learn how to calculate count rates for observations
of the same source and bandpass, but with different apertures. Note that this
feature is only available for observing modes that allow encircled energy (EE)
radius specification (see :ref:`stsynphot-appendixb`).

Create two observations of Vega (renormalized to 20 STMAG in Johnson *V*) with
ACS/WFC1 F555W bandpass, with 0.3 and 1.0 arcsec EE radii, respectively::

    >>> import stsynphot as STS
    >>> from astropy import units as u
    >>> from synphot import Observation
    >>> sp = STS.Vega.normalize(20 * u.STmag, STS.band('johnson,v'))
    >>> obs03 = Observation(sp, STS.band('acs,wfc1,f555w,aper#0.3'))
    >>> obs10 = Observation(sp, STS.band('acs,wfc1,f555w,aper#1.0'))

Calculate the count rates for both and display the results::

    >>> c03 = obs03.countrate(STS.conf.area)
    >>> c10 = obs10.countrate(STS.conf.area)
    >>> print('Count rate for 0.3" is {:.3f}\n'
    ...       'Count rate for 1.0" is {:.3f}'.format(c03, c10))
    Count rate for 0.3" is 174.801 ct / s
    Count rate for 1.0" is 186.521 ct / s


.. _tutorial_band_stmag:

Bandpass STMAG Zeropoint
------------------------

HST bandpasses store their :ref:`synphot:synphot-formula-uresp` values under
the ``PHOTFLAM`` keyword in image headers. This keyword is then used to compute
STMAG zeropoint for the respective bandpass (e.g.,
`ACS <http://www.stsci.edu/hst/acs/analysis/zeropoints>`_ and
`WFC3 <http://www.stsci.edu/hst/wfc3/phot_zp_lbn>`_).

In this tutorial, you will learn how to calculate the STMAG zeropoint for
the ACS/WFC1 F555W bandpass, which happens to be time-dependent::

    >>> import numpy as np
    >>> import stsynphot as STS
    >>> from astropy.time import Time
    >>> obsdate = Time('2017-05-30').mjd
    >>> bp = STS.band('acs,wfc1,f555w,mjd#{}'.format(obsdate))
    >>> photflam = bp.unit_response(STS.conf.area)
    >>> photflam
    <Quantity 1.9647813651514673e-19 FLAM>
    >>> st_zpt = -2.5 * np.log10(photflam.value) - 21.1
    >>> print('STmag zeropoint for {} is {:.5f}'.format(bp.obsmode, st_zpt))
    STmag zeropoint for acs,wfc1,f555w,mjd#57903.0 is 25.66671


.. _tutorial_band_abmag:

Bandpass ABMAG Zeropoint
------------------------

For ABMAG zeropoint, it extends from :ref:`tutorial_band_stmag` by also using
``PHOTPLAM`` keyword in image headers.

In this tutorial, you will learn how to calculate the ABMAG zeropoint for
the ACS/WFC1 F555W bandpass, which happens to be time-dependent::

    >>> import numpy as np
    >>> import stsynphot as STS
    >>> from astropy.time import Time
    >>> obsdate = Time('2017-05-30').mjd
    >>> bp = STS.band('acs,wfc1,f555w,mjd#{}'.format(obsdate))
    >>> photflam = bp.unit_response(STS.conf.area)
    >>> photplam = bp.pivot()
    >>> photplam
    <Quantity 5360.938362432486 Angstrom>
    >>> ab_zpt = (-2.5 * np.log10(photflam.value) - 21.1 -
    ...           5 * np.log10(photplam.value) + 18.6921)
    >>> print('ABmag zeropoint for {} is {:.5f}'.format(bp.obsmode, ab_zpt))
    ABmag zeropoint for acs,wfc1,f555w,mjd#57903.0 is 25.71261


.. _tutorial_band_vegamag:

Bandpass VEGAMAG Zeropoint
--------------------------

In addition to :ref:`tutorial_band_stmag` and :ref:`tutorial_band_abmag`,
HST bandpasses also provide zeropoints in ``VEGAMAG``, which is a magnitude
system where Vega has magnitude 0 at all wavelengths. Note that this zeropoint
strongly depends on the actual Vega spectrum used; Therefore, VEGAMAG zeropoint
values for the same filter might vary in literature as the authors use their
favorite Vega spectra.

In this tutorial, you will learn how to calculate the VEGAMAG zeropoint for
the ACS/WFC1 F555W bandpass, which happens to be time-dependent::

    >>> import numpy as np
    >>> import stsynphot as STS
    >>> from astropy.time import Time
    >>> from synphot import Observation
    >>> obsdate = Time('2017-05-30').mjd
    >>> bp = STS.band('acs,wfc1,f555w,mjd#{}'.format(obsdate))
    >>> obs = Observation(STS.Vega, bp, binset=bp.binset)
    >>> vega_zpt = -obs.effstim(flux_unit='obmag', area=STS.conf.area)
    >>> print('VEGAMAG zeropoint for {} is {:.5f}'.format(bp.obsmode, vega_zpt))
    VEGAMAG zeropoint for acs,wfc1,f555w,mjd#57903.0 is 25.71235 OBMAG


.. _tutorial_sun_absmag:

Sun's Abs. Mag. in HST Filters
------------------------------

In this tutorial, you will learn how to calculate the absolute magnitude of the
Sun for three different HST filters.
Sun's spectrum can be obtained from :ref:`stsynphot-appendixa-calspec` but
needs to be normalized to literature value
(e.g., http://www.astronomynotes.com/starprop/s4.htm)::

    >>> import stsynphot as STS
    >>> from synphot import units, SourceSpectrum, SpectralElement, Observation
    >>> v_band = SpectralElement.from_filter('johnson_v')
    >>> sun_file = 'ftp://ftp.stsci.edu/cdbs/calspec/sun_reference_stis_002.fits'
    >>> sun_raw = SourceSpectrum.from_file(sun_file)
    >>> sun = sun_raw.normalize(4.83 * units.VEGAMAG, v_band, vegaspec=STS.Vega)
    >>> for obsmode in ['acs,wfc1,f555w', 'wfc3,uvis2,f336w', 'wfc3,ir,f160w']:
    ...     bp = STS.band(obsmode)
    ...     obs = Observation(sun, bp, binset=bp.binset)
    ...     m = obs.effstim('vegamag', vegaspec=STS.Vega)
    ...     print("Sun's abs mag in {} is {:.4f}".format(bp.obsmode, m))
    Sun's abs mag in acs,wfc1,f555w is 4.8395 VEGAMAG
    Sun's abs mag in wfc3,uvis2,f336w is 5.4864 VEGAMAG
    Sun's abs mag in wfc3,ir,f160w is 3.4127 VEGAMAG


.. _tutorial_wavetab:

Custom Wavelength Table
-----------------------

In this tutorial, you will learn how to create a custom wavelength array and
save it to a FITS table using `astropy.io.fits`. Then, you will read the array
back in from file, and use it to define detector binning for an observation.

Suppose we want a wavelength set that ranges from 2000 to 8000 Angstrom, with
1 Angstrom spacing over most of the range, but 0.1 Angstrom spacing
around the [O III] forbidden lines at 4959 and 5007 Angstrom.

Create the 3 regions separately, concatenate them, and display the result::

    >>> import numpy as np
    >>> lowave = np.arange(2000, 4950)
    >>> mdwave = np.arange(4950, 5010, 0.1)  # [O III]
    >>> hiwave = np.arange(5010, 8000)
    >>> wave = np.concatenate([lowave, mdwave, hiwave])
    >>> wave
    array([ 2000.,  2001.,  2002., ...,  7997.,  7998.,  7999.])

Create an Astropy table from the concatenated array above and save it out as a
FITS table::

    >>> from astropy.io import fits
    >>> col = fits.Column(
    ...     name='wavelength', unit='angstrom', format='E', array=wave)
    >>> tabhdu = fits.BinTableHDU.from_columns([col])
    >>> tabhdu.writeto('mywaveset.fits')

Read the custom wavelength set back in from file using Astropy table::

    >>> from astropy.table import QTable
    >>> tab = QTable.read('mywaveset.fits')  # Ignore the UnitsWarning
    WARNING: UnitsWarning: The unit 'angstrom' has been deprecated...
    >>> wave = tab['wavelength']
    >>> wave
    <Quantity [ 2000., 2001., 2002.,...,  7997., 7998., 7999.] Angstrom>

Create an observation of Vega with ACS/WFC1 F555W bandpass, using the custom
wavelength binning above, and then check that the binned wavelength set is
indeed the given one::

    >>> import stsynphot as STS
    >>> from synphot import Observation
    >>> obs = Observation(STS.Vega, STS.band('acs,wfc1,f555w'), binset=wave)
    >>> obs.binset
    <Quantity [ 2000., 2001., 2002.,...,  7997., 7998., 7999.] Angstrom>

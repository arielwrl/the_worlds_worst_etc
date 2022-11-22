"""

ariel@oapd

Problem: Kieran wants to study the initial mass function of an open cluster in the Large Magellanic Cloud.
He plans to use the HAWK-I instrument on the VLT and would like to know what the faintest stars are that will be
detectable (S/N > 5) with 1 hour of observing time in the K filter. He assumes average (50th percentile)
observing conditions will apply for the observation

FIXME: This is a highly convoluted implementation
TODO: Include effect of atmosphere

"""

import numpy as np
import matplotlib.pyplot as plt
import hmbp
from astropy import units as u


def calculate_snr(in_flux, exposure_time):

    n_photons = hmbp.for_flux_in_filter(filter_name='Ks', flux=in_flux, instrument='HAWKI', observatory='Paranal')

    snr = np.sqrt(n_photons.value * (8 ** 2) * exposure_time)

    return snr


def plot_snr_magnitude(magnitude_range, exposure_time, target_snr=None, show_plot=True):

    magnitude_values = np.arange(magnitude_range[0], magnitude_range[1], 0.1)
    snr_values = np.array([calculate_snr(magnitude*u.ABmag, exposure_time) for magnitude in magnitude_values])

    plt.plot(magnitude_values, snr_values)

    if target_snr is not None:
        plt.axhline(y=target_snr, color='k', ls='dashed')

    if show_plot:
        plt.show()


def calculate_absolute_magnitude(apparent_magnitude, distance):

    absolute_magnitude = apparent_magnitude - 2.5 * np.log10(distance/10)

    return absolute_magnitude


def find_faintest_magnitude(magnitude_range, target_snr, exposure_time):
    """

    Searches a magnitude range to find the minimum apparent magnitude of a target given a target SNR and exposure time

    :param magnitude_range: magnitude range to perform search (list)
    :param target_snr: target SNR of the observation
    :param exposure_time: desired exposure time in seconds
    :return: faintest magnitude observed with SNR > target_snr within the exposure time
    """

    magnitude_values = np.arange(magnitude_range[0], magnitude_range[1], 0.1)
    snr_values = np.array([calculate_snr(magnitude*u.ABmag, exposure_time) for magnitude in magnitude_values])

    faintest_magnitude = np.max(magnitude_values[snr_values > target_snr])

    return faintest_magnitude




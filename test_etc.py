"""

ariel@oapd

Tests the functions included in testposure_time.py and prints final answer.

Note that this excercise is oversimplified as no backround photons were considered.

"""

import testposure_time as etc

# First, find the minimum apparent magnitude detectable:
faintest_apparent_magnitude = etc.find_faintest_magnitude(magnitude_range=[30, 40], target_snr=5, exposure_time=3600)

# Assuming the distance of 50kpc to the LMC, the absolute magnitude is given by:
absolute_magnitude = etc.calculate_absolute_magnitude(faintest_apparent_magnitude, 50*10**3)

# Print result (should be 24.75):
print('Under these conditions it is possible to observe an object of absolute magnitude ', absolute_magnitude)
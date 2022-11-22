# The world's worst exposure time calculator (ETC)
    
A crude implementation of an exposure time calculator.

### Goal: 
Find the faintest stars are that are detectable (S/N > 5) with 1 hour of observing time in the K filter of HAWK-I in the VLT.

### Implementation:
The main funcion of the module is `find_faintest_magnitude()`, it calculates the magnitude against SNR relation and finds the faintest apparent magnitude corresponding to a certain SNR. The relation can be plotted with `plot_snr_magnitude()`.
The number of photons reaching the detector is calculated using `hmbp.for_flux_in_filter()` with `filter_name='Ks'`, `instrument='HAWKI'` and `observatory='Paranal'`.

### Dependencies:
`numpy`, `matplotlib`, `astropy`, `HowManyPhotons`

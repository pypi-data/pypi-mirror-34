
from libpysat.transform.baseline_code.airpls import AirPLS
from libpysat.transform.baseline_code.als import ALS
from libpysat.transform.baseline_code.ccam_remove_continuum import ccam_br
from libpysat.transform.baseline_code.dietrich import Dietrich
from libpysat.transform.baseline_code.fabc import FABC
from libpysat.transform.baseline_code.kajfosz_kwiatek import KajfoszKwiatek as KK
from libpysat.transform.baseline_code.mario import Mario
from libpysat.transform.baseline_code.median import MedianFilter
from libpysat.transform.baseline_code.polyfit import PolyFit
from libpysat.transform.baseline_code.rubberband import Rubberband
import numpy as np

# This function applies baseline removal to the data
def remove_baseline(df, method='ALS', segment=True, params=None):
    wvls = np.array(df['wvl'].columns.values, dtype='float')
    spectra = np.array(df['wvl'], dtype='float')

    # set baseline removal object (br) to the specified method
    if method == 'ALS':
        br = ALS()
    elif method == 'Dietrich':
        br = Dietrich()
    elif method == 'Polyfit':
        br = PolyFit()
    elif method == 'AirPLS':
        br = AirPLS()
    elif method == 'FABC':
        br = FABC()
    elif method == 'KK':
        br = KK()
    elif method == 'Mario':
        br = Mario()
    elif method == 'Median':
        br = MedianFilter()
    elif method == 'Rubberband':
        br = Rubberband()
    elif method == 'Stationary Wavelets':
        br = ccam_br()
        # if method == 'wavelet':
        #   br=Wavelet()
    else:
        print(method + ' is not recognized!')

    # if parameters are provided, use them to set the parameters of br
    if params is not None:
        for i in params.keys():
            try:
                setattr(br, i, params[i])
            except:
                print('Required keys are:')
                print(br.__dict__.keys())
                print('Exiting without removing baseline!')
                return
    br.fit(wvls, spectra, segment=segment)
    df_baseline = df.copy()
    df_baseline['wvl'] = br.baseline
    df['wvl'] = df['wvl']-df_baseline['wvl']

    return df, df_baseline
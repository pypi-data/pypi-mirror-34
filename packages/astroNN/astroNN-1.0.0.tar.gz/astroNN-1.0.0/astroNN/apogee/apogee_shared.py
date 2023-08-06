# ---------------------------------------------------------#
#   astroNN.apogee.apogee_shared: shared functions for apogee
# ---------------------------------------------------------#

import os


def apogee_env():
    """
    NAME:
        apogee_env
    PURPOSE:
        get APOGEE environment variable
    INPUT:
        None
    OUTPUT:
        (path)
    HISTORY:
        2017-Oct-26 - Written - Henry Leung
    """
    from astroNN.config import ENVVAR_WARN_FLAG
    _APOGEE = os.getenv('SDSS_LOCAL_SAS_MIRROR')
    if _APOGEE is None and ENVVAR_WARN_FLAG is True:
        print("WARNING! APOGEE environment variable SDSS_LOCAL_SAS_MIRROR not set")

    return _APOGEE


def apogee_default_dr(dr=None):
    """
    NAME:
        apogee_default_dr
    PURPOSE:
        Check if dr argument is provided, if none then use default
    INPUT:
        dr (int): APOGEE DR, example dr=14
    OUTPUT:
        dr (int): APOGEE DR, example dr=14
    HISTORY:
        2017-Oct-26 - Written - Henry Leung (University of Toronto)
    """
    if dr is None:
        dr = 14
        print(f'dr is not provided, using default dr={dr}')
    else:
        pass

    return dr


def apogeeid_digit(arr):
    """
    NAME:
        apogeeid_digit
    PURPOSE:
        Extract digits from apogeeid because its too painful to deal with APOGEE ID in h5py
    INPUT:
        arr (ndarray): apogee_id
    OUTPUT:
        apogee_id with digits only (ndarray)
    HISTORY:
        2017-Oct-26 - Written - Henry Leung (University of Toronto)
    """
    import numpy as np
    if isinstance(arr, np.ndarray) or isinstance(arr, list):
        arr_copy = np.array(arr)  # make a copy
        for i in range(arr_copy.shape[0]):
            arr_copy[i] = str(''.join(filter(str.isdigit, arr_copy[i])))
        return arr_copy
    else:
        return str(''.join(filter(str.isdigit, arr)))

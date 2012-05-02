#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# mat2npz.py
#
# purpose:  Convert matlab file from TEOS-10 group to a npz file
# author:   Filipe P. A. Fernandes
# e-mail:   ocefpaf@gmail
# web:      http://ocefpaf.tiddlyspot.com/
# created:  06-Jun-2011
# modified: Wed 02 May 2012 04:29:32 PM EDT
#
# obs:
#

import numpy as np
# FIXME: To use the original matlab file I must use pytables.
import scipy.io as sio

data_ver = 'v3_0'
gsw_data = sio.loadmat('gsw_data_' + data_ver + '.mat', squeeze_me=True)

# Save compare values in a separate file.
gsw_cv = gsw_data['gsw_cv']
del gsw_data['gsw_cv']

cv_vars = {}
for name in gsw_cv.dtype.names:
    var = np.atleast_1d(gsw_cv[name])[0]
    cv_vars.update({name: var})

# Check values.
np.savez("gsw_cv_" + data_ver, **cv_vars)

# Delta SA Atlas.
ref_table = {}
for k in gsw_data:
    if '__' not in k:
        if 'deltaSA_ref' in k:
            name = 'delta_SA_ref'
        else:
            name = k

        var = np.atleast_1d(gsw_data[k])
        ref_table.update({name: var})

np.savez("gsw_data_" + data_ver, **ref_table)
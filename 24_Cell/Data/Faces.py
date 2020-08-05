import numpy as np

faces = {'aei': np.asarray([1.        , 0.33333333, 0.33333333, 0.33333333]),
         'aej': np.asarray([ 1.        ,  0.33333333,  0.33333333, -0.33333333]),
         'aem': np.asarray([ 0.66666667,  0.66666667,  0.66666667,  0.        ]),
         'afi': np.asarray([ 1.        ,  0.33333333, -0.33333333,  0.33333333]),
         'afj': np.asarray([ 1.        ,  0.33333333, -0.33333333, -0.33333333]),
         'afn': np.asarray([ 0.66666667,  0.66666667, -0.66666667,  0.        ]),
         'aiq': np.asarray([ 0.66666667,  0.66666667,  0.        ,  0.66666667]),
         'ajr': np.asarray([ 0.66666667,  0.66666667,  0.        , -0.66666667]),
         'amq': np.asarray([ 0.33333333,  1.        ,  0.33333333,  0.33333333]),
         'amr': np.asarray([ 0.33333333,  1.        ,  0.33333333, -0.33333333]),
         'anq': np.asarray([ 0.33333333,  1.        , -0.33333333,  0.33333333]),
         'anr': np.asarray([ 0.33333333,  1.        , -0.33333333, -0.33333333]),
         'bei': np.asarray([ 1.        , -0.33333333,  0.33333333,  0.33333333]),
         'bej': np.asarray([ 1.        , -0.33333333,  0.33333333, -0.33333333]),
         'beo': np.asarray([ 0.66666667, -0.66666667,  0.66666667,  0.        ]),
         'bfi': np.asarray([ 1.        , -0.33333333, -0.33333333,  0.33333333]),
         'bfj': np.asarray([ 1.        , -0.33333333, -0.33333333, -0.33333333]),
         'bfp': np.asarray([ 0.66666667, -0.66666667, -0.66666667,  0.        ]),
         'bis': np.asarray([ 0.66666667, -0.66666667,  0.        ,  0.66666667]),
         'bjt': np.asarray([ 0.66666667, -0.66666667,  0.        , -0.66666667]),
         'bos': np.asarray([ 0.33333333, -1.        ,  0.33333333,  0.33333333]),
         'bot': np.asarray([ 0.33333333, -1.        ,  0.33333333, -0.33333333]),
         'bps': np.asarray([ 0.33333333, -1.        , -0.33333333,  0.33333333]),
         'bpt': np.asarray([ 0.33333333, -1.        , -0.33333333, -0.33333333]),
         'cgk': np.asarray([-1.        ,  0.33333333,  0.33333333,  0.33333333]),
         'cgl': np.asarray([-1.        ,  0.33333333,  0.33333333, -0.33333333]),
         'cgm': np.asarray([-0.66666667,  0.66666667,  0.66666667,  0.        ]),
         'chk': np.asarray([-1.        ,  0.33333333, -0.33333333,  0.33333333]),
         'chl': np.asarray([-1.        ,  0.33333333, -0.33333333, -0.33333333]),
         'chn': np.asarray([-0.66666667,  0.66666667, -0.66666667,  0.        ]),
         'ckq': np.asarray([-0.66666667,  0.66666667,  0.        ,  0.66666667]),
         'clr': np.asarray([-0.66666667,  0.66666667,  0.        , -0.66666667]),
         'cmq': np.asarray([-0.33333333,  1.        ,  0.33333333,  0.33333333]),
         'cmr': np.asarray([-0.33333333,  1.        ,  0.33333333, -0.33333333]),
         'cnq': np.asarray([-0.33333333,  1.        , -0.33333333,  0.33333333]),
         'cnr': np.asarray([-0.33333333,  1.        , -0.33333333, -0.33333333]),
         'dgk': np.asarray([-1.        , -0.33333333,  0.33333333,  0.33333333]),
         'dgl': np.asarray([-1.        , -0.33333333,  0.33333333, -0.33333333]),
         'dgo': np.asarray([-0.66666667, -0.66666667,  0.66666667,  0.        ]),
         'dhk': np.asarray([-1.        , -0.33333333, -0.33333333,  0.33333333]),
         'dhl': np.asarray([-1.        , -0.33333333, -0.33333333, -0.33333333]),
         'dhp': np.asarray([-0.66666667, -0.66666667, -0.66666667,  0.        ]),
         'dks': np.asarray([-0.66666667, -0.66666667,  0.        ,  0.66666667]),
         'dlt': np.asarray([-0.66666667, -0.66666667,  0.        , -0.66666667]),
         'dos': np.asarray([-0.33333333, -1.        ,  0.33333333,  0.33333333]),
         'dot': np.asarray([-0.33333333, -1.        ,  0.33333333, -0.33333333]),
         'dps': np.asarray([-0.33333333, -1.        , -0.33333333,  0.33333333]),
         'dpt': np.asarray([-0.33333333, -1.        , -0.33333333, -0.33333333]),
         'eiu': np.asarray([ 0.66666667,  0.        ,  0.66666667,  0.66666667]),
         'ejv': np.asarray([ 0.66666667,  0.        ,  0.66666667, -0.66666667]),
         'emu': np.asarray([ 0.33333333,  0.33333333,  1.        ,  0.33333333]),
         'emv': np.asarray([ 0.33333333,  0.33333333,  1.        , -0.33333333]),
         'eou': np.asarray([ 0.33333333, -0.33333333,  1.        ,  0.33333333]),
         'eov': np.asarray([ 0.33333333, -0.33333333,  1.        , -0.33333333]),
         'fiw': np.asarray([ 0.66666667,  0.        , -0.66666667,  0.66666667]),
         'fjx': np.asarray([ 0.66666667,  0.        , -0.66666667, -0.66666667]),
         'fnw': np.asarray([ 0.33333333,  0.33333333, -1.        ,  0.33333333]),
         'fnx': np.asarray([ 0.33333333,  0.33333333, -1.        , -0.33333333]),
         'fpw': np.asarray([ 0.33333333, -0.33333333, -1.        ,  0.33333333]),
         'fpx': np.asarray([ 0.33333333, -0.33333333, -1.        , -0.33333333]),
         'gku': np.asarray([-0.66666667,  0.        ,  0.66666667,  0.66666667]),
         'glv': np.asarray([-0.66666667,  0.        ,  0.66666667, -0.66666667]),
         'gmu': np.asarray([-0.33333333,  0.33333333,  1.        ,  0.33333333]),
         'gmv': np.asarray([-0.33333333,  0.33333333,  1.        , -0.33333333]),
         'gou': np.asarray([-0.33333333, -0.33333333,  1.        ,  0.33333333]),
         'gov': np.asarray([-0.33333333, -0.33333333,  1.        , -0.33333333]),
         'hkw': np.asarray([-0.66666667,  0.        , -0.66666667,  0.66666667]),
         'hlx': np.asarray([-0.66666667,  0.        , -0.66666667, -0.66666667]),
         'hnw': np.asarray([-0.33333333,  0.33333333, -1.        ,  0.33333333]),
         'hnx': np.asarray([-0.33333333,  0.33333333, -1.        , -0.33333333]),
         'hpw': np.asarray([-0.33333333, -0.33333333, -1.        ,  0.33333333]),
         'hpx': np.asarray([-0.33333333, -0.33333333, -1.        , -0.33333333]),
         'iqu': np.asarray([ 0.33333333,  0.33333333,  0.33333333,  1.        ]),
         'iqw': np.asarray([ 0.33333333,  0.33333333, -0.33333333,  1.        ]),
         'isu': np.asarray([ 0.33333333, -0.33333333,  0.33333333,  1.        ]),
         'isw': np.asarray([ 0.33333333, -0.33333333, -0.33333333,  1.        ]),
         'jrv': np.asarray([ 0.33333333,  0.33333333,  0.33333333, -1.        ]),
         'jrx': np.asarray([ 0.33333333,  0.33333333, -0.33333333, -1.        ]),
         'jtv': np.asarray([ 0.33333333, -0.33333333,  0.33333333, -1.        ]),
         'jtx': np.asarray([ 0.33333333, -0.33333333, -0.33333333, -1.        ]),
         'kqu': np.asarray([-0.33333333,  0.33333333,  0.33333333,  1.        ]),
         'kqw': np.asarray([-0.33333333,  0.33333333, -0.33333333,  1.        ]),
         'ksu': np.asarray([-0.33333333, -0.33333333,  0.33333333,  1.        ]),
         'ksw': np.asarray([-0.33333333, -0.33333333, -0.33333333,  1.        ]),
         'lrv': np.asarray([-0.33333333,  0.33333333,  0.33333333, -1.        ]),
         'lrx': np.asarray([-0.33333333,  0.33333333, -0.33333333, -1.        ]),
         'ltv': np.asarray([-0.33333333, -0.33333333,  0.33333333, -1.        ]),
         'ltx': np.asarray([-0.33333333, -0.33333333, -0.33333333, -1.        ]),
         'mqu': np.asarray([ 0.        ,  0.66666667,  0.66666667,  0.66666667]),
         'mrv': np.asarray([ 0.        ,  0.66666667,  0.66666667, -0.66666667]),
         'nqw': np.asarray([ 0.        ,  0.66666667, -0.66666667,  0.66666667]),
         'nrx': np.asarray([ 0.        ,  0.66666667, -0.66666667, -0.66666667]),
         'osu': np.asarray([ 0.        , -0.66666667,  0.66666667,  0.66666667]),
         'otv': np.asarray([ 0.        , -0.66666667,  0.66666667, -0.66666667]),
         'psw': np.asarray([ 0.        , -0.66666667, -0.66666667,  0.66666667]),
         'ptx': np.asarray([ 0.        , -0.66666667, -0.66666667, -0.66666667])}
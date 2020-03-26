"""
CONFIG = defaultdict()

CONFIG['DATASET_PATH'] = './data/'
CONFIG['TEST_SIZE'] = 0.2
CONFIG['RANDOM_STATE'] = 25
CONFIG['STRAT_TYPE'] = 'TARGET'
"""

from easydict import EasyDict as edict


__C                                         = edict()
cfg                                         = __C

#
# Dataset Config
#
__C.DATASETS                               = edict()
__C.DATASETS.PATH                          = './data/'
__C.DATASETS.FILENAME                      = 'application_train.csv'
__C.DATASETS.IMPUTED_FILENAME              = 'imputed_dataframe.csv'

__C.CONST                                  = edict()
__C.CONST.IMPUTATION_ITERS                 = 50
__C.CONST.TARGET_NAME                      = 'TARGET'
__C.CONST.STRAT_TYPE                       = 'TARGET'
__C.CONST.TEST_RATIO                       = 0.2
__C.CONST.RANDOM_SEED                      = 25

import numpy as np


def collect_info(array):
    return 'Shape: {}; dimensions: {}; length: {}; size: {}'.format(
        np.shape(array),
        np.ndim(array),
        len(array),
        np.size(array)
    )

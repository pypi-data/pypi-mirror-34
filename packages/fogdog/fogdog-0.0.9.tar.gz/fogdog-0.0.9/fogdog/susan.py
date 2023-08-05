from ._susan import *


__all__ = ['read_data', 'read_row_indices', 'has_row_indices']


def read_data(path, sep='\t', dtype=float):
    """ Reads data.

    Note: All data elements are of the same data type.
    :param path: directory or single path or a list of paths
    :param sep: separator
    :param dtype: data type
    :return: iterable (each row of data)
    """
    return _read_data(path, sep, dtype)


def read_row_indices(path):
    """ Reads row indices.

    Note: row indices file has postfix '.ri' and the same file name with data file.
    :param path: data path
    :return: iterable (row indices)
    """
    return _read_row_indices(path)


def has_row_indices(path):
    """ Exams whether row index files exist.

    :param path: data path
    :return: True or False
    """
    return _has_row_indices(path)

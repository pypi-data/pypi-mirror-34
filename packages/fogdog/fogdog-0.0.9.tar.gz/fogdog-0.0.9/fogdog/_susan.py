from pathlib import Path
from .logger import *


__all__ = ['_read_data', '_read_row_indices', '_has_row_indices']


def _read_data(path, sep='\t', dtype=float):
    """ Reads data.

    Note: All data elements are of the same data type.
    :param path: directory or single path or a list of paths
    :param sep: separator
    :param dtype: data type
    :return: iterable rows
    """
    paths = _parse_data_paths(path)
    for row in _read_multi_data_files(paths, sep, dtype):
        yield row


def _parse_data_paths(path):
    """ Parses data paths from parameter: path.

    :param path: directory or single path or a list of paths
    :return: Iterable paths
    """
    if isinstance(path, list):
        paths = path
    else:
        pt = Path(path)
        if not pt.exists():
            raise FileNotFoundError("File or directory does not exist! path = '%s'" % path)
        if pt.is_dir():
            paths = _files_in_directory(pt)
        else:
            paths = [pt]
    return paths


def _files_in_directory(directory):
    return Path(directory).glob('*')


def _read_single_data_file(path, sep='\t', dtype=float):
    logger.info("Reading '%s'" % path)
    with open(path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            if line[-1] == '\n':
                line = line[0: -1]
            row = line.split(sep)
            yield [dtype(x) for x in row]


def _read_multi_data_files(paths, sep='\t', dtype=float):
    for path in paths:
        if not Path(path).exists():
            raise FileNotFoundError("File not found! path = '%s'" % path)
        for row in _read_single_data_file(path, sep, dtype):
            yield row


def _read_row_indices(path):
    """ Reads row indices.

    Note: row index file has postfix '.ri' and the same file name with data file.
    :param path: data path (directory or single path or a list of paths)
    :return: iterable (row indices)
    """
    paths = _parse_ri_paths(path)
    for row_index in _read_multi_ri_files(paths):
        yield row_index


def _parse_ri_paths(path):
    """ Parses row index file paths.

    :param path: data path (directory or single path or a list of paths)
    :return: row index file path
    """
    if isinstance(path, list):
        paths = path
    else:
        pt = _data_path_to_ri_path(path)
        if not pt.exists():
            raise FileNotFoundError("File or directory does not exist! path = '%s'" % path)
        if pt.is_dir():
            paths = [_data_path_to_ri_path(path) for path in _files_in_directory(pt)]
        else:
            paths = [pt]
    return paths


def _data_path_to_ri_path(path):
    ri_postfix = '.ri'
    p = Path(path)
    return p if p.is_dir() else p.with_name(p.stem + ri_postfix)


def _read_single_ri_file(path):
    logger.info("Reading '%s'" % path)
    with open(path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            yield line[0: -1] if line[-1] == '\n' else line


def _read_multi_ri_files(paths):
    for path in paths:
        if not Path(path).exists():
            raise FileNotFoundError("File not found! path = '%s'" % path)
        for row_index in _read_single_ri_file(path):
            yield row_index


def _has_row_indices(path):
    paths_ri = _parse_ri_paths(path)
    paths_data = _parse_data_paths(path)
    i = 0
    for path in paths_ri:
        i += 1
    if i == 0:
        return False
    for path in paths_data:
        i -= 1
    if i != 0:
        return False
    return True




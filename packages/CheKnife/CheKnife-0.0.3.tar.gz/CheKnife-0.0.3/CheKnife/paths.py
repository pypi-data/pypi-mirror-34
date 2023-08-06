import os
from CheKnife.errors import ParameterError


def mktree(abs_path):
    if not abs_path:
        raise ParameterError("No valid path suplied to mktree: {}".format(abs_path))
    if not os.path.isdir(abs_path):
        try:
            os.makedirs(abs_path, exist_ok=True)

        except IOError:
            raise PermissionError('Error creating directory: {} Check user permissions'.format(abs_path))
    return True

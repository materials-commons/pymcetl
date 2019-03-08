import os
from .access_exceptions import GlobusSetupException


class McdirHelper:

    def get_upload_dir(self):
        return self._get_base_dir('__upload_staging')

    def get_download_dir(self):
        return self._get_base_dir('__download_staging')

    def base_dir(self):
        return self._get_base_dir(None)

    def get_excel_file_link_dir(self):
        return self._get_base_dir('__excel_file_staging')

    @staticmethod
    def _get_base_dir(child):
        mcdir = os.environ.get('MCDIR')
        if not mcdir:
            raise GlobusSetupException("$MCDIR is None - must be defined")
        base_path = mcdir.split(':')[0]
        if not os.path.exists(base_path):
            raise GlobusSetupException(
                "the $MCDIR base path = {} - does not exist".format(base_path))
        if child:
            child_dir = os.path.join(base_path, child)
            if not os.path.exists(child_dir):
                os.mkdir(child_dir)
            return child_dir
        else:
            return base_path

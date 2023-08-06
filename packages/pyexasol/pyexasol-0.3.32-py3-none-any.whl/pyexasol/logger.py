import sys
import datetime
import pathlib

from . import constant
from .exceptions import ExaRuntimeError


class ExaLogger(object):
    def __init__(self, connection, log_target):
        self.connection = connection
        self.log_target = log_target

        if log_target is None:
            self.fd = None
        elif log_target == 'stderr':
            self.fd = sys.stderr
        elif isinstance(log_target, pathlib.Path):
            if not log_target.is_dir():
                raise ExaRuntimeError(self.connection, 'Not a directory: ' + str(log_target))

            self.fd = open(log_target / self._get_log_filename(), 'w', encoding='utf-8')

        else:
            raise ExaRuntimeError(self.connection, 'Invalid log_target')

    def __del__(self):
        if isinstance(self.log_target, pathlib.Path):
            self.fd.close()

    def log_json(self, message, data):
        if self.fd is None:
            return

        json_str = self.connection._json_encode(data, indent=4)

        if len(json_str) > constant.LOGGER_MAX_JSON_LENGTH:
            json_str = f'{json_str[0:constant.LOGGER_MAX_JSON_LENGTH]}\n------ TRUNCATED TOO LONG MESSAGE ------\n'

        self._write_log(f'[{message}]\n{json_str}')

    def log_message(self, message):
        self._write_log(f'{message}')

    def _write_log(self, message):
        if self.fd is None:
            return

        self.fd.write(f'{self._get_ts()} {message}\n')
        self.fd.flush()

    def _get_ts(self):
        return datetime.datetime.now().strftime(constant.LOGGER_MESSAGE_TIMESTAMP_FORMAT)

    def _get_log_filename(self):
        return datetime.datetime.now().strftime(constant.LOGGER_FILENAME_TIMESTAMP_FORMAT) + '.log'

import os

LC_PATH = os.environ.get('DLVM_CONF', '/etc/dlvm')
DEFAULT_CFG_FILE = 'default.cfg'
DLVM_CFG_FILE = 'dlvm.cfg'
# https://docs.python.org/3.6/library/logging.config.html
LOGGER_CFG_FILE = 'logger.json'
# http://docs.sqlalchemy.org/en/latest/core/engines.html
CELERY_CFG_FILE = 'celery.json'
# http://docs.celeryproject.org/en/latest/userguide/configuration.html
SQLALCHEMY_CFG_FILE = 'sqlalchemy.json'

DEFAULT_MONITOR_CFG = 'default_monitor.cfg'
MONITOR_CFG_FILE = 'monitor.cfg'

CELERY_APP_NAME = 'dlvm_celery_app'

RES_NAME_REGEX = r'[a-z,A-Z][a-z,A-Z,_]*'
RES_NAME_LENGTH = 32
DNS_NAME_LENGTH = 64
ID_LENGTH = 32

DEFAULT_SNAP_NAME = 'base'

MAX_GROUP_SIZE = 1024*1024*1024*1024
MIN_THIN_BLOCK_SIZE = 64*1024
MAX_BM_SIZE = MAX_GROUP_SIZE // MIN_THIN_BLOCK_SIZE
MAX_THIN_MAPPING = 100*1024*1024

API_LOGGER_NAME = 'dlvm.api'
DPV_LOGGER_NAME = 'dlvm.dpv'
IHOST_LOGGER_NAME = 'dlvm.ihost'
SM_LOGGER_NAME = 'dlvm.sm'
MONITOR_LOGGER_NAME = 'dlvm.monitor'

LOCK_HANDLER_NAME = 'lock_handler'
DPV_HANDLER_NAME = 'dpv_handler'

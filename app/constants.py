from os import getenv

DB_USER = getenv('POSTGRES_USER', None)
DB_PASS = getenv('POSTGRES_PASSWORD', None)
DB_NAME = getenv('DB_NAME', None)
DB_HOST = getenv('DB_HOST', None)
DB_PORT = getenv('DB_PORT', None)
DEFAULT_DB_NAME = 'default_db'

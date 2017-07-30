from base import *
import dj_database_url

DEBUG = False


DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}

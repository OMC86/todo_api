from base import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['todo-api-institute.herokuapp.com']

DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}

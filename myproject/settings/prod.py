from .base import *

ALLOWED_HOSTS = ['13.124.50.40', 'woongb.shop']

STATIC_ROOT = BASE_DIR / 'static/'

STATICFILES_DIRS = []

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'manager',
        'USER': 'dbmasteruser',
        'PASSWORD': 'xkfo77zlem!',
        'HOST': 'ls-8a726661033a3582de9b6a685720b04a5d7ce49d.ckyvgwwgkg6k.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}
import os
from pathlib import Path
from datetime import timedelta
from django.utils.log import DEFAULT_LOGGING


BASE_DIR = Path(__file__).resolve().parent.parent


########################################################################
# GENERAL
########################################################################

SECRET_KEY = os.environ.get('SECRET_KEY')
assert SECRET_KEY, 'Define SECRET_KEY'

DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS')
assert ALLOWED_HOSTS, 'Define ALLOWED_HOSTS'
ALLOWED_HOSTS = ALLOWED_HOSTS.split(',')


# ADMIN PANEL

ADMIN_PANEL = os.getenv('ADMIN_PANEL', 'True').lower() in ('true', '1', 't')


# CORS

_CORS_ALLOWED_ORIGINS = os.environ.get('CORS_ALLOWED_ORIGINS')
assert _CORS_ALLOWED_ORIGINS, 'Define CORS_ALLOWED_ORIGINS'

if _CORS_ALLOWED_ORIGINS == '*':
    CORS_ALLOW_ALL_ORIGINS = True
else:
    CORS_ALLOWED_ORIGINS = _CORS_ALLOWED_ORIGINS.split(',')


# CSRF

_CSRF_TRUSTED_ORIGINS = os.environ.get('CSRF_TRUSTED_ORIGINS')
assert _CSRF_TRUSTED_ORIGINS, 'Define CSRF_TRUSTED_ORIGINS'

if _CSRF_TRUSTED_ORIGINS == '*':
    CSRF_TRUSTED_ORIGINS = ['http://*', 'https://*']
else:
    CSRF_TRUSTED_ORIGINS = _CSRF_TRUSTED_ORIGINS.split(',')


########################################################################
# APPLICATION DEFINITION
########################################################################

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_yasg',
    'corsheaders',
    'rest_framework',
    'knox',
    'import_export',
    'channels',
    'django_user_agents',
    'django_minio_backend',
    'builder',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
]

ROOT_URLCONF = 'djangoapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangoapp.wsgi.application'


ASGI_APPLICATION = 'djangoapp.asgi.application'


###################################################
# DATABASE
###################################################

DB_HOST = os.environ.get('DB_HOST')
assert DB_HOST, 'Define DB_HOST'

DB_PORT = os.environ.get('DB_PORT')
assert DB_PORT, 'Define DB_PORT'

DB_DB = os.environ.get('DB_DB')
assert DB_DB, 'Define DB_DB'

DB_USER = os.environ.get('DB_USER')
assert DB_USER, 'Define DB_USER'

DB_PASSWORD = os.environ.get('DB_PASSWORD')
assert DB_PASSWORD, 'Define DB_PASSWORD'

DB_SSL = os.getenv('DB_SSL', 'False').lower() in ('true', '1', 't')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('DB_HOST', 'database'),
        'PORT': os.environ.get('DB_PORT', '5432'),
        'NAME': os.environ.get('DB_DB', 'app_db'),
        'USER': os.environ.get('DB_USER', 'app_db'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'OPTIONS': {},
    }
}

if DB_SSL:
    DATABASES['default']['OPTIONS']['sslmode'] = 'require'


###################################################
# REDIS
###################################################

REDIS_URL = os.environ.get('REDIS_URL')


###################################################
# Password validation
###################################################

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


###################################################
# Internationalization
###################################################

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


###################################################
# Default primary key field type
###################################################

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


###################################################
# REST framework
###################################################

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case.parser.CamelCaseFormParser',
        'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
    ),
}

if DEBUG:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] += (
        'djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer',)

###################################################
# FILE UPLOAD (MINIO, STATIC, MEDIA)
###################################################

MINIO_ENDPOINT = os.environ['MINIO_ENDPOINT']
MINIO_EXTERNAL_ENDPOINT = os.environ.get(
    'MINIO_EXTERNAL_ENDPOINT', MINIO_ENDPOINT)

MINIO_ACCESS_KEY = os.environ.get('MINIO_ACCESS_KEY', '')
MINIO_SECRET_KEY = os.environ.get('MINIO_SECRET_KEY', '')
MINIO_USE_HTTPS = os.getenv(
    'MINIO_USE_HTTPS', 'True').lower() in ('true', '1', 't')
MINIO_EXTERNAL_ENDPOINT_USE_HTTPS = os.getenv(
    'MINIO_EXTERNAL_ENDPOINT_USE_HTTPS', str(MINIO_USE_HTTPS)).lower() in ('true', '1', 't')
MINIO_URL_EXPIRY_HOURS = timedelta(hours=2)

MINIO_MEDIA_FILES_BUCKET = 'media-files-bucket'
MINIO_STATIC_FILES_BUCKET = 'static-files-bucket'
MINIO_PRIVATE_BUCKETS = [
    MINIO_MEDIA_FILES_BUCKET,
]
MINIO_PUBLIC_BUCKETS = [
    MINIO_STATIC_FILES_BUCKET,
]

DEFAULT_FILE_STORAGE = 'django_minio_backend.models.MinioBackend'
STATICFILES_STORAGE = 'django_minio_backend.models.MinioBackendStatic'

# To use filesystem storage instead of minio
# STATIC_URL = 'static/'
# STATIC_ROOT = '/data/static/'
# MEDIA_URL = 'media/'
# MEDIA_ROOT = '/data/media/'


###################################################
# REVERSE PROXY
###################################################

USE_X_FORWARDED_HOST = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


###################################################
# EMAIL
###################################################

EMAIL_HOST = os.environ.get('EMAIL_HOST', None)
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', None)
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', None)
EMAIL_PORT = os.environ.get('EMAIL_PORT', None)
EMAIL_USE_TLS = os.getenv(
    'EMAIL_USE_TLS', 'False').lower() in ('true', '1', 't')
EMAIL_USE_SSL = os.getenv(
    'EMAIL_USE_SSL', 'False').lower() in ('true', '1', 't')
EMAIL_SENDER = os.getenv('EMAIL_SENDER', '')

if EMAIL_HOST:
    assert EMAIL_HOST_PASSWORD, 'Define EMAIL_HOST_PASSWORD'
    assert EMAIL_HOST_USER, 'Define EMAIL_HOST_USER'
    assert EMAIL_PORT, 'Define EMAIL_PORT'
    assert EMAIL_SENDER != '', 'Define EMAIL_SENDER'


###################################################
# LOGGING
###################################################

LOGGING_CONFIG = None
LOGLEVEL = os.getenv('DJ_LOGLEVEL', 'info').upper()
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        # Use JSON formatter as default
        'default': {
            '()': 'pythonjsonlogger.jsonlogger.JsonFormatter',
        },
        'django.server': DEFAULT_LOGGING['formatters']['django.server'],
    },
    'handlers': {
        # Route console logs to stdout
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'django.server': DEFAULT_LOGGING['handlers']['django.server'],
    },
    'loggers': {
        # Default logger for all modules
        '': {
            'level': LOGLEVEL,
            'handlers': ['console', ],
        },
        # Default runserver request logging
        'django.server': DEFAULT_LOGGING['loggers']['django.server'],
    }
}

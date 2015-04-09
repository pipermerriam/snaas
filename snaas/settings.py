import os
import excavator
import dj_database_url
import django_cache_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = excavator.env_string('DJANGO_SECRET_KEY', required=True)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = excavator.env_bool('DJANGO_DEBUG', default=True)

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = excavator.env_list('DJANGO_ALLOWED_HOSTS', required=not DEBUG)


# Application definition

INSTALLED_APPS = (
    # django
    'django.contrib.staticfiles',
    # local project
    'snaas.apps.core',
    # django 3rd party
    'pipeline',
    'manifesto',
)

MIDDLEWARE_CLASSES = []

ROOT_URLCONF = 'snaas.urls'

WSGI_APPLICATION = 'snaas.wsgi.application'

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.parse(excavator.env_string('DATABASE_URL', required=True)),
}
DATABASES['default'].setdefault('ATOMIC_REQUESTS', True)

# Cache
CACHES = {
    'default': django_cache_url.config(),
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'MST'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static Files
STATIC_URL = excavator.env_string('DJANGO_STATIC_URL', default='/static/')
STATIC_ROOT = excavator.env_string(
    'DJANGO_STATIC_ROOT',
    default=os.path.join(BASE_DIR, 'snaas', 'public', 'static'),
)

MEDIA_URL = excavator.env_string('DJANGO_MEDIA_URL', default='/media/')
MEDIA_ROOT = excavator.env_string(
    'DJANGO_MEDIA_ROOT',
    default=os.path.join(BASE_DIR, 'snaas', 'public', 'media'),
)

DEFAULT_FILE_STORAGE = excavator.env_string(
    "DJANGO_DEFAULT_FILE_STORAGE",
    default="django.core.files.storage.FileSystemStorage",
)
STATICFILES_STORAGE = excavator.env_string(
    "DJANGO_STATICFILES_STORAGE",
    default="django.contrib.staticfiles.storage.StaticFilesStorage"
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'snaas', 'static'),
)

# Email Settings
EMAIL_BACKEND = excavator.env_string(
    'DJANGO_EMAIL_BACKEND',
    default='django.core.mail.backends.smtp.EmailBackend',
)
EMAIL_HOST = excavator.env_string('EMAIL_HOST', default='localhost')
EMAIL_HOST_USER = excavator.env_string('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = excavator.env_string('EMAIL_HOST_PASSWORD', default='')
EMAIL_PORT = excavator.env_string('EMAIL_PORT', default='25')
EMAIL_USE_TLS = excavator.env_bool('EMAIL_USE_TLS')
EMAIL_USE_SSL = excavator.env_bool('EMAIL_USE_SSL')

# `django.contrib.sites` settings
SITE_ID = 1

# Sentry
RAVEN_CONFIG = {
    'dsn': excavator.env_string('SENTRY_DSN', default=None),
}

# Herokuify
SECURE_PROXY_SSL_HEADER = excavator.env_list('SECURE_PROXY_SSL_HEADER', default='') or None

# AWS
AWS_ACCESS_KEY_ID = excavator.env_string('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = excavator.env_string('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = excavator.env_string('AWS_STORAGE_BUCKET_NAME')

DEFAULT_S3_PATH = "media"
STATIC_S3_PATH = "static"

# Sorl Thumbnailer
THUMBNAIL_DEFAULT_STORAGE = DEFAULT_FILE_STORAGE
THUMBNAIL_FORMAT = 'PNG'

AWS_REDUCED_REDUNDANCY = True
AWS_QUERYSTRING_AUTH = False
AWS_S3_FILE_OVERWRITE = True
AWS_S3_SECURE_URLS = True
AWS_IS_GZIPPED = False
AWS_PRELOAD_METADATA = True
AWS_HEADERS = {
    "Cache-Control": "public, max-age=86400",
}

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'snaas', 'templates'),
)

# Django Pipeline Settings
PIPELINE_DISABLE_WRAPPER = excavator.env_bool(
    'DJANGO_PIPELINE_DISABLE_WRAPPER', default=True,
)
PIPELINE_ENABLED = excavator.env_bool('DJANGO_PIPELINE_ENABLED', not DEBUG)
PIPELINE_CSS = {
    'base': {
        'source_filenames': (
            "css/bootstrap.css",
            "css/landing-page.css",
            "font-awesome/css/font-awesome.css",
            "css/project.css",
        ),
        'output_filename': 'css/base.css',
    },
    'highlight': {
        'source_filenames': (
            "css/zenburn.css",
        ),
        'output_filename': 'css/zenburn.css',
    },
}

PIPELINE_JS = {
    'base': {
        'source_filenames': (
            "js/jquery.js",
            "js/bootstrap.js",
            "js/project.js",
        ),
        'output_filename': 'js/base.js',
    },
    'highlight': {
        'source_filenames': (
            "js/highlight.pack.js",
        ),
        'output_filename': 'js/highlight.js',
    },
}
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'

if DEBUG:
    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )
else:
    # Cached template loading is bad for dev so keep it off when debug is on.
    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )),
    )

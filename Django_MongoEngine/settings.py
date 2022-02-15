"""
Django settings for Django_MongoEngine project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#^+xn2x910e9h5$q=uye1(=o_g=)(*3_bitdw+pkt__(29l$=$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',

	'project',

	'rest_framework',
	'rest_framework_mongoengine',

]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Django_MongoEngine.urls'

TEMPLATES = [
    {
			'BACKEND': 'django.template.backends.django.DjangoTemplates',
			'DIRS': [],
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

WSGI_APPLICATION = 'Django_MongoEngine.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
import mongoengine
# mongodb+srv://djangomongo:<password>@djangomongo.v3py4.mongodb.net/test
mongoengine.connect(db='linkedcamp-dev-new', host='mongodb+srv://mobylogix:mobylogix123@cluster0.rppvu.mongodb.net')
# DATABASES = {
#      'default': {
#          'ENGINE': 'django.db.backends.dummy',
#      },
# }
# DATABASES = {
#    'default' : {
#       'ENGINE' : 'django_mongodb_engine',
#       'NAME' : 'my_database'
#    }
# }

# MONGODB_DATABASES = {
#     "default": {
#         "db" : 'admin',
#         "host": 'Atlas',
#         "password": 'djangomongo',
#         "username": 'djangomongo',
#         "tz_aware": True, # if you using timezones in django (USE_TZ = True)
#     },
# }

# DATABASES = {
#      'default': {
#          'ENGINE': 'django.db.backends.dummy',
#      },
# }

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

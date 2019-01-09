"""
Django settings for decide project.
Generated by 'django-admin startproject' using Django 2.0.
For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
# Definimos el procesador de contexto para i18n

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOCALE_PATHS = (
 os.path.join(BASE_DIR, "locale"),
)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^##ydkswfu0+=ofw0l#$kv^8n)0$i(qd&d&ol#p9!b$8*5%j1+'

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
    'social_django',
    'nocaptcha_recaptcha',

    'corsheaders',
    'django_filters',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    )
}

AUTHENTICATION_BACKENDS = [
    'social_core.backends.open_id.OpenIdAuth',  # for Google authentication
    'social_core.backends.google.GoogleOpenId',  # for Google authentication
    'social_core.backends.google.GoogleOAuth2',  # for Google authentication
    'social_core.backends.github.GithubOAuth2',  # for Github authentication
    'social_core.backends.facebook.FacebookOAuth2',  # for Facebook authentication
    'base.backends.AuthBackend',
]

MODULES = [
    'authentication',
    'base',
    'booth',
    'census',
    'mixnet',
    'postproc',
    'store',
    'visualizer',
    'voting',
]

BASEURL = 'http://localhost:8000'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'decide.urls'

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'authentication.User'

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGES = (
    ('en-us', 'English'),
    ('es', 'Español'),
    ('ca', 'Català'),
)

LANGUAGE_CODE = 'en-us'
_ = lambda s: s



TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

# number of bits for the key, all auths should use the same number of bits
KEYBITS = 256

if 'TRAVIS' in os.environ:
    try:
        from local_settings_travis import *
    except ImportError:
        print("local_settings_travis.py not found")
elif 'HEROKU' in os.environ:
    try:
        from local_settings_heroku import *

        BASEURL = 'https://'+os.environ['REPO_NAME']+'.herokuapp.com/'

        #Heroku (Esta configuración debe ir aquí)
        import django_heroku
        django_heroku.settings(locals())
    except ImportError:
        print("local_settings_heroku.py not found")
else:
    try:
        from local_settings import *
    except ImportError:
        print("local_settings.example.py not found")


INSTALLED_APPS = INSTALLED_APPS + MODULES

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'decideganimedes@gmail.com'
EMAIL_HOST_PASSWORD = 'decide18-19'
EMAIL_PORT = 587

LOGIN_REDIRECT_URL = '/authentication/obtain_auth_token_rrss/'
LOGIN_URL = '/auth/login/google-oauth2/'

LOGOUT_REDIRECT_URL = '/'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY ='1016450567923-d0li25hpefseismg55uns76k7p38ou2s.apps.googleusercontent.com'  #CLient Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'cuYcihCQQootUwo8dsQ2FToo' #Secret Key

SOCIAL_AUTH_GITHUB_KEY = '5374f0f3acee01f795f6' #Client ID
SOCIAL_AUTH_GITHUB_SECRET = '057e80e49258b60a09acf76c2ff49fed36fa37b3' #Secret Key

SOCIAL_AUTH_FACEBOOK_KEY = '352361078682587'
SOCIAL_AUTH_FACEBOOK_SECRET = '993e12902a4eda5bcb2b51cbfc021593'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'locale': 'es_ES',
  'fields': 'id, name, email, age_range'
}
NORECAPTCHA_SITE_KEY = '6LdhDYgUAAAAAEiExWkWXgbOsFbb74QoFdDJzcqm'
NORECAPTCHA_SECRET_KEY = '6LdhDYgUAAAAAFc61sKda-9zzxhDnmpzgwE1PoS8'
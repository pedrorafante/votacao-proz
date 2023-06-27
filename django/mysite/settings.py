import os
from pathlib import Path

import info


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-rc^*w^w&6g9_(uvx#6s*bnt!w)l0rdi%!l7mv#y%uc&x%wo5pk'

# SECURITY WARNING: don't run with debug turned on in production!
<<<<<<< HEAD
DEBUG = True 
=======
DEBUG = True
>>>>>>> 472e17593db4b5c461118f0c589efc0fe0489f69

ALLOWED_HOSTS = ["*"]

# FORM SUBMISSION
<<<<<<< HEAD

# Comment out the following line and place your railway URL, and your production URL in the array.
CSRF_TRUSTED_ORIGINS = ["https://votacaoproz.up.railway.app"]
=======
# Comment out the following line and place your railway URL, and your production URL in the array.
# CSRF_TRUSTED_ORIGINS = ["*"]
>>>>>>> 472e17593db4b5c461118f0c589efc0fe0489f69

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
<<<<<<< HEAD
    'votacao_app',
    


=======
>>>>>>> 472e17593db4b5c461118f0c589efc0fe0489f69
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
<<<<<<< HEAD
    
=======
>>>>>>> 472e17593db4b5c461118f0c589efc0fe0489f69
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'mysite/templates')],
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

<<<<<<< HEAD
DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage' #o que salvar
DBBACKUP_STORAGE_OPTIONS = {'location': 'backups/'} # onde salvar
# pip install django-dbbackup
#python manage.py dbbackup  

=======
>>>>>>> 472e17593db4b5c461118f0c589efc0fe0489f69
WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'railway',
    'USER': 'root',
    'PASSWORD': 'U64HzXAeJ3EsPe5bfaWl',
    'HOST': 'containers-us-west-131.railway.app',
    'PORT': '8016',
    }}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'railway',
#         'USER': 'root',
#         'PASSWORD': 'U64HzXAeJ3EsPe5bfaWl',
#         'HOST': 'containers-us-west-131.railway.app',
#         'PORT': 8016,
#     }
# }


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

LOGIN_REDIRECT_URL = '/'


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

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR.joinpath('staticfiles')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

<<<<<<< HEAD
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
=======
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
>>>>>>> 472e17593db4b5c461118f0c589efc0fe0489f69
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = info.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = info.EMAIL_HOST_PASSWORD



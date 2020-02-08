from .base import *

SECRET_KEY = config('SECRET_KEY')
DEBUG = True
ALLOWED_HOSTS = [config('HOST_NAME'), '*']

################################
##      WSGI CONFIGURATION    ##
################################

WSGI_APPLICATION = 'djpocket.wsgi.application'

################################
##    DATABASE CONFIGURATION  ##
################################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

################################
##      AUTH CONFIGURATION    ##
################################

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
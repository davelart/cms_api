import environ
import os
from pathlib import Path
from django.urls import reverse_lazy

env = environ.Env()
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(&be07+0ri=pnofi#y4*dqo&zc-#rh)wddc8qvfmtgl&pvy!pe'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

CUSTOM_APPS = [
    'accounts',
    'administration',
    'attendance',
    'branches',
    'churchprofile',
    'dashboard',
    'finance',
    'guests',
    'index',
    'main',
    'members',
    'notifier',
    'reports',
    'techpanel',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'django_filters',
    'drf_spectacular',
    'drf_spectacular_sidecar',
    'rest_framework_simplejwt',
]

INSTALLED_APPS += CUSTOM_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema'
}

SPECTACULAR_SETTINGS = {
    'TITLE': None,
    'DESCRIPTION': 'churchaffairs_doc_description',
    # 'EXTENSIONS_INFO': {
    #     "x-logo": {
    #         "url": "https://churchaffairs.com/static/images/toplogo_white.png",
    #         "backgroundColor": "#"
    #     }
    # },
    'TOS': None,
    'CONTACT': None,
    'LICENCE': None,
    'VERSION': None,
    'SERVE_AUTHENTICATION': None,
    'SERVE_INCLUDE_SCHEMA': True,
    'PREPROCESSING_HOOKS': ["api.hooks.remove_apis_from_list"],
    'EXCLUDE_PATH': [reverse_lazy("schema")],
    'TAGS': [
        {'name':'Churchs'}, 
        {'name':'Accounts'}, 
        {'name':'Sign In'}, 
        {'name':'Sign Up'}, 
        {'name':'Reset Password'}, 
        {'name':'Reset Password Confirm'},
        {'name': 'Church Group'},
        {'name': 'Choice'},
        {'name': 'Attendance Program'},
        {'name': 'Attendance'},
        {'name': 'Branches'},
        {'name': 'Branch Users'},
        {'name': 'Register'},
        {'name': 'Profile'},
        {'name': 'Account Setup'},
        {'name': 'Account Payment'},
        {'name': 'Account Expenditure'},
        {'name': 'Guest'},
        {'name': 'Testimony'},
        {'name': 'Feature'},
        {'name': 'Email Subscription'},
        {'name': 'Member'},
        {'name': 'Notifier Setting'},
        {'name': 'Sent Sms'},
        {'name': 'Sent Email'},
        {'name': 'Sent Push'},
        {'name': 'Telephones'},
        {'name': 'Branch Report'},
        {'name': 'Advanced User'},
        {'name': 'Sales User Account'},
        {'name': 'Sales'},
        {'name': 'Tech Chat Ticket'},
        {'name': 'Tech Chat'},
    ],
    'EXTENSIONS_ROOT': {
        'x-tagGroups': [
            {'name': 'Accounts', 'tags': ['Churchs', 'Accounts', 'Sign In', 'Sign Up', 'Reset Password', 'Reset Password Confirm']},
            {'name': 'Administration', 'tags': ['Church Group', 'Choice']},
            {'name': 'Attendance', 'tags': ['Attendance Program', 'Attendance']},
            {'name': 'Branches', 'tags': ['Branch', 'Branch User']},
            {'name': 'Church Profile', 'tags': ['Register', 'Profile']},
            {'name': 'Finance', 'tags': ['Account Setup', 'Account Payment', 'Account Expenditure']},
            {'name': 'Guests', 'tags': ['Guest']},
            {'name': 'Index', 'tags': ['Testimony', 'Feature', 'Email Subscription']},
            {'name': 'Members', 'tags': ['Member']},
            {'name': 'Notifier', 'tags': ['Notifier Setting', 'Sent Sms', 'Sent Emails', 'Sent Push', 'Telephony']},
            {'name': 'Reports', 'tags': ['Branch Report']},
            {'name': 'Tech Panels', 'tags': ['Advanced User', 'Sales User Account', 'Sales', 'Tech Chat Ticket', 'Tech Chat']},
        ]
    },
    'REDOC_UI_SETTINGS': {
        'deepLinking': True,
        'hideDownLoadButton': True,
        'hideSchemaTitles': True,
        'theme': {
            'typography': {
                'headings': {}
            },
            'logo': {}
        }
    },
    'SWAGGER_UI_DIST': 'SIDECAR',
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
}

REDOC_SETTINGS = {
    'HIDE_DOWNLOAD_BUTTON': True
}

REST_USE_JWT = True

ROOT_URLCONF = 'api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'drf_spectacular.context.spectacular_context',
                # 'accounts.context_processors.church_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'api.wsgi.app'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = { 
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': 5432,
        'OPTIONS': {
            'sslmode': 'require'
        },
    },
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT =  os.path.join(BASE_DIR, "static")
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
from pathlib import Path
from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


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
        {'name': 'Church Groups'},
        {'name': 'Choices'},
        {'name': 'Attendance Programs'},
        {'name': 'Attendances'},
        {'name': 'Branches'},
        {'name': 'Branch Users'},
        {'name': 'Registers'},
        {'name': 'Church Profiles'},
        {'name': 'Account Setups'},
        {'name': 'Account Payments'},
        {'name': 'Account Expenditures'},
        {'name': 'Guests'},
        {'name': 'Testimonies'},
        {'name': 'Features'},
        {'name': 'Email Subscriptions'},
        {'name': 'Members'},
        {'name': 'Notifier Settings'},
        {'name': 'Sent Sms'},
        {'name': 'Sent Emails'},
        {'name': 'Sent Pushes'},
        {'name': 'Telephones'},
        {'name': 'Branch Reports'},
        {'name': 'Advanced Users'},
        {'name': 'Sales User Accounts'},
        {'name': 'Sales'},
        {'name': 'Tech Chat Tickets'},
        {'name': 'Tech Chats'},
    ],
    'EXTENSIONS_ROOT': {
        'x-tagGroups': [
            {'name': 'Administration', 'tags': ['Church Groups', 'Choices']},
            {'name': 'Attendance', 'tags': ['Attendance Programs', 'Attendances']},
            {'name': 'Branches', 'tags': ['Branches', 'Branch Users']},
            {'name': 'Church Profile', 'tags': ['Registers', 'Church Profiles']},
            {'name': 'Finance', 'tags': ['Account Setups', 'Account Payments', 'Account Expenditures']},
            {'name': 'Guests', 'tags': ['Guests']},
            {'name': 'Index', 'tags': ['Testimonies', 'Features', 'Email Subscriptions']},
            {'name': 'Members', 'tags': ['Members']},
            {'name': 'Notifier', 'tags': ['Notifier Settings', 'Sent Sms', 'Sent Emails', 'Sent Pushes', 'Telephones']},
            {'name': 'Reports', 'tags': ['Branch Reports']},
            {'name': 'Tech Panels', 'tags': ['Advanced Users', 'Sales User Accounts', 'Sales', 'Tech Chat Tickets', 'Tech Chats']},
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
        'NAME': 'postgres',
        'USER': 'postgres.blqkoylsoxzfnfmvuwaf',
        'PASSWORD': 'onlyGodcanstopme',
        'HOST': 'aws-0-us-east-1.pooler.supabase.com',
        'PORT': 6543,
        'OPTIONS': {
            # 'sslmode': 'verify-full'
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

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

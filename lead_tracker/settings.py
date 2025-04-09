import os
from pathlib import Path
from corsheaders.defaults import default_headers


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # For collectstatic on deploy
STATICFILES_DIRS = [
   os.path.join(BASE_DIR, 'api/templates')  # Where your form_tracker.js lives
]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8!tjn&iuvt(my0eil5*u_fiqc@!dgktse%f781-ve9nfkwry2n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Set to False for production (after testing)

ALLOWED_HOSTS = [
    'leadtracker-production.up.railway.app', 
    '127.0.0.1', 
    'localhost'
]

# CSRF fix for external domains (WordPress, GitHub Pages, etc.)
CSRF_TRUSTED_ORIGINS = [
    'https://leadtracker-production.up.railway.app',
    'https://aditya-05-alt.github.io',
]

# Application definition
INSTALLED_APPS = [  
    'admin_interface',  # MUST be before 'django.contrib.admin'
    'colorfield',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "https://themcostudio.com","https://www.brandmirchi.com"
]

CORS_ALLOW_CREDENTIALS = True

# Optional: allow all headers for frontend testing
CORS_ALLOW_HEADERS = list(default_headers) + [
    'X-CSRFToken',
]

ROOT_URLCONF = 'lead_tracker.urls'

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

WSGI_APPLICATION = 'lead_tracker.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'Rocmob',
#         'USER': 'root',
#         'PASSWORD': '',
#         'HOST': 'localhost',  # or '127.0.0.1'
#         'PORT': '3306',
#     }
# }

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Default auto field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

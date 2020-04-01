"""
Django settings for pyjobs project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

import dj_database_url
from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django_extensions",
    "pyjobs.core",
    "pyjobs.api",
    "pyjobs.partners",
    "pyjobs.marketing",
    "widget_tweaks",
    "django_select2",
    "django.contrib.sitemaps",
    "raven.contrib.django.raven_compat",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = "pyjobs.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "pyjobs.core.context_processors.global_vars",
            ]
        },
    }
]

WSGI_APPLICATION = "pyjobs.wsgi.application"


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.config(default="sqlite:///%s/db.sqlite3" % (BASE_DIR))
}


THUMBNAILS_BASE_FOLDER = "%s/pyjobs/core/thumb/" % (BASE_DIR)

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")
STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, "staticfiles"),)

RAVEN_CONFIG = {"dsn": config("SENTRY_DSN", default=None)}

LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "/login"

EMAIL_BACKEND = config(
    "EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)

SENDGRID_API_KEY = config("SENDGRID_API_KEY", default=None)

GA_CODE = config("GA_CODE", default="")

# MailChimp

MAILCHIMP_API_KEY = config("MAILCHIMP_API_KEY", default=None)
MAILCHIMP_USERNAME = config("MAILCHIMP_USERNAME", default=None)
MAILCHIMP_LIST_KEY = config("MAILCHIMP_LIST_KEY", default=None)


# Telegram

TELEGRAM_TOKEN = config("TELEGRAM_TOKEN", default=None)
TELEGRAM_CHATID = config("TELEGRAM_CHATID", default=None)


# Recaptcha

RECAPTCHA_SECRET_KEY = config("RECAPTCHA_SECRET_KEY", default=None)

# Force SSL

if "DYNO" in os.environ:  # pragma: no cover
    SECURE_SSL_REDIRECT = config("SECURE_SSL_REDIRECT", default=False)
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Website configurations to enable alternative deployments (to be deprecated)
# TODO: Create a configuration model that works

WEBSITE_NAME = config("WEBSITE_NAME", default=None)
WEBSITE_SLOGAN = config("WEBSITE_SLOGAN", default=None)
WEBSITE_OWNER_EMAIL = config("WEBSITE_OWNER_EMAIL", default=None)
WEBSITE_GENERAL_EMAIL = config("WEBSITE_GENERAL_EMAIL", default=None)
WEBSITE_WORKING_LANGUAGE = config("WEBSITE_WORKING_LANGUAGE", default=None)
WEBSITE_MAILINGLIST_LINK = config("WEBSITE_MAILINGLIST_LINK", default=None)
WEBSITE_OWNER_NAME = config("WEBSITE_OWNER_NAME", default=None)
USER_SUBSTANTIVE = config("USER_SUBSTANTIVE", default=None)
WEBSITE_HOME_URL = config("WEBSITE_HOME_URL", default=None)
MAILERLITE_API_KEY = config("MAILERLITE_API_KEY", default=None)

STATE_CHOICES = [
    (0, "Acre"),
    (1, "Alagoas"),
    (2, "Amapá"),
    (3, "Amazonas"),
    (4, "Bahia"),
    (5, "Ceará"),
    (6, "Distrito Federal"),
    (7, "Espírito Santo"),
    (8, "Goiás"),
    (9, "Maranhão"),
    (10, "Mato Grosso"),
    (11, "Mato Grosso do Sul"),
    (12, "Minas Gerais"),
    (13, "Pará"),
    (14, "Paraíba"),
    (15, "Paraná"),
    (16, "Pernambuco"),
    (17, "Piauí"),
    (18, "Rio de Janeiro"),
    (19, "Rio Grande do Norte"),
    (20, "Rio Grande do Sul"),
    (21, "Rondônia"),
    (22, "Roraima"),
    (23, "Santa Catarina"),
    (24, "São Paulo"),
    (25, "Sergipe"),
    (26, "Tocantins"),
    (27, "Indeterminado"),
]

SALARY_RANGES = [
    (1, "R$ 0,00 a R$ 1.000,00"),
    (2, "R$ 1.000,01 a R$ 3.000,00"),
    (3, "R$ 3.000,01 a R$ 6.000,00"),
    (4, "R$ 6.000,01 a R$ 10.000,00"),
    (5, "R$ 10.000,01 a R$ 13.000,00"),
    (6, "R$ 13.000,01 a R$ 16.000,00"),
    (7, "R$ 16.000,01 a R$ 19.000,00"),
    (8, "R$ 19.000,01 a R$ 21.000,00"),
    (9, "R$ 21.000,01 ou mais"),
    (10, "A combinar"),
]

JOB_LEVELS = [
    (1, "Estágio"),
    (2, "Junior"),
    (3, "Pleno"),
    (4, "Sênior"),
    (5, "Indeterminado"),
]

CONTRACT = [
    (1, "A combinar"),
    (2, "CLT"),
    (3, "PJ"),
    (4, "Estágio"),
]

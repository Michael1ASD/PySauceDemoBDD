import os
from decouple import Config, RepositoryIni

env = os.getenv('APP_ENV', 'dev')
if env == 'prod':
    config = Config(RepositoryIni('settings.prod.ini'))
else:
    config = Config(RepositoryIni('settings.dev.ini'))

DEBUG = config('DEBUG', default=False, cast=bool)
SECRET_KEY = config('SECRET_KEY')
EMAIL_HOST = config('EMAIL_HOST', default='localhost')
EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)
DATABASE_URL = config('DATABASE_URL')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])

# Jak ustawić zmienną środowiskową
# Aby ustawić środowisko na produkcję, możesz ustawić zmienną środowiskową APP_ENV przed uruchomieniem aplikacji:
#
# bash
# Copy
# export APP_ENV=prod
# # następnie uruchom swoją aplikację
# W ten sposób możesz łatwo zarządzać konfiguracją dla różnych środowisk, zmieniając tylko plik konfiguracyjny i zmienną środowiskową.
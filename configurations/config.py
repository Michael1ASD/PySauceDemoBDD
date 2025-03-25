from decouple import Config, RepositoryEnv
import os

env = os.getenv('APP_ENV', 'dev')
print(f"Loaded APP_ENV: {env}")
base_path = r'C:\Development\PySauceDemo\configurations'
env_file = os.path.join(base_path, f'config.{env}.env')

config = Config(RepositoryEnv(env_file))

DEBUG = config('DEBUG', default=False, cast=bool)
LOGIN_URL = config('LOGIN_URL')
VALID_USERNAME = config('VALID_USERNAME')
VALID_PASSWORD = config('VALID_PASSWORD')

# Scripts to run tests
# $env:APP_ENV='prod'; pytest -v test_cases/test_login.py
# $env:APP_ENV='dev'; pytest -v test_cases/test_login.py

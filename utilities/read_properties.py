import configparser

config = configparser.RawConfigParser()
config.read('C:/Development/PySauceDemo/configurations/config.ini')

class ReadConfig:
    @staticmethod
    def get_login_page_url():
        url = config.get('login', 'LOGIN_URL')
        return url
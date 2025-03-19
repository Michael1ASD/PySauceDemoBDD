import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogMaker
from base_pages.LoginPage import LoginPage
from base_pages.AllItems import AllItems
from base_pages.ExpandedList import ExpandedList
from utilities.assertions import Assertion

class TestProducts:
    login_url = ReadConfig.get_login_page_url()
    valid_username = 'standard_user'
    valid_password = 'secret_sauce'
    logger = LogMaker.log_gen()


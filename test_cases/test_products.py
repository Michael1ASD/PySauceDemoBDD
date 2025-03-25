import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.custom_logger import LogMaker
from base_pages.LoginPage import LoginPage
from base_pages.AllItems import AllItems
from base_pages.ExpandedList import ExpandedList
from utilities.assertions import Assertion

class TestProducts:
    logger = LogMaker.log_gen()


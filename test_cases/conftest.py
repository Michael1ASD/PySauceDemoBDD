import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def setup():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("enable-logging")
    chrome_options.add_argument("v=1")
    chrome_options.add_argument("--start-maximized")
    log_file_path = "chromedriver.log"
    chrome_options.add_argument(f"--log-path={log_file_path}")
    chrome_options.add_argument("--log-level=ALL")
    driver = webdriver.Chrome(options=chrome_options)
    return driver
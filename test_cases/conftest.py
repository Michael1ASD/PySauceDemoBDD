import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging

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


# Konfiguracja logowania
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

logger = logging.getLogger(__name__)

def pytest_runtest_logreport(report):
    if report.failed:
        logger.error(f"Test {report.nodeid} failed. Reason: {report.longrepr}")
    elif report.passed:
        logger.info(f"Test {report.nodeid} passed.")
    elif report.skipped:
        logger.warning(f"Test {report.nodeid} skipped.")
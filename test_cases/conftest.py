import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

import logging

# @pytest.fixture
# def setup():
#     chrome_options = Options()
#     # chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--disable-dev-shm-usage")
#     chrome_options.add_argument("enable-logging")
#     chrome_options.add_argument("v=1")
#     chrome_options.add_argument("--start-maximized")
#     log_file_path = "chromedriver.log"
#     chrome_options.add_argument(f"--log-path={log_file_path}")
#     chrome_options.add_argument("--log-level=ALL")
#     driver = webdriver.Chrome(options=chrome_options)
#     return driver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                             help="Choose browser: chrome, firefox, or edge")

@pytest.fixture
def setup(request):
    browser_name = request.config.getoption("browser")
    driver = None

    if browser_name == "chrome":
        chrome_options = ChromeOptions()
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

    elif browser_name == "edge":
        edge_options = EdgeOptions()
        edge_options.use_chromium = True  # Upewnij się, że używasz wersji Chromium Edge
        edge_options.add_argument("--disable-dev-shm-usage")
        edge_options.add_argument("enable-logging")
        edge_options.add_argument("v=1")
        edge_options.add_argument("--start-maximized")
        log_file_path = "edgedriver.log"
        edge_options.add_argument(f"--log-path={log_file_path}")
        edge_options.add_argument("--log-level=ALL")
        driver = webdriver.Edge(options=edge_options)
        return driver

    elif browser_name == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--start-maximized")
        log_file_path = "geckodriver.log"
        firefox_options.log.level = "trace"
        driver = webdriver.Firefox(options=firefox_options)
        return driver

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    # yield driver
    # driver.quit()

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
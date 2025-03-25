import logging
import pytest

class LogMaker:
    @staticmethod
    def log_gen():
        logging.basicConfig(filename="C:/Development/PySauceDemo/logs/saucedemo.log", format="%(asctime)s:%(levelname)s:%(message)s",
                            datefmt="%Y-%m=%d %H:%M:%S",force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger


# # Konfiguracja logowania
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
# )
#
# logger = logging.getLogger(__name__)
#
# def pytest_runtest_logreport(report):
#     if report.failed:
#         logger.error(f"Test {report.nodeid} failed. Reason: {report.longrepr}")
#     elif report.passed:
#         logger.info(f"Test {report.nodeid} passed.")
#     elif report.skipped:
#         logger.warning(f"Test {report.nodeid} skipped.")
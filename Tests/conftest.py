import datetime
import os
import pytest
import allure
import glob
from Library.store import Store


@pytest.fixture(autouse=True)
def before_each():
    print('*-* Before each INITIALIZATION')
    try:
        yield
        for driver in Store.drivers:
            root_dir = os.path.dirname(os.path.abspath(__file__)).replace("/Tests", "")
            name = 'img%s.png' % datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            config_path = root_dir + '/reports/screenshots/' + name
            driver.save_screenshot(config_path)
            allure.attach.file(config_path, name=name, attachment_type=allure.attachment_type.PNG)
    except Exception as e:
        print(e)
    print('*-* After each END')


@pytest.fixture(scope='module', autouse=True)
def before_module():
    print('*-* Before module INITIALIZATION')
    yield
    for driver in Store.drivers:
        driver.quit()
    print('*-* After module END')


def pytest_configure(config):
    """
    Allows plugins and conftest files to perform initial configuration.
    This hook is called for every plugin and initial conftest
    file after command line options have been parsed.
    """
    print("*-* pytest_configure")
    root_dir = os.path.dirname(os.path.abspath(__file__)).replace("/Tests", "")
    config_path = root_dir + '/reports/screenshots/*.png'
    for CleanUp in glob.glob(config_path):
        print(CleanUp)
        os.remove(CleanUp)


def pytest_sessionstart(session):
    """
    Called after the Session object has been created and
    before performing collection and entering the run test loop.
    """
    print("*-* pytest_sessionstart")


def pytest_sessionfinish(session, exitstatus):
    """
    Called after whole test run finished, right before
    returning the exit status to the system.
    """
    print("*-* pytest_sessionfinish")


def pytest_unconfigure(config):
    """
    called before test process is exited.
    """
    print("*-* pytest_unconfigure")

import pytest
import selenium.webdriver.support.expected_conditions as ec
import self as self
from _pytest import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import unittest

#@pytest.fixture()
#def enviroment_setup():
    #global driver
    #driver = webdriver.Chrome('/Users/lukaszswieboda/Downloads/chromedriver')
    #driver.get("https://thetestingworld.com/testings")
    #driver.refresh()
    #driver.maximize_window()
    #yield
    #driver.close()


class MainTests(unittest.TestCase):

    def test_verify_registration(self):
        self.driver = webdriver.Chrome('/Users/lukaszswieboda/Downloads/chromedriver')
        driver = self.driver
        driver.get("https://thetestingworld.com/testings")
        wait = WebDriverWait(driver, 100)
        wait.until(ec.text_to_be_present_in_element(By.ID, 'countryId'), "India")
        obj = Select(driver.find_element_by_id("countryId"))
        obj.select_by_visible_text("India")

        wait.until(ec.text_to_be_present_in_element(By.ID, 'stateId'), "Delhi")
        obj = Select(driver.find_element_by_id("stateId"))
        obj.select_by_visible_text("Delhi")



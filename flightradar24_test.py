import unittest
from selenium import webdriver

class MainTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome('/Users/lukaszswieboda/Downloads/chromedriver')

    def setUp(self):
        print('przygotowanie do testu')

    def test_titleAssertion(self):
        driver = self.driver
        driver.get('https://www.flightradar24.com')
        title = driver.title
        print(title)
        assert 'Flightradar24: Live Flight Tracker - Real-Time Flight Tracker Map' == title

    @classmethod
    def tearDownClass(self):
        self.driver.quit()







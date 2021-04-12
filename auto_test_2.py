import unittest
from selenium import webdriver

class MainTests(unittest.TestCase):
   @classmethod
   def setUpClass(self):
       self.driver = webdriver.Chrome('/Users/lukaszswieboda/Downloads/chromedriver')
       # Dodajmy do metody setUp() inicjalizację drivera usuwając jednocześnie inne polecenia, które tam dodaliśmy

   def test_demo_login(self):
       driver = self.driver
       driver.get('https://demobank.jaktestowac.pl/logowanie_etap_1.html')
       title = driver.title
       print(title)
       assert 'Demobank - Bankowość Internetowa - Logowanie' == title

   def test_demo_pulpit(self):
       driver = self.driver
       driver.get('https://demobank.jaktestowac.pl/pulpit.html')
       title = driver.title
       print(title)
       assert 'Demobank - Bankowość Internetowa - Pulpit' == title

   @classmethod
   def tearDownClass(self):
       self.driver.quit()

       # tearDownClass()
       # Dzięki niej dopiero po wykonaniu wszystkich metod w klasie nastąpi zamknięcie przeglądarki



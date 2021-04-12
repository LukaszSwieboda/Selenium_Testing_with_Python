from selenium import webdriver

def test_checkbox_selenium_easy():
    driver = webdriver.Chrome('/Users/lukaszswieboda/Downloads/chromedriver')
    # 1. get to seleniumeasy.com
    driver.get('https://www.seleniumeasy.com/test/basic-checkbox-demo.html')

    # 2. click the checkbox demo
    checkbox = driver.find_element_by_id("isAgeSelected")
    checkbox.click()

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

def test_lava_golem_is_displayed():
    driver = webdriver.Chrome('/Users/lukaszswieboda/Downloads/chromedriver')
    # 1. go to statsroyale.com
    driver.get('https://statsroyale.com')

    # 2. go to cards page
    driver.find_element(By.CSS_SELECTOR, "[href='/cards']").click()

    # 3. assert Golem is displayed
    golem_card = driver.find_element(By.CSS_SELECTOR, "[href*='Golem']")
    assert golem_card.is_displayed()



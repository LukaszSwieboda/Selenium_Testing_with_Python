from selenium import webdriver
from selenium.webdriver.common.by import By


def test_checkbox():
    driver = webdriver.Chrome('/Your/Driver/Path/')
    #1. go to statsroyale.com
    driver.get('https://statsroyale.com')

    #2. click the Cards button
    #driver.find_element(By.CSS_SELECTOR, "[href='/cards']").click()
    # I have tried also with css selector and it's fine.

    cards_button = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[2]/div/div[3]/a').isDisplayed()
    print('card_button', cards_button)
    cards_button.click()

    #3. unchecks the Common Filter
    checkbox_common = driver.find_element_by_id('common-cards')
    print('halo halo kkk8888', checkbox_common)
    checkbox_common.click()




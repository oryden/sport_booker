from dotenv import load_dotenv
import os

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from webdriver_manager.chrome import ChromeDriverManager


if __name__ == '__main__':
    load_dotenv('credentials.env')

    user_name = os.getenv('USER_NAME')
    password = os.getenv('PASSWORD')

    # Creating the webdriver
    browser = webdriver.Chrome(ChromeDriverManager().install())

    # Link to matchi
    link = r"https://www.matchi.se/login/auth"
    browser.get(link)  # navigate to the page

    # Set user name
    username_input = browser.find_element_by_id("username")
    username_input.clear()
    username_input.send_keys(user_name)

    # Set password
    password_input = browser.find_element_by_id("password")
    password_input.clear()
    password_input.send_keys(password)

    # CLick login
    log_in_button = browser.find_element_by_css_selector('.btn-success').click()
    ActionChains(browser).click(log_in_button).perform()

    #

    # # Go to PDL center booking
    # link_text = "PDL Center Frihamnen"
    # pdl_center_link_object = browser.find_elements_by_xpath("//*[contains(text(), '{}')]".format(link_text))
    # ActionChains(browser).click(pdl_center_link_object).perform()

    delay = 10 # seconds
    try:
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.LINK_TEXT, 'PDL Center Frihamnen')))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")

    print("Get browser")
    browser.get(r"https://www.matchi.se/facilities/pdlcenter")




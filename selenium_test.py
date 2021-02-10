from dotenv import load_dotenv
import os
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from webdriver_manager.chrome import ChromeDriverManager

from date_transforms import matchi_date_split


# Change to day
date_to_go_to = "2021-01-27"
day_to_go = 27
month_to_go = 1

if __name__ == '__main__':
    load_dotenv('credentials.env')

    user_name = os.getenv('USER_NAME')
    password = os.getenv('PASSWORD')

    # Creating the webdriver
    browser = webdriver.Chrome(ChromeDriverManager().install())

    browser.set_window_position(0, 0)
    browser.set_window_size(1600, 1000)

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

    delay = 10 # seconds
    try:
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.LINK_TEXT, 'PDL Center Frihamnen')))
        print("Page is ready 1!")
    except TimeoutException:
        print("Loading took too much time!")

    print("Get browser")
    browser.get(r"https://www.matchi.se/facilities/pdlcenter")


    # Find the right button
    try:
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-circle')))
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'picker_daily')))
        print("Page is ready 2!")
    except TimeoutException:
        print("Loading took too much time!")

    text_date = browser.find_element_by_id('picker_daily').text
    act_date, act_month = matchi_date_split(text_date)

    while (act_date < day_to_go) or (act_month < month_to_go):

        try:
            myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-circle')))
            print("Loaded: {}".format(text_date))
        except TimeoutException:
            print("Loading took too much time for: {}!".format(text_date))
            break

        time.sleep(2)
        right_button = browser.find_elements_by_class_name('btn-circle')[1]
        ActionChains(browser).click(right_button).perform()

        time.sleep(2)
        try:
            myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'picker_daily')))
            print("Updated to date: {}".format(text_date))
        except TimeoutException:
            print("Loading took too much time after button click: {}!".format(text_date))
            break

        text_date = browser.find_element_by_id('picker_daily').text
        act_date, act_month = matchi_date_split(text_date)

    print("Date loops ends on: {}".format(text_date))

    # Get all html code from selenium
    # Select the free elements
    # Click on selected free time based on some decision rules
    # Book time with clip-card
    # - Need a loop here if time is booked allready
    # Close down program

    #browser.refresh()

    print("updated webpage")

    free_times = browser.find_elements_by_class_name("slot free")
    print(free_times)




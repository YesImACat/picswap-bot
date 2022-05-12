from re import A
from selenium import webdriver
from threading import Thread
from random import randint
import os
import time


def Bot(filter, headless):
    site = "https://pictureswap.co/"

    op = webdriver.ChromeOptions()
    
    if headless:
        op.add_argument('--headless')

    driver = webdriver.Chrome(options=op)

    file = os.path.abspath("torn.png")
    driver.get(site)

    upload_button_xpath = '//*[@id="file"]'
    swap_button_xpath = '//*[@id="form"]/div[1]/div/button'
    nsfw_button_xpath = '//*[@id="form"]/div[2]/label[3]'
    sfw_button_xpath = '//*[@id="form"]/div[2]/label[2]'
    random_button_xpath = '//*[@id="form"]/div[2]/label[1]'
    upload_new_button_xpath = '//*[@id="message"]/button'
    image_xpath = '//*[@id="preview"]'
    
    upload_button = driver.find_element("xpath", upload_button_xpath)
    swap_button = driver.find_element("xpath", swap_button_xpath)
    nsfw_button = driver.find_element("xpath", nsfw_button_xpath)
    sfw_button = driver.find_element("xpath", sfw_button_xpath)
    random_button = driver.find_element("xpath", random_button_xpath)

    if filter == "nsfw":
        nsfw_button.click()

    if filter == "sfw":
        sfw_button.click()

    upload_button.send_keys(file)
    print("Started a new ", filter, " thread")

    while True:
        time.sleep(randint(3, 10))
        try:
            swap_button.click()

        except:
            driver.find_element("xpath", upload_new_button_xpath).click()

        else:
            print("Success! ", driver.find_element("xpath", image_xpath).get_property("naturalHeight"), "x", driver.find_element("xpath", image_xpath).get_property("naturalWidth"), " image returned", sep="")

# Multi-threading must be headless
threads_per_filter = 20
for _ in range(threads_per_filter):
    a = Thread(target=Bot, args=["nsfw", True])
    a.start()

    b = Thread(target=Bot, args=["sfw", True])
    b.start()

    c = Thread(target=Bot, args=["random", True])
    c.start()
    time.sleep(2)

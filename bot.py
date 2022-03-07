from selenium import webdriver
from threading import Thread
from random import randint
import os
import time


def Bot():
    site = "https://pictureswap.co/"

    op = webdriver.ChromeOptions()
    op.add_argument('--headless')

    driver = webdriver.Chrome(options=op)

    file = os.path.abspath("torn.png")
    driver.get(site)

    upload_button_xpath = '//*[@id="file"]'
    swap_button_xpath = '//*[@id="form"]/div[1]/div/button'
    nsfw_button_xpath = '//*[@id="form"]/div[2]/label[3]'
    upload_new_button_xpath = '//*[@id="message"]/button'
    image_xpath = '//*[@id="preview"]'
    
    upload_button = driver.find_element("xpath", upload_button_xpath)
    swap_button = driver.find_element("xpath", swap_button_xpath)
    nsfw_button = driver.find_element("xpath", nsfw_button_xpath)

    nsfw_button.click()
    upload_button.send_keys(file)

    while True:
        time.sleep(randint(3, 10))
        try:
            swap_button.click()

        except:
            driver.find_element("xpath", upload_new_button_xpath).click()

        else:
            print("Success! ", driver.find_element("xpath", image_xpath).get_property("naturalHeight"), "x", driver.find_element("xpath", image_xpath).get_property("naturalWidth"), sep="")


for _ in range(5):
    t = Thread(target=Bot)
    t.start()
    time.sleep(2)

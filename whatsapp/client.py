# Client properties
import asyncio
import time

# Whatsapp.py properties
from .core import Core

# selenium properties
from selenium import webdriver

class Client:
    def __init__(self):
        """The main class to create the bot"""

    def run(self, save_login: bool):
        # setup webdriver
        options = webdriver.ChromeOptions()
        options.add_argument("--user-data-dir=chrome-data")
        Core.driver = webdriver.Chrome("./Selenium/chromedriver.exe", chrome_options=options)
        
        # setup whatsapp web
        Core.driver.get("https://web.whatsapp.com/")

        # check if already logged
        save_checked = True
        while True:
            qr_code = Core.driver.find_elements_by_class_name(Core.classes.QRCODE)
            if not qr_code:
                startup_load = Core.driver.find_elements_by_id("Startup")
                if not startup_load:
                    break
            elif save_checked:
                if save_login == False:
                    Core.driver.find_element_by_xpath("//input[@name='rememberMe']").click()
                    save_checked = False
        # start the main loop on Core()
        time.sleep(1)

    async def listener(self):
        pass 
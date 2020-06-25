from selenium import webdriver
from .client import Client

class Sticker(object):
    def __init__(self, link):
        self.link = link
        self.driver = Client().driver
        self.class_name = Client().sticker_class

    def get_sticker(self, id):
        with open('sticker-{}.png'.format(str(id)), 'wb') as file:
            file.write(self.driver.find_element_by_class_name(self.class_name).screenshot_as_png)
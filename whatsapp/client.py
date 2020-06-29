import time
import asyncio
import pyperclip
import requests
import emoji

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

from selenium.common.exceptions import NoSuchElementException

from .sticker import Sticker

class Client():
    """The Client implementation to Whatsapp Web. Used to save the element's classes, open driver and setup a Chrome profile.
    The other stuff are done by the Client's functions."""
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--user-data-dir=chrome-data")
        self.driver = webdriver.Chrome("./Selenium/chromedriver.exe", options=chrome_options)

        self.chat_class = "_2hqOq"
        self.sticker_class = "_11S5R"
        self.qrcode_class = "_2nIZM"
        self.input_class = '_3uMse'

        self._listeners = {}
        self._listeners["on_message"] = []

    def run(self, message_console: bool, perma_connection = False):
        """Will open the Whatsapp Web page on Selenium and run the main loop."""
        self.driver.get("https://web.whatsapp.com/")
        self.message_console = message_console
        if perma_connection == False:
            try:
                self.driver.find_element_by_xpath("//input[@name='rememberMe']").click()
            except:
                pass
        while True:
            try:
                self.driver.find_element_by_class_name(self.qrcode_class)
            except:
                break
        time.sleep(5)
        self.event_loop = asyncio.get_event_loop()
        self._listeners["on_ready"]()
        self.event_loop.run_until_complete(self.listener())

    def select_contact(self, contact):
        self.contact = contact

    async def listener(self):
        """The `listener()` starts a loop that will get the last message and return the message and the author to the respective functions: `get_message()` and `get_message_author`"""
        message_filter = ""
        while True:
            self.driver.find_element_by_xpath("//span[@title='"+ self.contact +"']").click()
            await asyncio.sleep(0.5)
            try: # Try find text
                chat = self.driver.find_elements_by_class_name(self.chat_class)
                ultimo_chat = len(chat) - 1
                self.message = chat[ultimo_chat].find_element_by_css_selector('span.selectable-text').text

            except NoSuchElementException:
                try: # Try find stickers
                    stickers = self.driver.find_elements_by_class_name(self.sticker_class)
                    ultimo_sticker = len(stickers) - 1
                    self.message = stickers[ultimo_sticker].get_attribute("src")
                except:
                    raise Exception("Non-regonizable object.")
                else: # If finds one, set them on self.message and writes the author on self.name
                    if message_filter != self.message:
                        nomes = stickers[ultimo_sticker].find_elements_by_xpath("//span[not(@data-icon)][@aria-label]")
                        ultimo_nome = len(nomes) - 1
                        self.name = nomes[ultimo_nome].get_attribute("aria-label")
                        sticker = Sticker(self.message)
                        await asyncio.sleep(2)
                        sticker.get_sticker(1)
                        if self.message_console:
                            print(self.get_message_author() + ":", self.get_message())
                        message_filter = self.get_message()
                    else:
                        continue

            else:
                if message_filter != self.message: #if finds one text, do the same
                    nomes = chat[ultimo_chat].find_elements_by_xpath("//span[not(@data-icon)][@aria-label]")
                    ultimo_nome = len(nomes) - 1
                    self.name = nomes[ultimo_nome].get_attribute("aria-label")
                    if self.message_console:
                        print(self.get_message_author() + ":", self.get_message())
                    message_filter = self.get_message()
                    try:
                        functions = self._listeners["on_message"]
                    except KeyError():
                        continue
                    else:
                        for function in functions:
                            self.event_loop.create_task(function())
                else:
                    continue

    async def send_message(self, message): # send a message
        """Will send a message to contact previous selected."""
        input_box = self.driver.find_element_by_class_name(self.input_class)
        await asyncio.sleep(1)
        input_box.click()
        message = emoji.emojize(message, True)
        pyperclip.copy(message)
        input_box.send_keys(Keys.CONTROL + "v")
        button = self.driver.find_element_by_xpath("//span[@data-icon='send']")
        await asyncio.sleep(0.05)
        button.click()

    def event(self, type = None): # the decorator `event()` will wrap the command used to be executed on listener
        """A decorator to convert functions to executable commands by chat."""
        def decorator(f):
            if type != None:
                self._listeners[type].append(f)
            else:
                self._listeners[f.__name__] = f
            print(self._listeners)
            return f
        return decorator

    def get_message_author(self): # Returns the message's author
        """Return the last message's author.
        
        OBS: This function needs the Listener's execution."""
        return str(self.name).replace(":", "")

    def get_message(self): # Returns the message
        """Return the last message send to chat.
        
        OBS: This function needs the Listener's execution."""
        return str(self.message)
    
    def latency(self):
        start = time.time()
        requests.get("https://www.whatsapp.com")
        end = time.time()
        return end - start

    def stop(self):
        self.driver.quit()
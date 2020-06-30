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

        self.CHAT = "_2hqOq"
        self.CHAT_IN = "message-in"
        self.CHAT_OUT = "message-out"
        self.STICKER = "_11S5R"
        self.QRCODE = "_2nIZM"
        self.INPUTBOX = '_3uMse'

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
                self.driver.find_element_by_class_name(self.QRCODE)
            except:
                break

        while True:
            try:
                self.driver.find_element_by_class_name("startup")
            except:
                break
        time.sleep(2)
        self.event_loop = asyncio.get_event_loop()
        self.event_loop.run_until_complete(self.listener())

    def select_contact(self, contact):
        if type(contact) == tuple:
            self.contact, contact_type = contact
            if contact_type == "group":
                self.has_group = True
            elif contact_type == "user":
                pass
        elif type(contact) == list:
            for contact_tuple in contact:
                pass

    async def listener(self):
        """The `listener()` starts a loop that will get the last message and return the message and the author to the respective functions: `get_message()` and `get_message_author`"""
        
        await asyncio.sleep(5)
        message_filter = ""
        await self.get_user_info()
        self._listeners["on_ready"]()

        while True:
            self.driver.find_element_by_xpath("//span[@title='"+ self.contact +"']").click()
            await asyncio.sleep(0.5)
            try: # Try find text
                chat = self.driver.find_elements_by_class_name(self.CHAT)
                ultimo_chat = len(chat) - 1
                self.message = chat[ultimo_chat].find_element_by_css_selector('span.selectable-text').text

            except NoSuchElementException:
                try: # Try find stickers
                    stickers = self.driver.find_elements_by_class_name(self.STICKER)
                    ultimo_sticker = len(stickers) - 1
                    self.message = stickers[ultimo_sticker].get_attribute("src")
                except:
                    raise Exception("Non-regonizable object.")
                else: # If finds one, set them on self.message and writes the author on self.name
                    if message_filter != self.message:
                        self._listener_get_name(stickers, ultimo_sticker) 
                        sticker = Sticker(self.message)
                        await asyncio.sleep(2)
                        if self.message_console:
                            print(self.get_message_author() + ":", self.get_message())
                        message_filter = self.get_message()
                        self.function_exec()
                    else:
                        continue

            else:
                if message_filter != self.message: #if finds one text, do the same
                    self._listener_get_name(chat, ultimo_chat) 
                    if self.message_console:
                        print(self.get_message_author() + ":", self.get_message())
                    message_filter = self.get_message()
                else:
                    continue

    async def send_message(self, message): # send a message
        """Will send a message to contact previous selected."""
        input_box = self.driver.find_element_by_class_name(self.INPUTBOX)
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

    async def get_user_info(self):

        USER_PROFILE = '_1BjNO'
        USER_SETTINGS = '_3FRCZ'
        self.driver.find_element_by_class_name(USER_PROFILE).click()
        await asyncio.sleep(1)
        user_sets = self.driver.find_elements_by_class_name(USER_SETTINGS)

        self.username = user_sets[0].text
        self.user_message = user_sets[1].text

        self.driver.find_element_by_xpath("//span[@data-icon='back']").click()

    def stop(self):
        self.driver.quit()
        self.event_loop.close()
        self.event_loop.stop()
    
    def _listener_get_name(self, chat, last_chat):
        if self.has_group:
                classes = "FMlAw FdF4z _3Whw5"
                chat_in = self.driver.find_elements_by_class_name(self.CHAT_IN)
                last_chat_in = len(chat_in) - 1
                if last_chat_in == last_chat:
                    nomes = chat_in[last_chat].find_elements_by_xpath("//span[contains(@class, '"+ classes +"')]")
                    ultimo_nome = len(nomes) - 1
                    self.name = nomes[ultimo_nome].text
                else:
                    nomes = chat[last_chat].find_elements_by_xpath("//span[not(@data-icon)][@aria-label]")
                    ultimo_nome = len(nomes) - 1
                    self.name = nomes[ultimo_nome].get_attribute("aria-label")
        else:
            nomes = chat[last_chat].find_elements_by_xpath("//span[not(@data-icon)][@aria-label]")
            ultimo_nome = len(nomes) - 1
            self.name = nomes[ultimo_nome].get_attribute("aria-label")

    def function_exec(self):
        functions = self._listeners["on_message"]
        for function in functions:
            self.event_loop.create_task(function())
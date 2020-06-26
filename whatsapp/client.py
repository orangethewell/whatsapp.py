import time
import asyncio

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import NoSuchElementException

from .sticker import Sticker

class Client():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path="./Selenium/chromedriver.exe")

        self.chat_class = "_2hqOq"
        self.sticker_class = "_11S5R"
        self.qrcode_class = "_2nIZM"
        self.input_class = '_3uMse'

        self.func_dict = {}

    def run(self, perma_connection = False, prefix = "."):
        """Will open the Whatsapp Web page on Selenium and run the main loop."""
        self.driver.get("https://web.whatsapp.com/")
        if perma_connection == False:
            self.driver.find_element_by_xpath("//input[@name='rememberMe']").click()
        while True:
            try:
                self.driver.find_element_by_class_name(self.qrcode_class)
            except:
                break
        time.sleep(2)
        loop = asyncio.get_event_loop()
        loop.create_task(self.listener())
        loop.run_forever()

    def select_contact(self, contact):
        self.contact = contact

    async def listener(self):
        """Retorna o valor da última mensagem enviada no bate-papo."""
        while True:
            self.driver.find_element_by_xpath("//span[@title='"+ self.contact +"']").click()
            await asyncio.sleep(0.1)
            try:
                chat = self.driver.find_elements_by_class_name(self.chat_class)
                ultimo_chat = len(chat) - 1
                self.mensagem = chat[ultimo_chat].find_element_by_css_selector('span.selectable-text').text

            except NoSuchElementException:
                try:
                    stickers = self.driver.find_elements_by_class_name(self.sticker_class)
                    ultimo_sticker = len(stickers) - 1
                    self.mensagem = stickers[ultimo_sticker].get_attribute("src")
                except:
                    raise Exception("Non-regonizable object.")
                else:
                    nomes = stickers[ultimo_sticker].find_elements_by_xpath("//span[not(@data-icon)][@aria-label]")
                    ultimo_nome = len(nomes) - 1
                    self.name = nomes[ultimo_nome].get_attribute("aria-label")
                    sticker = Sticker(self.mensagem)
                    await asyncio.sleep(2)
                    sticker.get_sticker(1)
                    print(self.get_message_author + ":", self.get_message)

            else:
                nomes = chat[ultimo_chat].find_elements_by_xpath("//span[not(@data-icon)][@aria-label]")
                ultimo_nome = len(nomes) - 1
                self.name = nomes[ultimo_nome].get_attribute("aria-label")
                print(self.get_message_author() + ":", self.get_message())
                try:
                    fd = self.func_dict
                except KeyError:
                    continue
                else:
                    for key in fd:
                        if key == str(self.mensagem):
                            function = fd[key]
                            await function()

    async def send_message(self, message):
        """Usa as teclas para enviar uma mensagem. (OBS.: A mensagem é enviada inteira.)"""
        input_box = self.driver.find_element_by_class_name(self.input_class)
        await asyncio.sleep(1)
        input_box.click()
        raw_menssage = message.replace(" ", " _ ")
        raw_menssage = raw_menssage.replace("\n", " // ")

        # Formata a mensagem para que quando enviada, ela não envie comandos como ENTER
        # para enviar a mensagem direto e não quebrar a linha, que talvez era o que precisava.
        # Será alterado para um sistema de copiar e colar futuramente.

        for palavra in raw_menssage.split(" "):
            await asyncio.sleep(0.01)
            if palavra == "//":
                input_box.send_keys(Keys.SHIFT + Keys.ENTER)
            elif palavra == "_":
                input_box.send_keys(" ")
            else:
                input_box.send_keys(palavra)
        button = self.driver.find_element_by_xpath("//span[@data-icon='send']")
        time.sleep(0.05)
        button.click()

    def wait_for_message(self, message): # Decorador para comandos
        def decorator(f):
            self.func_dict[message] = f
            print(self.func_dict)
            return f
        return decorator

    def get_message_author(self): # Retorna o nome do autor da última mensagem
        return str(self.name).replace(":", "")

    def get_message(self): # Retorna a última mensagem
        return str(self.mensagem)
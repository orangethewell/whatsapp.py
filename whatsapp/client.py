import time
import asyncio

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import NoSuchElementException

from sticker import Sticker

class Client():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path="./Selenium/chromedriver.exe")

        self.chat_class = "_2hqOq"
        self.sticker_class = "_11S5R"
        self.qrcode_class = "_2nIZM"
        self.input_class = '_3uMse'

    def start(self, perma_connection = False):
        """Will open the Whatsapp Web page on Selenium."""
        self.driver.get("https://web.whatsapp.com/")
        # Desativa a conexão permanente caso o usário esteja testando o bot, para deixar
        # permanente, basta alterar o parâmetro perma_connection = True
        if perma_connection == False:
            self.driver.find_element_by_xpath("//input[@name='rememberMe']").click()
        while True:
            try:
                self.driver.find_element_by_class_name(self.qrcode_class)
            except:
                break

    def select_contact(self, contact):
        contact = self.driver.find_element_by_xpath("//span[@title='"+ contact +"'")
        contact.click()

    async def listen(self):
        """Retorna o valor da última mensagem enviada no bate-papo."""
        try:
            chat = self.driver.find_elements_by_class_name(self.chat_class)
            ultimo_chat = len(chat) - 1
            mensagem = chat[ultimo_chat].find_element_by_css_selector('span.selectable-text').text
            
            # Procura por textos na última mensagem enviada no chat, caso não encontre, o código
            # parte para a excessão que tenta achar um link, caso a última mensagem seja uma
            # imagem.

        except NoSuchElementException:
            try:
                stickers = self.driver.find_elements_by_class_name(self.sticker_class)
                ultimo_sticker = len(stickers) - 1
                mensagem = stickers[ultimo_sticker].get_attribute("src")
            except:
                raise Exception("Non-regonizable object.")
            else:
                nomes = stickers[ultimo_sticker].find_elements_by_xpath("//span[not(@data-icon)][@aria-label]")
                ultimo_nome = len(nomes) - 1
                nome = nomes[ultimo_nome].get_attribute("aria-label")
                sticker = Sticker(mensagem)
                time.sleep(2)
                sticker.get_sticker(1)
                return nome, mensagem
                
                # por fim, retorna os valores encontrados, no caso mensagem e nome do usuário.
        else:
            nomes = chat[ultimo_chat].find_elements_by_xpath("//span[not(@data-icon)][@aria-label]")
            ultimo_nome = len(nomes) - 1
            nome = nomes[ultimo_nome].get_attribute("aria-label")
            return nome, mensagem

    def send_message(self, message):
        """Usa as teclas para enviar uma mensagem. (OBS.: A mensagem é enviada inteira.)"""
        input_box = self.driver.find_element_by_class_name(self.input_class)
        time.sleep(1)
        input_box.click()
        raw_menssage = message.replace(" ", " _ ")
        raw_menssage = raw_menssage.replace("\n", " // ")

        # Formata a mensagem para que quando enviada, ela não envie comandos como ENTER
        # para enviar a mensagem direto e não quebrar a linha, que talvez era o que precisava.
        # Será alterado para um sistema de copiar e colar futuramente.

        for palavra in raw_menssage.split(" "):
            if palavra == "//":
                input_box.send_keys(Keys.SHIFT + Keys.ENTER)
            elif palavra == "_":
                input_box.send_keys(" ")
            else:
                input_box.send_keys(palavra)
        button = self.driver.find_element_by_xpath("//span[@data-icon='send']")
        time.sleep(0.05)
        button.click()

    async def wait_for_message(self, message):
        found = False
        while found == False:
            await asyncio.sleep(0.05)
            message_test = self.listen()[1]
            if message_test == message:
                def decorator(fun):
                    return fun()
                return decorator
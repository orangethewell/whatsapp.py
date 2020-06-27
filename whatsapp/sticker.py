from . import client

class Sticker(object):
    def __init__(self, link):
        self.link = link
        self.class_name = client.Client().sticker_class

    def get_sticker(self, id):
        with open('sticker-{}.png'.format(str(id)), 'wb') as file:
            file.write(client.Client().driver.find_element_by_class_name(self.class_name).screenshot_as_png)
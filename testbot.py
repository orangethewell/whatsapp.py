import whatsapp

bot = whatsapp.Client()

bot.start_client()

def on_start():
    print("iniciado!")

bot.select_contact("Karina")
bot.wait_for_message()
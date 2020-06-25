import whatsapp

bot = whatsapp.Client()

bot.start_client()

@whatsapp.on_ready
def on_start():
    print("iniciado!")

bot.select_contact("Karina")
bot.wait_for_message()
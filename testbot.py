import whatsapp

bot = whatsapp.Client()

bot.start()

bot.select_contact("my friend")

@bot.wait_for_message("!foo")
async def print_foo():
    bot.send_message("foo")

import whatsapp 
import asyncio

bot = whatsapp.Client()
bot.select_contact("Teste Bot")

@bot.event("on_message")
async def func():
    if bot.get_message() == "?teste":
        message = "This is a test!"
        await bot.send_message(message)

bot.run()

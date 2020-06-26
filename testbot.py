import whatsapp 
import asyncio

bot = whatsapp.Client()
bot.select_contact("Teste Bot")

@bot.event("on_message")
async def func():
    if bot.get_message() == "?poema":
        poem = open("poem.txt", 'r', encoding="utf-8").read()
        await bot.send_message(poem)

bot.run()

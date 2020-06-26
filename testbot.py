import whatsapp
import asyncio

bot = whatsapp.Client()
bot.select_contact("My friend")

@bot.wait_for_message("?poema")
async def func():
    poem = open("poem.txt", 'r').read()
    await bot.send_message(poem)

bot.run()

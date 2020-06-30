import whatsapp 
import asyncio
import random

client = whatsapp.Client()
client.select_contact(("", "group"))

@client.event()
def on_ready():
    print("logged as " + client.username)
    print("user message '" + client.user_message + "'")

@client.event("on_message")
async def pingtest():
    if client.get_message() == "?ping":
        await client.send_message("Pong! :ping_pong: latência: " + str(round(client.latency(), 2)) + "ms!")

@client.event("on_message")
async def stop_client():
    if client.get_message() == "?parar" and client.get_message_author() == "Você":
        await client.send_message("parando o cliente do bot... Para me fazer retornar, basta rodar o código de novo!")
        client.stop()
    elif client.get_message == "?parar" and client.get_message_author() != "Você":
        await client.send_message("Você não tem direito de pedir esse comando!")

@client.event("on_message")
async def send_poem():
    if client.get_message() == "?poema":
        await client.send_message("É para já!")
        id = random.randrange(1, 3)
        título, poema, autor = open("poems/poem" + str(id) + ".txt", 'r', encoding="utf").read().split("'='")
        if título.replace('\n', '') != "NoneTitle":
            await client.send_message("O título do texto é *" + título.replace('\n', '') + "*.")
        await client.send_message(poema)
        await client.send_message("Escrito por: *" + autor.replace('\n', '') + "*")

client.run(True, perma_connection=True)
import whatsapp 
import asyncio
import emoji

client = whatsapp.Client()
client.select_contact("Teste Bot")

@client.event()
def on_ready():
    print("logged!")

@client.event("on_message")
async def pingtest():
    if client.get_message() == "?ping":
        await client.send_message("Pong! :ping_pong: latência: " + str(round(client.latency(), 2)) + "ms!")

@client.event("on_message")
async def stop_client():
    if client.get_message() == "?stop" and client.get_message_author() == "Você":
        client.stop()

client.run(True, perma_connection=True)
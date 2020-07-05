import asyncio

class Core:
    # Set main loop
    main_loop = asyncio.get_event_loop()
    driver = None
    # Save WebElement classes
    class classes:
        QRCODE = "_2nIZM"
        CHAT = "_2hqOq"
        CHAT_IN = "message-in"
        CHAT_OUT = "message-out"
        STICKER = "_11S5R"
        INPUTBOX = '_3uMse'
from interactions import listen
from interactions.api.events import Ready, Disconnect
from data.DBManager import DBManager as DBManager
import asyncio

class ConnectionListeners:
    """
    -------------------------------------------------------------------------------
    Program:    ConnectionListeners.py
    Author:     Patrick J. McGranahan
    Date:       05.19.2025
    Language:   python
    Purpose:    The purpose of this code is to contain listeners that connect and
                disconnect from the DB
    -------------------------------------------------------------------------------
    Change Log:
    Who  When           What
    PJM  05.19.2025     Created comment block.
    -------------------------------------------------------------------------------
    """
    # Listeners
    @listen(event_name=Ready)
    async def on_ready() -> None:
        """
        Triggers when the bot connects. Turns on the DB connection.
        """
        print("Bot has connected to the server. Attempting to connect to DB...")
        try:
            DBManager.open_all()
            print("DB connected.")
        except:
            print("Unable to connect to DB.")

    @listen(event_name=Disconnect)
    async def on_disconnect() -> None:
        """
        Triggers when the bot disconnects. Turns off the DB connection.
        """
        print("Bot has been disconnected from the server. Attempting to disconnect DB...")
        try:
            DBManager.close_all()
            print("DB disconnected.")
        except:
            print("Unable to close DB.")
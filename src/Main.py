from interactions import Client
from cmds.CommandList import CommandList as CommandList
from listeners.ConnectionListeners import ConnectionListeners
import os
from dotenv import load_dotenv, dotenv_values

class Main:
    """
    -------------------------------------------------------------------------------
    Program:    Main.py
    Author:     Patrick J. McGranahan
    Date:       05.10.2025
    Language:   python
    Purpose:    To serve as a main program for the GemTrackerBot project.
    -------------------------------------------------------------------------------
    Change Log:
    Who  When           What
    PJM  05.13.2025     Added imports for custom listeners.
    PJM  05.12.2025     Began rewiring for the interactions module.
    PJM  05.10.2025     Added imports 'discord' and 'commands'.
    PJM  05.10.2025     Created main() method and established the script as a main
                        program.
    PJM  05.10.2025     Created class Main, created comment block.
    -------------------------------------------------------------------------------
    """

    def main():
        load_dotenv() # Load enviromental variables

        # Load bot and commands
        bot = Client()
        bot.add_command(func=CommandList.test)
        bot.add_command(func=CommandList.commands)
        bot.add_command(func=CommandList.create)

        # Load listeners
        bot.add_listener(listener=ConnectionListeners.on_ready)
        bot.add_listener(listener=ConnectionListeners.on_disconnect)

        # Retieve token and run the bot
        bot_token = os.getenv(key="BOT_TOKEN")
        bot.start(token=bot_token)

    if __name__ == "__main__":
        main()
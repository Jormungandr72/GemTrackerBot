from sqlite3 import Connection, connect, Cursor

class DBManager:
    """
    -------------------------------------------------------------------------------
    Program:    DBManager.py
    Author:     Patrick J. McGranahan
    Date:       05.13.2025
    Language:   python
    Purpose:    The purpose of this code is to manage database connections for the
                gem tracker bot.
    -------------------------------------------------------------------------------
    Change Log:
    Who  When           What
    PJM  05.17.2025     Deleted getters for troubleshooting, need to get back to 
                        that later.
    PJM  05.17.2025     Deleted constructor. Made all attributes static.
    PJM  05.14.2025     Made connection and cursor class variables.
    PJM  05.13.2025     Created constructor and close_all().
    PJM  05.13.2025     Created DBManager.py, created comment block.
    -------------------------------------------------------------------------------
    """
    # Class variables
    con: Connection
    cur: Cursor
    
    # Methods
    @staticmethod
    def open_all() -> None:
        """
        Opens all database connections.
        """
        DBManager.con = connect(database="src/data/db.sqlite3")
        DBManager.cur = DBManager.con.cursor()

    @staticmethod
    def close_all() -> None:
        """
        Closes all database connections.
        """
        DBManager.cur.close()
        DBManager.con.close()
        
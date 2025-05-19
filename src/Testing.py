from data.DBManager import DBManager as DBManager

class Testing:
    """
    -------------------------------------------------------------------------------
    Program:    Testing.py
    Author:     Patrick J. McGranahan
    Date:       05.19.2025
    Language:   python
    Purpose:    To test misc code for the GemTrackerBot project.
    -------------------------------------------------------------------------------
    Change Log:
    Who  When           What
    PJM  05.19.2025     Added blueprint for a main program.
    PJM  05.19.2025     Created class Testing, created comment block.
    -------------------------------------------------------------------------------
    """
    def main():
        DBManager.cur.execute("""
        select ROWID, main_monster
        from quests
        where user_id = ?;
        """, (663063684620353586))

        print(DBManager.cur.fetchall())

    if __name__ == "__main__":
        main()
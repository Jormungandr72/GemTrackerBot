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
    PJM  05.19.2025     Put some sql code in to test with.
    PJM  05.19.2025     Added blueprint for a main program.
    PJM  05.19.2025     Created class Testing, created comment block.
    -------------------------------------------------------------------------------
    """
    def main():
        DBManager.open_all()

        DBManager.cur.execute("""
        select ROWID, main_monster
        from quests
        where user_id = ?;
        """, (663063684620353586))

        print(DBManager.cur.fetchall())

        DBManager.close_all()

    if __name__ == "__main__":
        main()
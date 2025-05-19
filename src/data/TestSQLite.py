from sqlite3 import Connection, connect, Cursor

class TestSQLite:
    def main():
        # Open DB connections
        con = connect("src/data/db.sqlite3")
        cur =con.cursor()

        # Close DB connections
        cur.close()
        con.close()

    if __name__ == "__main__":
        main()
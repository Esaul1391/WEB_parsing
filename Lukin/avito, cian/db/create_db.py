import sqlite3

def main():
    connection = sqlite3.connect('realty.db')   # create connection with database
    cursor = connection.cursor()    # manage database
    cursor.execute("""
        CREATE TABLE offers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT,
        offer_id INTEGER,
        data TEXT,
        price INTEGER,
        address TEXT,
        area INTEGER,
        rooms TEXT,
        floor INTEGER,
        total_floor INTEGER
        )
    """)
    connection.close()

if __name__ == '__main__':
    main()
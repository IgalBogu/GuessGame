import sqlite3

sqlite_file = 'Scores.sqlite'  # name of the sqlite database file
Players = 'Players'  # name of the table to be created
firstName = 'FirstName'  # name of the column
Wins = 'Wins'  # name of the column
Looses = 'Looses'  # name of the column
field_type = 'Text'  # column data type


def create_connection(Scores_db):
    try:
        Done = False
        while not (firstName, Wins, Looses):
            Done = True

        # Connecting to the database file
        conn = sqlite3.connect(Scores_db)
        c = conn.cursor()

        # Creating a new SQLite table with 1 column
        c.execute('CREATE TABLE {tn} ({nf} {ft})'
                  .format(tn=Players, nf=firstName, ft=field_type))

        # Creating a new SQLite table with 1 column
        c.execute('CREATE TABLE {tn} ({nf} {ft})'
                  .format(tn=Wins, nf=Wins, ft=field_type))

        # Creating a new SQLite table with 1 column
        c.execute('CREATE TABLE {tn} ({nf} {ft})'
                  .format(tn=Looses, nf=Looses, ft=field_type))
    finally:
        return
    # Committing changes and closing the connection to the database file
    conn.commit()
    conn.close()
    return conn



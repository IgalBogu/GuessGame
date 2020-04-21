import string
import sqlite3


class Players:
    @staticmethod
    def addPlayerName():
        try:
            _userInput = input("Enter Player Name: ")

            if _userInput == "" or _userInput == "\n\f\r\t" or _userInput == string.whitespace or _userInput == '':
                return Players.addPlayerName()

            else:
                db_conn = sqlite3.connect('/Users/igal/PycharmProjects/GuessGame/Scores.db')
                c = db_conn.cursor()

                c.execute('''\
                    SELECT Players.FirstName,Wins.Wins,Looses.Looses
                    FROM Players
                    JOIN Wins ON Players.id = Wins.id
                    JOIN Looses ON Players.id = Looses.id
                    ''')

                data = c.fetchall()
                if data:
                    print(data)

                print(f"\nWelcome {_userInput}, We are Glad to see you here!")

                # Connecting to the database file
                db_conn = sqlite3.connect('/Users/igal/PycharmProjects/GuessGame/Scores.db')
                c = db_conn.cursor()

                c.execute("INSERT INTO Players (FirstName) VALUES(?)", (_userInput,))
                db_conn.commit()
                db_conn.close()
                return db_conn

        except ValueError as _valueError:
            print(_valueError)

        except KeyboardInterrupt as ki:
            print(ki)

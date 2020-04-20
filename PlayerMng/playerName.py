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
                conn = sqlite3.connect('Scores.sqlite')
                c = conn.cursor()
                with conn:
                    c.execute('''\
                    SELECT Players.FirstName,Wins.Wins,Looses.Looses
                    FROM Players
                    JOIN Wins ON Players.id = Wins.id
                    JOIN Looses ON Players.id = Looses.id
                    ''')
                    data = c.fetchall()
                    print("Players List")
                    print(data)

                    if data:
                        print(data)

                    print(f"\nWelcome {_userInput}, We are Glad to see you here!")

                    # Connecting to the database file
                    conn = sqlite3.connect('Scores.sqlite')
                    c = conn.cursor()

                    c.execute("INSERT INTO Players (FirstName) VALUES(?)", (_userInput,))
                    conn.commit()
                    conn.close()
                    return conn

        except ValueError as _valueError:
                print(_valueError)

        except KeyboardInterrupt as ki:
                print(ki)

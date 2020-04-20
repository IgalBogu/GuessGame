import random
import sqlite3
from FileOperation import Db_Select as select
from PlayerMng import playerName as pName


class Start:
    @staticmethod
    def startGame():

        print('Starting Game...')

        guess_count = 0
        guess_limit = 3
        secret_number = random.randint(0, 9)

        while guess_count < guess_limit:
            guess_count += 1
            try:
                user_input = int(input("Select Number: "))
                if user_input != "":
                    if user_input == secret_number:
                        conWin = sqlite3.connect('Scores.sqlite')

                        with conWin:
                            c = conWin.cursor()

                            print(f"""###########  Winning Number: {user_input} ###########""")
                            return conWin

                    elif user_input not in range(0, 10):
                        print("Select Only Number between 0 and 9 , Try Again! ")
                        return user_input

                    else:
                        if secret_number != user_input and guess_count == guess_limit:
                            print("""########## You Loose ##########""")

                            conLoose = sqlite3.connect('Scores.sqlite')
                            c = conLoose.cursor()

                            Wins = str(select.Wins())
                            Looses = str(select.Looses())

                            for win in c.fetchall():
                                print(win)

         #                   c.execute("INSERT INTO Wins (Wins) VALUES(?)", (win,))
          #                  c.execute("INSERT INTO Looses (Looses) VALUES(?)", (1,))

                            print(Wins)
                            print(Looses)

                            conLoose.commit()
                            conLoose.close()
                            return conLoose

            except ValueError:
                print("Select Only Number between 0 and 9 , Try Again! ")
                guess_count += -1
                return user_input

            except AssertionError:
                print("Please enter Digits only")
                guess_count += -1
                return user_input

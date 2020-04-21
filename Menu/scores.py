import sqlite3 as db
import sys
from Menu import start


class ScoreMenu:
    @staticmethod
    def scoreMenu(x):
        while True:
            print(''' 
                ############ Score Board #######
                    1 - My Scores
                    2 - All Players
                    3 - Top Score
                    4 - Top Looser
                    5 - Back to Main Menu
                    ''')
            try:
                command = input("> ").lower()

                if command == '1':
                    print("My Score ")
                elif command == '2':
                    _all = AllPlayers
                    _all.allPlayersResults()

                elif command == '3':
                    _top = topScore
                    _top.topPlayer()

                elif command == '4':
                    _loose = topLoose
                    _loose.topLoose()

                elif command == '5':
                    return

            except Exception as ex:
                print(ex)


class AllPlayers:
    @staticmethod
    def allPlayersResults():
        """Load all scores"""

        con = None
        try:
            con = db.connect('/Users/igal/PycharmProjects/GuessGame/Scores.db')
            cur = con.cursor()
            with con:
                cur.execute('''\
                            SELECT Players.FirstName, Wins.Wins, Looses.Looses
                            From Players
                            JOIN  Wins ON Players.id = Wins.id
                            JOIN  Looses ON Players.id = Looses.id
                            ''')

                data = cur.fetchall()
                for players in data:
                    print("Name: ", players)

        except db.Error as e:
            print("Error {}:".format(e.args[0]))
            sys.exit(1)

        finally:
            if con:
                con.close()


class topScore:
    @staticmethod
    def topPlayer():
        """Load top players scores"""
        conn = None
        try:
            conn = db.connect('/Users/igal/PycharmProjects/GuessGame/Scores.db')

            cur = conn.cursor()
            cur.execute('''\
                SELECT Players.FirstName, Wins.Wins, Looses.Looses
                From Players
                 JOIN Wins ON Players.id = Wins.id
                 JOIN Looses ON Players.id = Looses.id
                ORDER by Wins DESC
                        ''')
            data = cur.fetchone()
            print("Name: ", data[0], "\nWins: ", data[1], "\nLooses: ", data[2])

        except db.Error as e:
            print("Error {}:".format(e.args[0]))
            sys.exit(1)

        finally:
            if conn:
                conn.close()


class topLoose:
    @staticmethod
    def topLoose():
        """Load Top loose"""
        conn = None
        try:
            conn = db.connect('/Users/igal/PycharmProjects/GuessGame/Scores.db')

            cur = conn.cursor()
            cur.execute('''\
                SELECT Players.FirstName, Wins.Wins, Looses.Looses
                From Players
                 JOIN Wins ON Players.id = Wins.id
                 JOIN Looses ON Players.id = Looses.id
                ORDER by Wins ASC
                        ''')

            data = cur.fetchone()
            print("Name: ", data[0], "\nWins: ", data[1], "\nLooses", data[2])

        except db.Error as e:
            print("Error {}:".format(e.args[0]))
            sys.exit(1)

        finally:
            if conn:
                conn.close()

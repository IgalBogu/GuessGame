import logging
from FileOperation import DbConnection
from PlayerMng import playerName, playerSignOut
from Menu import start, help, quit, scores
from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():

    db = DbConnection
    db.create_connection('Scores.db')

    pName = playerName.Players
    pName.addPlayerName()

    while True:
        print(''' 
                    1 - Game instructions
                    2 - Start the game
                    3 - Load score
                    4 - Quit
                    5 - Sign Out''')
        try:
            command = input("> ").lower()

            if command == '1':
                h = help.Help
                print(h.gamehelp(help))

            elif command == '2':
                s = start.Start
                s.startGame()

            elif command == '3':
                os = scores.ScoreMenu
                os.scoreMenu(scores)

            elif command == '4':
                q = quit.Quit
                q.quitGame(quit)

            elif command == '5':
                signOut = playerSignOut.newPlayer
                signOut.newPlayer()

            else:
                print("Incorrect Selection")

        except Exception as ex:
            logging.exception(ex)
            print(ex)

        except ValueError as ve:
            print(ve)


if __name__ == "__main__":
    try:
        app.env = 'development'
        app.debug = True
        app.run()

    except KeyboardInterrupt:
        print('\nGame Interrupted...Quiting')

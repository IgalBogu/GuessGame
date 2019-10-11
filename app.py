import logging

import FileOperation.InitScoreBoard as initFile
import FileOperation.scores as openScores
from PlayerMng import playerName, playerSignOut
from Menu import start, help, quit

init = initFile.Init
init.createFile()


def main():
    print('''
            Welcome To the Guessing Game!
            May you're staying will be Pleasant!
            
            
            ''')

    playerName.addPlayerName()

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
                s.startGame(start)

            elif command == '3':
                os = openScores.LoadScores
                os.loadResults()

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
        main()
    except KeyboardInterrupt:
        print('\nGame Interrupted...Quiting')


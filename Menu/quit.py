import string
import sys

from Menu import start


class Quit:

    @staticmethod
    def quitGame(self):
        try:
            while True:
                yesChoice = ['YES', 'yes', 'Yes', 'yEs', 'yeS', 'YEs', 'yES', 'y', 'Y', 'ye', 'YE']
                noChoice = ['NO', 'no', 'No', 'nO', 'n', 'N']

                _user_input = input("Would you like to play again? (y/n) ").lower()

                if _user_input == "" or _user_input == "\n\f\r\t" or _user_input == string.whitespace \
                        or _user_input == '':
                    return

                elif _user_input in yesChoice:
                    print("\n")
                    restartGame = start.Start
                    restartGame.startGame(start)

                elif _user_input in noChoice:
                    print("\nOhh Please Be back soon!, Bye bye")
                    sys.exit(0)

                else:
                    return "Invalid input.\nExiting."
                    break

        except ValueError:
            return

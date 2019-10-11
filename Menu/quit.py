import sys

from Menu import start


class Quit:

    @staticmethod
    def quitGame(self):
        try:
            while True:
                yesChoice = ['YES', 'yes', 'Yes', 'yEs', 'yeS', 'YEs', 'yES', 'y', 'Y', 'ye', 'YE']
                noChoice = ['NO', 'no', 'No', 'nO', 'n', 'N']

                user_input = input("Would you like to play again? (y/n) ").lower()

                if user_input in yesChoice:
                    s = start.Start
                    s.startGame(start)
                elif user_input in noChoice:
                    print("\nOhh Please Be back soon!, Bye bye")
                    sys.exit(0)

                else:
                    print
                    "Invalid input.\nExiting."
                    break

        except ValueError:
            print("")

import json
import random


class Start():
    @staticmethod
    def startGame(self):
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
                        with open('scores.json', 'r+') as f:
                            data = json.load(f)
                            win_count = data["Wins"]
                            data["Wins"] = win_count + 1
                            f.seek(0)
                            json.dump(data, f, indent=4)
                            f.truncate()
                        print(f"""###########  Winning Number: {user_input} ###########""")
                        return user_input

                    elif user_input not in range(0, 10):
                        print("Select Only Number between 0 and 9 ")
                        print("Try Again")
                        return user_input

                    else:
                        if secret_number != user_input and guess_count == guess_limit:
                            with open('scores.json', 'r+') as f:
                                data = json.load(f)
                                loose_count = data["Looses"]
                                data["Looses"] = loose_count + 1
                                f.seek(0)
                                json.dump(data, f, indent=4)
                                f.truncate()
                            print("""########## You Loose ##########""")
                            return user_input

            except ValueError:
                print("Select Only Number between 0 and 9 ")
                print("Try Again")
                guess_count += -1
                return user_input

            except AssertionError:
                print("Please enter Digits only")
                guess_count += -1
                return user_input

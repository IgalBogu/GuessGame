import json
import string


def addPlayerName():
    try:
        _userInput = input("Enter Player Name: ")

        if _userInput == "" or _userInput == "\n\f\r\t" or _userInput == string.whitespace or _userInput == '':
            return addPlayerName()

        else:
            print(f"Welcome {_userInput}")
            with open('scores.json', 'r+') as f:
                data = json.load(f)
                data['Name'] = f"{_userInput}"  # <--- add `Name` value.
                f.seek(0)  # <--- should reset file position to the beginning.
                json.dump(data, f, indent=4)
                f.truncate()

    except ValueError as _valueError:
        print(_valueError)

    except KeyboardInterrupt as ki:
        print(ki)

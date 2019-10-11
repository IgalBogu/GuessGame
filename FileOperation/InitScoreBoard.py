from pathlib import Path
import json


class Init:

    @staticmethod
    def createFile():
        my_file = Path("scores.json")
        if not my_file.is_file():
            file = open(my_file, 'w+')
            jsonScheme = {
                "Name": "",
                "Wins": 0,
                "Looses": 0
            }
            jsonSchemeDump = json.dumps(jsonScheme, indent=4, skipkeys=True, ensure_ascii=True)
            file.write(jsonSchemeDump)
            file.close()
        else:
            return

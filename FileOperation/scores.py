from pathlib import Path
import json


class LoadScores:
    @staticmethod
    def loadResults():
        filePath = Path("scores.json")

        with open(filePath, 'r+') as f:
            scoreBoard = json.load(f)

        if filePath:
            name = scoreBoard["Name"]
            wins = scoreBoard["Wins"]
            looses = scoreBoard["Looses"]

            print(("Name: " + name))
            print(("Wins: " + str(wins)))
            print(("Looses: " + str(looses)))

            winRate = wins / 100
            looseRate = looses / 100
            totalWinRate = round((winRate / looseRate), 2)

            print(f"Win Rate: {totalWinRate}%")

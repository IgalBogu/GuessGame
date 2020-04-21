import sqlite3


def PlayerName():
    conn = sqlite3.connect('Scores.db')
    c = conn.cursor()
    with conn:
        _playerName = c.execute('Select * FROM Players WHERE id = (SELECT MAX(id) FROM Players)')
        return _playerName


def Wins():
    conn = sqlite3.connect('Scores.db')
    c = conn.cursor()
    with conn:
        _wins = c.execute('Select * FROM Wins WHERE id = (SELECT MAX(ID) FROM Wins)')
        return _wins


def Looses():
    conn = sqlite3.connect('Scores.db')
    c = conn.cursor()
    with conn:
        _looses = c.execute('Select * FROM Looses WHERE Id = (SELECT Max(ID) FROM Looses)')
        return _looses

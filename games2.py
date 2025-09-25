import json

games = None

with open("games.json", "r") as file:
    games = json.load(file)

print(games)

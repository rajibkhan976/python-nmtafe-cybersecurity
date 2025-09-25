# Lab 9 : Nested dictionaries
# (Support can be found at https://www.programiz.com/python-programming/nested-dictionary)
import json
games = {
    220860: {"name": "McPixel", "release date": "26 Sep 2012", "url": "https://store.steampowered.com/app/220860/McPixel/", "price": 6.99, "tags": ["Point & Click", "Comedy", "Indie", "Pixel Graphics"]},
    1605220: {"name": "Dune: Spice Wars", "release date": "26 Apr 2022", "url": "https://store.steampowered.com/app/1605220/Dune_Spice_Wars/", "price": 44.99, "tags": ["Economy", "Diplomacy", "Political", "Building", "4X"]},
    686200: {"name": "Door Kickers: Action Squad", "release date": "11 Sep 2018", "url": "https://store.steampowered.com/app/686200/Door_Kickers_Action_Squad/", "price": 19.95, "tags": ["Pixel Graphics", "Action", "Co-op", "Indie", "Tactical"]},
    250500: {"name": "Super Amazing Wagon Adventure", "release date": "16 Oct 2013", "url": "https://store.steampowered.com/app/250500/Super_Amazing_Wagon_Adventure/", "price": 4.50, "tags": ["Indie", "Action", "Action Rougelike", "Adventure", "2D"]},
    312660: {"name": "Sniper Elite 4", "release date": "14 Feb 2017", "url": "https://store.steampowered.com/app/312660/Sniper_Elite_4/", "price": 84.95, "tags": ["Sniper", "Action", "Multiplayer", "Shooter", "War"]},
    312530: {"name": "Duck Game", "release date": "5 Jun 2015", "url": "https://store.steampowered.com/app/312530/Duck_Game/", "price": 18.50, "tags": ["Multiplayer", "Funny", "Pixel Graphics", "Action", "2D"]},
    488790: {"name": "South Park™: The Fractured But Whole™", "release date": "18 Oct 2017", "url": "https://store.steampowered.com/app/488790/South_Park_The_Fractured_But_Whole/", "price": 89.95, "tags": ["RPG", "Comedy", "Dark Humor", "Funny", "Superhero"]},
    632360: {"name": "Risk of Rain 2", "release date": "18 Oct 2017", "url": "https://store.steampowered.com/app/632360/Risk_of_Rain_2/", "price": 35.95, "tags": ["Third-Person Shooter", "Action Rougelike", "Multiplayer"]},
    94400: {"name": "Nidhogg", "release date": "14 Jan 2014", "url": "https://store.steampowered.com/app/94400/Nidhogg/", "price": 14.50, "tags": ["Local Multiplayer", "Fighting", "Action", "PvP"]},
    1382330: {"name": "Persona® 5 Strikers", "release date": "23 Feb 2021", "url": "https://store.steampowered.com/app/1382330/Persona_5_Strikers/", "price": 99.95, "tags": ["Anime", "Great Soundtrack", "JRPG", "Hack and Slash"]},
    1817070: {"name": "Marvel’s Spider-Man Remastered", "release date": "12 Aug 2022", "url": "https://store.steampowered.com/app/1817070/Marvels_SpiderMan_Remastered/", "price": 94.95, "tags": ["Superhero", "Action", "Open World", "Singleplayer"]}
}

# Challenge 1: Print all game names using a loop
print("\n--- 1! ---")
counter = 0
for x in games.values():
    counter += 1
    print(f"Game {counter} is: {x['name']}")

# Challenge 2: Print only the games that cost less than 50 dollars
print("\n--- 2! ---")
for x in games.values():
    if x['price'] < 50:
        print(f"{x['name']} costs {x['price']} AUD.")

# Challenge 3: Print the details of the game with the ID 312530.
print("\n--- 3! ---")
for x, y in games.items():
    if x == 312530:
        print(f"Game {x} is: {y['name']}")
        print(f"It was released in: {y['release date']}")
        print(f"URL: {y['url']}")
        print(f"Price: {y['price']} AUD")
        for z in y['tags']:
            print(f"Tag: {z}")

# Challenge 4: Find and display all the games with the tag “Action”.
print("\n--- 4! ---")
for x, y in games.items():
    for z in y['tags']:
        if z == "Action":
            print(f"{y['name']} Tags: {y['tags']}")

# Challenge 5: Change the price of any game the user wishes to change to any value a user wants to input. Then display the information to confirm
# Ensure you preserve data types!
print("\n--- 5! ---")
gameId = input("Enter the ID of the game to set the new price for: ")
gameIdList = list(games.keys())
if gameId.isnumeric() and gameIdList.count(int(gameId)) > 0:
    newPrice = input("Enter the new price: ")
    if newPrice.isdigit() or (newPrice.split(".")[0].isdigit() and newPrice.split(".")[1].isdigit()):
        games[int(gameId)]["price"] = float(newPrice)
        print(
            f'The game: {games[int(gameId)]["name"]} now costs {games[int(gameId)]["price"]}')
    else:
        print("You enetered an invalid price.")
else:
    print("The ID of the game doesn't match!")


# Challenge 6: Save the data in JSON


file = open("games.json", "w")
json.dump(games, file, indent=1)
file.close()
print("Saved!")

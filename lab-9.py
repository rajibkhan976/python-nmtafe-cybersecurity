# Name: Rajib Hossain Khan
# Student ID: 20145454
# Version: 202009081123

translations = {
    "zero": "null",
    "one": "eins",
    "two": "zwei",
    "three": "drei",
    "four": "vier",
    "five": "funf",
    "six": "sechs",
    "seven": "sieben",
    "eight": "acht",
    "nine": "neun",
    "ten": "zehn"
}

translations.pop("zero")
translations.update({
    "twenty": "zwanzig",
    "twenty one": "ienundzwanzig"
})
print(translations)

for key, value in translations.items():
    print((key, value))

restaurants = ("Tayyabs", "Rasa", "Dishoom", "Xi' and impression", "Silk Road", "New Ming", "Trullo", "Manteca", "Ciao Bella")

restaurant_cuisine = {
    "Tayyabs": "Indian",
    "Rasa": "Indian",
    "Dishoom": "Indian",
    "Xi'an Impression": "Chinese",
    "Silk Road": "Chinese",
    "New Ming": "Chinese",
    "Trullo": "Italian",
    "Manteca": "Italian",
    "Ciao Bella": "Italian"
}

restaurant_prices = {
    "Tayyabs" : "£20-30",
    "Rasa" : "£15-25",
    "Dishoom" : "£20-30",
    "Xi' and impression" : "£15-25",
    "Silk Road" : "£15-25",
    "New Ming" : "£10-20",
    "Trullo" : "£30-40",
    "Manteca" : "£40-50",
    "Ciao Bella" : "£20-30",

}

restaurant_tube_stations = {
    "Tayyabs": "Whitechapel",
    "Rasa": "St. John's Wood",
    "Dishoom": "Covent Garden",
    "Xi'an Impression": "Highbury & Islington",
    "Silk Road": "London Bridge",
    "New Ming": "Abbey Wood",
    "Trullo": "Highbury & Islington",
    "Manteca": "Barbican",
    "Ciao Bella": "Tottenham Court Road"
}

def menu():
    print("Welcome to my London food guide!")
    print("1. List all restaurants")
    print("2. Select cuisine")
    print("3. Are times tough?")
    print("4. Feeling fancy?")
    usersInput = input("Enter your option here: ")
    if usersInput == "1":
        print(restaurants)
    if usersInput == "2":
        print(restaurants)
    if usersInput == "3":
        print(restaurants)
    if usersInput == "4":
        print(restaurants)
    else:
        print("That is not an option! Please select a number from the menu above :)")
    
restaurants = ("Tayyabs", "Rasa", "Dishoom", "Xi' and impression", "Silk Road", "New Ming", "Trullo", "Manteca", "Ciao Bella")

iterated_restuarants = []

for restaurant in restaurants:
    iterated_restuarants.append(restaurant)

restaurant_cuisine = {
    "Indian": ["Tayyabs", "Rasa", "Dishoom"],
    "Chinese": ["Xi'an Impression", "Silk Road", "New Ming"],
    "Italian": ["Trullo", "Manteca", "Ciao Bella"]
}

indian_restaurants = restaurant_cuisine["Indian"]
chinese_restaurants = restaurant_cuisine["Chinese"]
italian_restaurants = restaurant_cuisine["Italian"]

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

def getCuisine():
    print("Cuisines to choose from: Indian, Chinese, Italian")
    chooseCuisine = input("What cuisine are you feeling? Select 'Indian', 'Chinese' or 'Italian'. ")
    if chooseCuisine == "Indian":
        print("Indian restaurants:")
        return indian_restaurants
    elif chooseCuisine == "Chinese":
        print("Chinese restaurants:")
        return chinese_restaurants
    elif chooseCuisine == "Italian":
        print("Italian restaurants:")
        return italian_restaurants
    else:
        return "This is not an option! Please select from a cuisine listed above."


def getCheapest():
    cheapest_restaurants = []
    print("Here are the restaurants that you can spend under £30:")
    for restaurant, price in restaurant_prices.items():
        price_range = price.replace("£", "")
        price_values = price_range.split("-")
        min_price = int(price_values[0])
        if min_price < 30:
            cheapest_restaurants.append(restaurant + ": " + price)
    return cheapest_restaurants

def getFancy():
    fancy_restaurants = []
    for restaurant, price in restaurant_prices.items():
        price_range = price.replace("£", "")
        price_values = price_range.split("-")
        min_price = int(price_values[0])
        if min_price >= 30:
            fancy_restaurants.append(restaurant + ": " + price)
    return fancy_restaurants

def getLocation():
    for restaurant in restaurants:
        print(restaurant)
    chooseRestaurant = input("Which restaurant would you like to know the nearest tube station to? Please enter the exact name of the restaurant. ")
    return restaurant_tube_stations[chooseRestaurant]

def menu():
    print("Welcome to my London food guide!")
    print("1. List all restaurants")
    print("2. Select cuisine")
    print("3. Are times tough?")
    print("4. Feeling fancy?")
    print("5. Get nearest tube station to restaurant")
    usersInput = input("Enter your option here: ")
    if usersInput == "1":
        for restaurant in restaurants:
            print(restaurant)
    elif usersInput == "2":
        cuisine = getCuisine()
        if isinstance(cuisine, list):
            for restaurant in cuisine:
                print("- " + restaurant)
        else:
            print(cuisine)
    elif usersInput == "3":
        cheapest_restaurants = getCheapest()
        for restaurant in cheapest_restaurants:
            print(restaurant)
    elif usersInput == "4":
        fancy_restaurants = getFancy()
        for restaurant in fancy_restaurants:
            print(restaurant)
    elif usersInput == "5":
        print(getLocation())
    else:
        print("That is not an option! Please select a number from the menu above :)")
    menu()

menu()
    
# fruits = ["Apple", "Banana", "Orange", "Pear"]
# print(fruits)
# fruits.append("Watermelon")
# print(fruits)
# fruits[2] = "Mango"
# print(fruits)

# fruits = {
#     "1st Favorite": "Apple",
#     "2nd Favorite": "Banana",
#     "3rd Favorite": "Mango",
#     "4th Favorite": "Pear",
#     "5th Favorite": "Watermelon"
# }

# print(fruits["1st Favorite"])
# print(fruits.values())
# print(fruits.keys())

# fruits.pop("2nd Favorite")
# print(fruits)
# fruits["2nd Favourite"] = ("Kiwi")
# print(fruits)

def update_fruits():

    fruits = {
        "Apple": 50,
        "Banana": 100,
        "Mango": 25,
        "Pear": 30,
        "Watermelon" : 30
    }

    fruits_sold = {
        "Apple": 30,
        "Banana": 40,
        "Mango": 25,
        "Pear": 20,
        "Watermelon" : 10
    }
    fruits["Apple"] = fruits["Apple"] - fruits_sold["Apple"]
    fruits["Banana"] = fruits["Banana"] - fruits_sold["Banana"]
    fruits["Mango"] = fruits["Mango"] - fruits_sold["Mango"]
    fruits["Pear"] = fruits["Pear"] - fruits_sold["Pear"]
    fruits["Watermelon"] = fruits["Watermelon"] - fruits_sold["Watermelon"]

    print(fruits)

update_fruits()


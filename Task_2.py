# The Shopping List maker
# Task 1: Create a func that retrieve user input and add it to a list
# Task 2: Add a removable feature
# Task 3: Create a func that displays the list

def shoppingList_Add(*items):
    itemList = []
    for i in items:
        itemList.append(i)
    return itemList

def shoppingList_Removal(*items):
    itemList = []
    for i in items:
        itemList.remove(i)
    return itemList

def options():
    userInput = int(input())
    match userInput:
        case 1:
            addItem = shoppingList_Add(*list(map(str, input("Add an item:").split())))
            return addItem
        case 2: 
            removeItem = shoppingList_Add(*list(map(str, input("Add an item:").split())))
            return removeItem
        case _:
            return "invalid Option"
    

print("\t Shopping List\n1. Add Item(s)\n2. Remove Item(s)")

print("Enter the number to operate: ")

print(options())
# The Shopping List maker
# Task 1: Create a func that retrieve user input and add it to a list
# Task 2: Add a removable feature
# Task 3: Create a func that displays the list

itemList = []

def shoppingList_Add(*items):
    for i in items:
        itemList.append(i)
    return itemList

def shoppingList_Removal(*items):
    for i in items:
        itemList.remove(i)
    return itemList

def store():
    print("Do you wanna go shopping?")
    while True:      
        x = input("Continue? y/n")
        if x == "y":
            print("\n\tShopping List\n---------------------------------\n1. Check Bag\n2. Add Item(s)\n3. Remove Item(s)\n4. Exit")
            userInput = int(input("Give me a number"))
            match userInput:
                case 1:
                    if len(itemList) > 0:
                        for i in itemList:
                            print(i)                  
                    else:
                        print("Bag is empty")
                case 2:
                    addItem = shoppingList_Add(*list(map(str, input("Add an item:").split())))
                    print(addItem)
                case 3: 
                    removeItem = shoppingList_Removal(*list(map(str, input("remove an item:").split())))
                    print(removeItem) 
                case 4:
                    return "Have a nice day!"
                case _:
                    return "invalid option"
        elif x == "n":
            print("Goodbye!")
            break
            

print(store())
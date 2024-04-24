# The Calculator App

# Task 1: Create arthmetical funcs
# Task 2: Retrieve user input and arthmetic choice
# Task 3: Error handling

def addition(*num):
    add_res = 0
    for i in num:
        add_res += i
    return add_res

def subtraction(*num):
    sub_res = 0
    for i in num:
        sub_res -= i
    return sub_res

def multiplication(*num):
    mult_res = 1
    for i in num:
        mult_res *= i
    return mult_res

def division(*num):
    div_res = 1
    for i in num:
        div_res /= i
    return div_res

def options():
    while True:
        x = input("Do you wanna continue? y/n")
        if x == "n":
            break
        
        print("\t Calculator\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")

        print("Enter the number to operate: ")
        userChoice = int(input())

        match userChoice:
            case 1:
                sumRes = addition(*list(map(int, input("Your numbers: ").split()))) 
                return f"The sum is {sumRes}"

            case 2:
                diffRes = subtraction(*list(map(int, input("Your numbers: ").split())))
                return f"The difference is {diffRes}"
            
            case 3:
                prodRes = multiplication(*list(map(int, input("Your numbers: ").split())))
                return f"The product is {prodRes}"

            case 4:   
                try:
                    quoRes = division(*list(map(int, input("Your numbers: ").split())))
                    return f"The quotient is {quoRes}"
                except ZeroDivisionError:
                    print("Zero is not divisible") 
            
            case _:
                return "invalid option...."



print(options())
    

# The map() allows users to continously execute specified operations on each iterable value in the list
# try/catch is a statement that can handle errors
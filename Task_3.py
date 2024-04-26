# The Grade Analyzer

# Task 1: Create a func to calculate GPA
# Task 2: Create a func to find the highest and lowest grades listed
# Task 3: Create a feature that categorizes grade into its alphabetical counterpart

def gradeAvg(*grade):
    initialval = 0
    for i in grade:
        initialval += float(i)
    return initialval / len(grade)

def finder(*num):
    minGrade = num[0]
    maxGrade = num[0]

    for i in range(len(num)):
        if i <= minGrade:
            minGrade = num[i]
        if i >= maxGrade:
            maxGrade = num[i]
    return minGrade, maxGrade

def gradeConverter(*grade):
    # A = 100 - 90, B = 89 - 80, C = 79 -70, D = 69 - 60, F = 59 - 0

    for i in grade:
        if i <= 100 and i >= 90:
           print("A")
        elif i <= 89 and i >= 80:
            print("B")
        elif i <= 79 and i >= 70:
            print("C")
        elif i <= 69 and i >= 60:
            print("D")
        elif i <= 59 and i >= 0:
            print("F")
        
    

ex = gradeConverter(12, 35, 100, 50)
print(ex)
# The Quiz Game

# Task 1: Create a list of questions and answers
# Task 2: Create a func that quizzes the user and takes in their response
# Task 3: Score the quiz and provide feedback 

# questionListGernre "Math", "Animals", "Trends", "Programming
# answerList = 230, "Husky", "Anime", "Javascript"
                        
questionList = {
"What does 270 - 125 * 4 + 460 equal?" : "C",
"In the 2002 movie, \"Snow Dogs\", what dog breed were the cast?" : "B",
"What is the popular form of adaptation for manga?" : "D",
"What is the program language used with to add functionality to a webpage" : "B"
} # Allows for a cleaner implementation of provding questions(key) with its respective answer(value)

answerList = [["A. 540", "B. -230", "C. 230", "D. -540"],
              ["A. American Eskimo", "B. Husky", "C. Akita", "D. American Malamute"],
              ["A. Manwha", "B. Cartoon", "C. J-Drama", "D. Anime"],
              ["A. Java", "B. Javascipt", "C. C#", "D. C++"]]

def quizTime():
    score = 0
    answerNum = 1
    print("\tQuiz Time!\n-------------------------------------")
    for i in questionList:
        print(i)
        for a in answerList[answerNum -1]:
            print(a)
        userAnswer = input("Your answer: ").upper()
        if userAnswer in questionList.get(i): # Checking if the given input from user matches the key's value
            print("You are correct!\n")
            score += 25
        else:
            print("You are incorrect...\n")
        answerNum += 1   
    print(f"\tFinal Score: {score}")  
    print("\nYou know your stuff!" if score == 100 else "You did great!" if score == 75 else "You got half right" if score == 50 else "You could do better" if score == 25 else "Better luck next time..." )      
        

print(quizTime())
   
# The Fitness Tracker App

# Task 1: Create a func that logs activities and their duration
# Task 2: Create a func that provides the est. calories burned based on the activity and duration
# Task 3: Create a func that provides a summary

def activityLog():
    #Will a dict variable work for this assignment?
    activites = ["Swimming", "Dancing", "Biking"]
    duration = [30, 25, 20]
    return activites, duration

def burntCal():
    #Access the the activities and time in the prior function
    activities, duration = activityLog()
    totalCal = []
    for i in range(len(activities)):
       totalCal.append(duration[i] * 5)
    return totalCal

def activitysummary():
    activities, duration = activityLog()
    totalCal = burntCal()
    for i in range(len(activities)):
        print(f"Calories burnt by {activities[i]} are {totalCal[i]} in {duration[i]} minutes.")

activitysummary()
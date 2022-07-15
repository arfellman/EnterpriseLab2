#!/usr/bin/env python3

#Create a list
list = []

i = 0

#Gather 3 numbers to average from user
while(i < 3):
    usernum = int(input('Please enter a number: '))
    list.append(usernum)
    i += 1
#print(list)

#Function to take the average of our list
def Average(userinput):
    avg = sum(userinput) / len(userinput)
    return avg

average = Average(list)
print("The average of your list is: ", average)
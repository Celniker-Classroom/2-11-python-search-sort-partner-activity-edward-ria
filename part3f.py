from random import randint #This line imports the randint function from the random module. The randint function generates a random integer between two specified values

list = [] #name your list and make sure it is empty!
maxNumber = int(input("What is the biggest number that should be generated?")) #what the max number is for the random numbers
minNumber = int(input("What is the smallest number that should be able to be generated?")) #what the minimum number is for the random number range
numRange = int(input("How many numbers do you want to generate?")) #how big the list/how many numbers to genreate 
randomNumber = int(input("What number do you want to search for in the list?")) #user input number to search for
comparisons = 0 #initial comparisons
percentage = 0 #initial percent chance

# Generates a list of 5 or 10 random integers between 1 and 50 inclusive.
def genNumber():
    for num in range(numRange): #now puts numbers in range of the user input
        list.append(randint(minNumber,maxNumber)) #adds a number based on the minimum and maximum user input variable

# get the percent chance of finding the number within the list
if randomNumber < minNumber: # if the chosen number is smaller than the minimum number
    percentage = 0 #then there is a 0% chance of finding it within the list
elif randomNumber > maxNumber: # otherwise if the chosen number is bigger than the maximum number
    percentage = 0 # then there is a 0% chance of finding it within the list
else: # if the chosen number is between smallest/biggest number, then find the percentage
    possibleNums = (maxNumber - minNumber) + 1 #total numbers that will be on the list
    probMiss = (possibleNums - 1) / possibleNums #the chance that the number won't be picked in the first scan
    probFailure = probMiss ** numRange # the chance that the number won't even be found on the list
    percentage = round((1 - probFailure) * 100, 2) # using round function to find percentage


genNumber() #call the function
print("Generated List:",list) #print the list
print("") #paragraph for nice spacing/visual looks
print(randomNumber,"has a",percentage,"% chance to be found in the list")
print("Searching for number:",randomNumber) #searching for the random number in list
import time
time.sleep(3) #for dramatic effect 

if randomNumber in list:
    print("Number",randomNumber,"found in the list!") #if found
else:
    print("Number",randomNumber,"not found in the list.") #if not found
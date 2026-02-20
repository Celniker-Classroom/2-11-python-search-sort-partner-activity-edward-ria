from random import randint #This line imports the randint function from the random module. The randint function generates a random integer between two specified values


list = [] #name your list and make sure it is empty!
randomNumber = int(input("What number do you want to search for in the list?")) #user input number to search for
numRange = int(input("How many numbers do you want to generate?")) #how big the list/how many numbers to genreate
maxNumber = int(input("What is the biggest number that should be generated?")) #what the max number is for the random numbers
minNumber = int(input("What is the smallest number that should be able to be generated?"))
comparisons = 0 #initial comparisons
found = False

# Generates a list of 5 or 10 random integers between 1 and 50 inclusive.
def genNumber():
    for num in range(numRange): #for loop appends 5 numbers to your list, but make sure you name your variable
        list.append(randint(1,maxNumber)) #this adds a random number between 1-50 to the list


genNumber()
print("Generated List:",list) #print the list!
print("") #paragraph for nice spacing/visual looks
print("Searching for number:",randomNumber) #searching for the random number in list

if randomNumber in list:
    print("Number",randomNumber,"found in the list!") #if found
else:
    print("Number",randomNumber,"not found in the list.") #if not found
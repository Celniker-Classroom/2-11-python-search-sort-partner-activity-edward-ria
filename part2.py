from random import randint #This line imports the randint function from the random module. The randint function generates a random integer between two specified values


list = [] #name your list and make sure it is empty!
randomNumber = randint(1,50) #the random number that we want to search for in the list
comparisons = 0
found = False

# Generates a list of 5 or 10 random integers between 1 and 50 inclusive.
def genNumber():
    for num in range(10): #for loop appends 5 numbers to your list, but make sure you name your variable
        list.append(randint(1,50)) #this adds a random number between 1-50 to the list


genNumber()
print("Generated List:",list) #print the list!
print("") #paragraph for nice spacing/visual looks
print("Searching for number:",randomNumber) #searching for the random number in list

for numbers in list:  # Name your variable in the for loop
    comparisons += 1  # Increment the counter for each comparison
    if numbers == randomNumber:
        found = True  # Set found to True if the number is in the list
        print("Number",randomNumber,"found in the list after",comparisons,"comparisons!")
        break  # Exit the loop early if the number is found
    else:
        print("Number",randomNumber,"not found in the list after",comparisons,"comparisons!")
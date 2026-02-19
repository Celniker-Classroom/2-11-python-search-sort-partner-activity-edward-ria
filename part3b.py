from random import randint #This line imports the randint function from the random module. The randint function generates a random integer between two specified values


list = [] #name your list and make sure it is empty!

# Generates a list of 5 or 10 random integers between 1 and 50 inclusive.
def genNumber():
    for num in range(10): #for loop appends 5 numbers to your list, but make sure you name your variable
        list.append(randint(1,50)) #this adds a random number between 1-50 to the list


genNumber()
print("Generated List:",list) #print the list!
print("") #paragraph for nice spacing/visual looks
list.sort()
print("Sorted list:",list)
print("") # paragraph spacing
smallest = list[0]
print("The smallest value of the list is:",smallest)
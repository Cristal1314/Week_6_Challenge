#######################################Dictionaries###############################
# Dictionaries Practice #1
# Create a dictionary called fruits with the following key-value pairs:
# apple --> red
# banana --> yellow
# mango --> green
# cherry --> red
# watermelon --> green
# Display the dictionary on the screen.
fruits={"apple":"red" , 
        "banana": "yellow",
        "mango": "orange",
        "cherry": "red",
      "watermelon":"green"}
# Dictionaries Practice #1
# Create a dictionary called my_dict that stores the following information about a person:
my_dict = {"name":" Karen",
"surname": "Jurgens",
"occupation": "Journalist"
}


# The names of the keys and values must be equal to the ones indicated above.

#   Dictionaries Practice #2
# Use print to returns the second item of the list called points2, inside the following dictionary.
# If the value 300 were to change in the future, the code should work the same to return the value at that same position. To do this, you must refer to the names of the keys and/or indexes as appropriate.
# my_dict = {"values_1":{"v1":3,"v2":6},"points":{"points1":9,"points2":[10,300,15]}}
# print(my_dict[]) #Use dictionary indices to extract the second item of points2

# Dictionaries Practice #3
# Update the information in our dictionary called my_dict (reassigning new values to the keys as appropriate), and add a new key called "country" (without a tilde). The new data is:
# name: Karen
# surname: Jurgens
# age: 36
# occupation: Editor
# country: Colombia
# to do this, you should not change the line of code already written, but update the values using dictionary methods.
my_dict = {"name":"Karen", "surname":"Jurgens", "age":35, "occupation":"Journalist"}
my_dict.update({"age": 36,
                "occupation": "Editor",})
my_dict.update({"Country": "Colombia"})
################################Tuples##################################

# Tuples Practice #1
# Use a tuple method to count the number of times the value 2 appears in the following tuple, and display the result (integer) on the screen:

my_tuple = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(len("2" in my_tuple))
# Tuples Practice #2
# Convert the following tuple to a list, and store it in a variable called my_list.

my_list = [1, 2, 3, 2, 3, 1, 3, 2]

# Tuples Practice #3
# Extract the elements of the following tuple into four variables: a, b, c, d

my_tuple = (1, 2, 3, 4)
my_tuple.update({1:"a",
                 2: "b",
                 3: "c",
                 4: "d" })

###############################SETS########################################
# Sets Practice #1
# Join the following sets into one, called my_set_3:
# {1, 2, "three", "four"}
my_set_3 = {"1" , "2", "three", "four"}
# {"three", 4, 5}
my_set_1 = {1, 2, "three", "four"}

my_set_2 = {"three", 4, 5}

# Sets Practice #2
# Remove a random item from the following set, using set methods.
raffle = {"Rachel", "Monica", "Phoebe", "Joey", "Chandler", "Ross"}
print(raffle.pop())
# Sets Practice #3
# Add the name Gunther to the following set, using set methods:
raffle = {"Rachel", "Monica", "Phoebe", "Joey", "Chandler", "Ross"}
print(raffle.add("Gunther"))
###########################Booleans#######################################

# Booleans Practice #1
# Make a comparison that returns a boolean and store the result (True/False) in a variable called test
test = 
# Booleans Practice #2
# Check if 17834/34 is greater than 87*56 and print the boolean result to the screen using print()
if 17834/34 > 87*56
print ("yes slayyy")
else:
print("No booo go to math class 87*56 is greater ")
# Booleans Practice #3
# Check if the square root of 25 is equal to 5 and display the result (boolean) on the screen using print()

###############################Proceed to last slide#################################

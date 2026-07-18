#idea: 
#a fake and funny news generator program/app

#how it works: 
#1- there will be three list of words (subject, verb, object)
#2- one random word will be picked form each list
#3- those three words will be concatinated to form a funny sentence


#concepts used: 
#1- list concept of python, [] : to store the words in it
#2- random.choice() module: to pick the random words 
#3- while loop : to ask to user whether to continue or exit
#4- input() module : to take input form the user

#6- strip() : to remove extra space
#7- lower() : to convert strings into lowercase


#pesudocode: 
# ?




# step 1: import the 'random' module
import random 

# step 2: create lists to store words 
subject_list = [
    "PM", 
    "A cat", 
    "A bus driver", 
    "Rajesh Hamal",
    "My friend", 
    "A boy", 
    "A group of monkeys",
    "A car",
    "dog"
    
]

verb_list = [
    "eats",
    "fall from",
    "collided with",
    "dances with",
    "laughed at",
    "ran after",
    "is singing",
    "mimics",
    "rides"
]

object_list = [
    "samosa",
    "road",
    "river",
    "momo",
    "truck",
    "bike",
    "Singh Durbar",
    "Babar Mahal",
    "Tripureshwor"
    
]

while(1):
    subject = random.choice(subject_list)
    verb = random.choice(verb_list)
    object = random.choice(object_list)
    print (f" HEADLINE: {subject} {verb} {object} . ")
    
    choice = input("Do you want more ? (yes/no  or y/n ) ")
    real_choice = choice.strip().lower()
    if(real_choice == 'no' or real_choice == 'n'):
        break
    
print("Thank you for playing with us. Have a nice day!")





# Extend: -------------------------------------------------------

# Add category also 
# Get user perspective 
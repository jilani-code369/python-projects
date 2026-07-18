#PREREQUISITES: ---------------------------------------------------------------------------------

#idea: 
#password guessing game

#how it works:
#computer will generate a password but user don't know about it
#the user will guess the password
#if the password is wrong then it will say wrong
#if the initial letters are correct then it will give hint about how many more letter are their in the word
#if guessing is right then it will say in how many attempt the guessing become right

#concepts used:
# list [] : to store the words
# random() : to pick the random word to generate a passowrd secretely
# input() : to take user input
# while() loop : to run the program endlessly until the password is correct
#conditional statement(if-elif-else) : to check different conditions

#len(variable) : to conun the no of letter in a word 

#pseudocode: 
# 1- start 
# 2- create three lists of words(easy list, medium list and hard list)
# 3- take the user input for easy, midium and hard
# 4- run the if-elif-else conditional statement
#     if user choose easy:
#         use random() module and pick a random word from the easy list
#     elif user choose medium:
#         pick a random word form medium list
#     elif user chooe hard :
#         then pick a random word from the hard list
#     else (if user didn't choose any option):
#         choose the random word from the easy list as a default behaviour
     
# 5- set count=0
# 6- while(True):
#     a- use input() function and ask user to guess the password

#     b- run the if-elif-else conditional statement
    
#         if user guess == computer guess 
#              display "password is correct" and also display count
#              break the loop 
        
#         elif user guess != computer guess then:
#             i- increase the count 
#             ii- display "The password is incorrect"
     
#             iii- match the letter of input with the computer guess
#             iv- show the correct letter for the matching letters and _ _ _ for the unmatched letters


#CODE: ------------------------------------------------------------------------------------------
import random           # to choose random word form a list

easy_list = ['bat', 'man', 'pot', 'win', 'you']
medium_list = ['rain', 'glass', 'dinner', 'eagle', 'python']
hard_list = ['elephant', 'ambition', 'pneumonia', 'umbrella', 'psychology']

level = input("Enter the hardness level(easy, medium, hard) ").strip().lower()

if level == 'easy':
    password = random.choice(easy_list)
elif level == 'medium':
    password = random.choice(medium_list)
elif level== 'hard':
    password = random.choice(hard_list)
else:
    print("Defaulting to the easy level ")
    password = random.choice(easy_list) 
    
attempt = 1
while(True):
    guess = input(f"Enter the password. ").strip().lower()
    if guess == password:
        print("Congratulation! Your guess is correct. ")
        print("You guessed in ", attempt, "attempt. \n")
        break
        
    attempt+=1
    print("Wrong password! See the hint below. ")
   
   #logic to give hint
    hint = ""
    for i in range(len(password)):
        if i<len(guess) and guess[i]==password[i]:
            hint+=guess[i]
        else:
            hint+="_ "
    print(f"Hint(length:{len(password)}): ", hint)
    print("\n")
        
        
        
    
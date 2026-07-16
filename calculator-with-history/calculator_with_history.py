#PREREQUISITES:---------------------------------------------------------------------------

#idea: 
#to create a calculator that perform arithmetic calculation and saves the history as well 

#how it works: 
#1- it takes input from the user as: number, operator, number
#2. it perform the arithmetic calculation and show the result 
#3. it saves the result in the file
#4. it display the content of the file when user want to see the history

#concepts used: 
#1- file handling concepts of python : to save history in the file
#2- funtion concept : to create saperate function for saperate tasks 
#3- while loop : to ask input form the user until user exits
#4- input() function : to take input from the user
#5- conditional statement (if..elif...else) : to check different conditons to perform calculation
#6- arithmetic operators(+, -, *, /) :  to perform calculations
#7- split() function : to split user input to separate numbers and operators

#pseudocode: 
#1- start the program
#2- define the name of the history file eg: HISTORY.txt
#3- loop forever (while true)
    #a- ask user to enter expression(like: 4+3) or commands (history, clear, exit)
    
    #b- if user enter 'exit'
        #i- print goodbye message
        #ii- break the loop
        
    #c- if user enter 'history'
        #i- try to open the HISTORY.txt file for reading
        #ii- if file exists and is not empty then print the content of the file
        #iii- if file doesn't exist or is empty then print "No history found"
        #iv- continue to the next loop     
        
    #d- if user enter 'clear'
        #i- open the file HISTORY.txt file and overwrite it with nothing 
        #ii- print "History is cleared."
        #iii- continue to the next loop
        
    #e- otherwise (if user typed calculation and hit enter)
        #i- try to parse input to get number and operator
        #ii- if input is not valid then print "Invalid input and contitue the loop"
        #iii- performt the calculation using if..elif..else
            #if + then add
            #if - then subtract
            #if * then multiply
            #if / then divide
        #iv- show the result to the user
        #v- write the calculation and result to the HISTORY.txt file to save the history
        
#4- end the program.





#CODE: ---------------------------------------------------------------------------------

#history.txt file: 
HISTORY_FILE = "history.txt"


#clear_history() function
def clear_history():
    file = open(HISTORY_FILE, 'w')             # opening file in writing automatically wipe out all the content of the file and make it empty
    file.close()
    print("Your history is cleared.")
    
    
#show_history() function:
def show_history():
    file = open(HISTORY_FILE, 'r')
    lines = file.readlines()
    if len(lines) == 0:
        print("File is empty")
    else: 
        for line in lines:
            print(line.strip())
    
    file.close()                # closing the file
        
        
#save_to_history()
def save_to_history(equation, result):
    file = open(HISTORY_FILE, 'a')
    file.write(equation + "=" + str(result) + "\n")     # str(result) : typecasting is done bec result is an integer and it need to be a string to concatinate with other strings
    file.close()



#calculate() function:
def calculate(user_input):
    parts = user_input.split()
    if len(parts) !=3:
        print("Invalid format. Enter number, operator, number ")
        return                           # return is used here bec the program terminates when return is encountered
    
    num1= float(parts[0])
    op = parts[1]
    num2 = float(parts[2])
    

    if op == "+":
        result = num1+num2
    
    elif op == "-":
        result = num1-num2
        
    elif op == "*":
        result = num1*num2
        
    elif op == "/":
        if num2==0:
            print("Cannot divide by zero!")
            return
        result = num1/num2
    
    else:
        print("Invalid operator")
        return
        
    
    print("Result:", result)
    
    
    #save result to history file
    save_to_history(user_input, result)
   
        


#main() function:
def main():
    while(True):
        user_input = input("Enter equation or command (history, clear, exit )")
    
        if user_input == "exit":
            print("Goodbye! ")    
            break
        elif user_input == "clear":
            clear_history()
        elif user_input == "history":
            show_history()
        else:
            calculate(user_input)
        
        

#call main() function
main()
    

    
    
# HISTORY_FILE = 'history.txt'

# def show_history():
#     file = open(HISTORY_FILE, 'r')
#     lines = file.readlines()
#     if len(lines) == 0:
#         print("No history found")
#     file.close()
    
# def clear_history():
#     file = open(HISTORY_FILE, 'w')
#     file.close()
#     print("History cleared!")
    
# def save_to_history(equation, result):
#     file = open(HISTORY_FILE, 'a')
#     file.write(equation + "=" + str(result) + "\n")
#     file.close()
    
# def calculate(user_input):
#     parts = user_input.split()
#     if len(parts)!=3:
#         print("Invalid input. User proper format: number, operator, number (eg: 8+8) ")
#         return
#     num1 = float(parts[0])
#     op = parts[1]
#     num2 = float(parts[2])

#     if op == "+":
#         result = num1 + num2
    
#     elif op == "-":
#         result = num1 - num2
        
#     elif op == "*":
#         result = num1 * num2
        
#     elif op == "/":
#         if num2== 0:
#             print("Cannot divide by zero.")
#             return
#         result = num1 + num2
    
#     else: 
#         print("Invalid operator. Only usr +, _, *, /")
#         return
    
#     if int(result) == result:
#         result = int(result)
        
#     print("Result, result")
#     save_to_history(user_input, result)
    
    
# def main():
#     while True:
#         user_input = input("Enter calculation or command (history, clear, exit) ")
#         if user_input == 'exit':
#             print("Goodbye!")
#             break
#         elif user_input == 'history':
#             show_history()
#         elif user_input == 'clear':
#             clear_history()
#         else:
#             calculate(user_input)
            
# main()
    
    
    
    
#EXTENDS: -----------------------------------------------------------------------------
#also implement % (modulus) and ** (exponent)
#make it support more that two digits 

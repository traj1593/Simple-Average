'''
Program: Simple Average
Filename: simpleAverage-tRaj-00.py
Author: Tushar Raj
Description: calculate the average of a sequence of numbers
Revisions: No revisions made
'''
#There is no import statement
#There are no literal constraint
#There are no class defined

def inputdata(number,usecase): #checks the user input is correct
    '''
    This function accepts the input from the user and checks if the value contains any special character,alphabets.It even checks that the value is not negative for the number of sequence
    Input: user input from the console which is string type
    output: returns converted strings into float/int data type
    '''
    count = 1
    special = "!@#$%^&*()+?_=,<>/"
    alphabet = "QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm"
    while(count):
        if(any( i in alphabet for i in number)): #checks if the value entered in number variable is having any character or not
            print("****Entered value can not have characters****\n") #prints the error message
            progress = input("Please enter if you want to continue with computation of Simple Average(y/n): ") #ask users if he wants to continue with program
            if( progress == 'y' or progress == 'Y' ):#checks the response of the user if its yes, asks to enter the diameter again
                number = input("\nTry entering the last value again: ")
            if( progress == 'n' or progress == 'N' ):#exits the program if response in no
                exit()
            continue
        elif (any( i in special for i in number)): #picks up each character from the number variable and then checks in special variable if it is present, if present run this elif
            print("****Input cant have special character. Please Enter the valid entry****\n")
            progress = input("Please enter if you want to continue with computation of Simple Average(y/n): ")
            if( progress == 'y' or progress == 'Y' ):
                number = input("\nTry entering the last value again: ")
            if( progress == 'n' or progress == 'N' ):
                exit()
            continue
        elif(float(number) <=  0 and usecase == "sequence"): #checks if the entered user input is negative
            print("****Please Enter the valid sequence number for which you need avergae(greater than 0)****\n")
            progress = input("Please enter if you want to continue with computation of Simple Average(y/n): ")
            if( progress == 'y' or progress == 'Y' ):
                number = input("\nTry entering the last value again: ")
            if( progress == 'n' or progress == 'N' ):
                exit()
            continue
        else:
            if(usecase == "data"):
                converted_number = float(number)
                return converted_number
            elif(float(number) > 0 and usecase == "sequence"):
                converted_number = int(number)
                return converted_number


### Step 1: Announce, prompt and get Response
print("Simple Average:")
print("Program to compute the average of the numbers provided.\n")

#Main Program starts here
#Prompt user to get the number of input for average
sequence_value = input("How many numbers would you like to average? ")
converted_sequence_value = inputdata(sequence_value,"sequence") #check the user input if its a valid entry by calling the inputdata function

#Prompt user to get the number for average
addition = 0
for i in range(converted_sequence_value):
    print("Enter number {}: ".format((i+1)), end = "")
    user_input=input() #asking user for the user input
    number = inputdata(user_input,"data") #checking if the user input is valid or not
    addition += number #adding all the user input

###Step 2: Calculate the simple average
simple_average = addition/converted_sequence_value

###Step 3: print the result
print("\nThe average is {0}.".format(simple_average))
print("\n****Simple Average program ended ****")


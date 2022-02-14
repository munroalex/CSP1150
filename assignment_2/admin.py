# Name:  
# Student Number:  

# This file is provided to you as a starting point for the "admin.py" program of the Project
# of Programming Principles in Semester 1, 2022.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis of your work.
# You are not required to reference it.

# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter file runs smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the necessary module(s).
import json


# This function repeatedly prompts for input until an integer of at least 1 is entered.
# See Point 1 of the "Functions in admin.py" section of the assignment brief.
def input_int(prompt):
    pass



# This function repeatedly prompts for input until something other than whitespace is entered.
# See Point 2 of the "Functions in admin.py" section of the assignment brief.
def input_something(prompt):
    pass



# This function opens "data.txt" in write mode and writes data_list to it in JSON format.
# See Point 3 of the "Functions in admin.py" section of the assignment brief.
def save_data(data_list):
    pass



# Here is where you attempt to open data.txt and read the data into a "data" variable.
# If the file does not exist or does not contain JSON data, set "data" to an empty list instead.
# This is the only time that the program should need to read anything from the file.
# See Point 1 of the "Requirements of admin.py" section of the assignment brief.



# Print welcome message, then enter the endless loop which prompts the user for a choice.
# See Point 2 of the "Requirements of admin.py" section of the assignment brief.
# The rest is up to you.
print('Welcome to the "Quote Catalogue" Admin Program.')

while True:
    print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
    choice = input('> ').lower() 
        
    if choice == 'a':
        # Add a new quote.
        # See Point 3 of the "Requirements of admin.py" section of the assignment brief.
        pass


    
    elif choice == 'l':
        # List the current quotes.
        # See Point 4 of the "Requirements of admin.py" section of the assignment brief.
        pass



    elif choice == 's':
        # Search the current quotes.
        # See Point 5 of the "Requirements of admin.py" section of the assignment brief.
        pass



    elif choice == 'v':
        # View a quote.
        # See Point 6 of the "Requirements of admin.py" section of the assignment brief.
        pass

        

    elif choice == 'd':
        # Delete a quote.
        # See Point 7 of the "Requirements of admin.py" section of the assignment brief.
        pass

        

    elif choice == 'q':
        # End the program.
        # See Point 8 of the "Requirements of admin.py" section of the assignment brief.
        pass



    else:
        # Print "invalid choice" message.
        # See Point 9 of the "Requirements of admin.py" section of the assignment brief.
        pass



# If you have been paid to write this program, please delete this comment.

# Date - 20/04/2023
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# UoW Student ID - w1998725
# IIT student ID - 20221110
# Name- Janeesha Fernando

# Program to predict progression outcomes at the end of the academic year.

# Initializations of integer variables 'progress', 'trailer', 'exclude' and 'retriever' which are used to count the number of outcomes.
progress = 0
progress = 0
trailer = 0
exclude = 0
retriever = 0

# This dictionary is used to store the progress outcomes.
progress_outcome = {}

# The code defines different Unicode characters that are used in drawing the corners and lines of a box.
# Stack Overflow (2010).Box drawing in python[Source code].https://stackoverflow.com/questions/664991/box-drawing-in-python.
top_left_corner = "\u2554"
top_right_corner = "\u2557"
horizontal = "\u2550"
vertical = "\u2551"
bottom_left_corner = "\u255A"
bottom_right_corner = "\u255D"

print(top_left_corner+horizontal*80+top_right_corner)
print(vertical+"             P R O G R E S S I O N   O U T C O M E S  P R O G R A M             "+vertical)
print(bottom_left_corner+horizontal*80+bottom_right_corner)
print()

#credit_range is a list representing the range of credit scores from 0-120 
credit_range = range(0,121,20)

# This function to validate user type.
def is_total_incorrect(credit_pass,credit_defer,credit_fail):
    total_credits = credit_pass+credit_defer+credit_fail  
    if total_credits != 120:
        print("Total incorrect.\n")
        return False
    return True

# This function validates a given UoW number to check if it is valid or not.
def validate_uow(uow_no):
    if uow_no[0].lower() != 'w': # check first character is w or not
        return False
    if len(uow_no) != 8: # check number of characters = 8
        return False
    if not uow_no[1:].isdigit(): # check remaining characters are digits or not
        return False
    return True

# While run_again is true the code within the loop will execute repeatedly.
run_again="y"

while True:

    # Initializes an empty dictionary to store the output of
    outcome={}

    # Prompt the user to enter their UoW number in the format wXXXXXXX.
    uow_no = input("Please enter your UoW number (wXXXXXXX): ")

    
    # Check if 'uow_no' exists as a key in 'progress_outcome'. 
    if uow_no in progress_outcome.keys():
        print("Already exist")
        continue
    
    # Check if the UoW number is valid and print it to the console.
    if validate_uow(uow_no):
        print("\n")
        print("UoW No:",uow_no)
        print("\n")

    else:
        print("Invalid format. Please try again (wXXXXXXX).")
        print("\n")
        continue    


    try:       
        # Takes an integer input of "credits at pass" from the user and stores it in a variable called credit_pass.
        credit_pass = int(input("Enter your total PASS credits: "))

        # Checks if the input credit_pass is in the credit range. 
        if credit_pass not in credit_range:
            print("Out of range\n")
            continue
        
        # Takes an integer input of "credits at defer" from the user and stores it in a variable called credit_defer.
        credit_defer = int(input("Enter your total DEFER credits: "))

        # Checks if the input credit_defer is in the credit range. 
        if credit_defer not in credit_range:
            print("Out of range\n")
            continue

        # Takes an integer input of "credits at fail" from the user and stores it in a variable called credit_fail.
        credit_fail = int(input("Enter your total FAIL credits: "))
        
        # Checks if the input credit_fail is invalid.
        if credit_fail not in credit_range:
            print("Out of range\n")
            continue
                
    # If a ValueError is raised, the message "Integer Required." will be printed on the console.
    except ValueError:
        print("Integer required.\n")
        continue
        
    #Calling the function to check whether the total credits are correct.
    if not is_total_incorrect(credit_pass,credit_defer,credit_fail):
        continue
        
    # Adding outcomes as key/value pair in progress_outcome dictionary.
    if (credit_pass == 120):
        print("Progress")
        outcome= {uow_no: f"Progress - {credit_pass}, {credit_defer}, {credit_fail}"}
        progress_outcome.update(outcome)
        progress += 1
        
    elif (credit_pass == 100):
        print("Progress (module trailer)")
        outcome= {uow_no: f"Progress (module trailer) - {credit_pass}, {credit_defer}, {credit_fail}"}
        progress_outcome.update(outcome)
        trailer += 1

    elif(credit_fail <= 60):
        print("Do not progress – module retriever")
        outcome= {uow_no: f"Progress (module retriever) - {credit_pass}, {credit_defer}, {credit_fail}"}
        progress_outcome.update(outcome)
        retriever += 1
    
    elif (credit_fail >= 80):
        print("Exclude") 
        outcome= {uow_no: f"Exclude - {credit_pass}, {credit_defer}, {credit_fail}"}
        progress_outcome.update(outcome)
        exclude += 1 

    while True:
        print("\n")
        print("Would you like to enter another set of data? " )
        run_again = str(input("Enter 'y' for yes or 'q' to quit and view results :"))
        print("\n")
        if run_again == "y": 
            break   
    
        elif run_again == "q":  
            print("---------------------------------------------------------------------------------------------------------------------------------------------------------")  
            # Loop through progress_outcome dictionary and print each key value pairs.
            print("\n")
            print(top_left_corner+horizontal*86+top_right_corner)
            print(vertical+"             P R O G R E S S I O N   O U T C O M E S  D I C T I O N A R Y             "+vertical)
            print(bottom_left_corner+horizontal*86+bottom_right_corner)
            print("\n")

            for (key,value) in progress_outcome.items():               
                print(key,":",value,"\n")                                  
            
        else:
            print("Invalid Input")
    


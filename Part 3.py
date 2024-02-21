# Date - 20/04/2023
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# UoW Student ID - w1998725
# IIT student ID - 20221110
# Name- Janeesha Fernando

# Part 3 - Text File

# Initializations of integer variables 'progress', 'trailer', 'exclude' and 'retriever' which are used to count the number of outcomes.
progress = 0
trailer = 0
exclude = 0
retriever = 0

# Initializing four counts to keep track of progress, trailers, exclusions and retrievals.
progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0

# Creating a list to store all the progress data.
progress_list = []

# Creating a list to store all the module trailer data.
trailer_list = []

# Creating a list to store all the  module retriever data.
retriever_list = []

# Creating a list to store all the exclude data.
exclude_list = []

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
        print("Total incorrect.")
        print("\n")
        return False
    return True

# While run_again is true the code within the loop will execute repeatedly.
run_again="y"

while True:
    try:
        # Takes an integer input of "credits at pass" from the user and stores it in a variable called credit_pass.
        credit_pass = int(input("Enter your total PASS credits: "))

        # Checks if the input credit_pass is in the credit range. 
        if credit_pass not in credit_range:
            print("Out of range")
            print("\n")
            continue
            
        # Takes an integer input of "credits at defer" from the user and stores it in a variable called credit_defer.
        credit_defer = int(input("Enter your total DEFER credits: "))

        # Checks if the input credit_defer is in the credit range. 
        if credit_defer not in credit_range:
            print("Out of range")
            print("\n")
            continue

        # Takes an integer input of "credits at fail" from the user and stores it in a variable called credit_fail.
        credit_fail = int(input("Enter your total FAIL credits: "))
       
        # Checks if the input credit_fail is invalid.
        if credit_fail not in credit_range:
            print("Out of range")
            print("\n")
            continue
            
    # If a ValueError is raised, the message "Integer Required." will be printed on the console.
    except ValueError:
        print("Integer required.")
        print("\n")
        continue
    
    #Calling the function to check whether the total credits are correct.
    if not is_total_incorrect(credit_pass,credit_defer,credit_fail):
        continue

    # Check if the student meets the requirements for Progress.
    if (credit_pass == 120):
        print("Progress")

        progress_list.append(credit_pass)   # Adding credits at pass to the progress list.
        progress_list.append(credit_defer)  # Adding credits at defer to the progress list.
        progress_list.append(credit_fail)   # Adding credits at fail to the progress list.
        
        # Write the progression list to the  progression data text file. 
        with open('progression data.txt', 'a') as fp:
            progress_string = ', '.join(str(item) for item in progress_list)
            fp.write("\nProgression - " + progress_string)
            progress_list.clear()

    elif (credit_pass == 100):
        print("Progress (module trailer)")

        trailer_list.append(credit_pass)   #Adding credit at pass to the trailer list.
        trailer_list.append(credit_defer)  #Adding credit at defer to the trailer list.
        trailer_list.append(credit_fail)   #Adding credit at fail to the trailer list.
       
        # Write the module trailer list to the progression data text file. 
        with open('progression data.txt', 'a') as fp:
            progress_string = ', '.join(str(item) for item in trailer_list)
            fp.write("\nProgress (module trailer) - " + progress_string)
            trailer_list.clear()
    
    elif(credit_fail <= 60):
        print("Do not progress – module retriever")

        retriever_list.append(credit_pass)   #Adding credit at pass to the retriever list.
        retriever_list.append(credit_defer)  #Adding credit at defer to the retriever list.
        retriever_list.append(credit_fail)   #Adding credit at fail to the retriever list.

        # Write the module retriever list to the progression data text file. 
        with open('progression data.txt', 'a') as fp:
            progress_string = ', '.join(str(item) for item in retriever_list)
            fp.write("\nDo not progress (module retriever) - " + progress_string)
            retriever_list.clear()

    elif (credit_fail >= 80):
        print("Exclude") 
      
        exclude_list.append(credit_pass)    #Adding credit at pass to the exclude list.
        exclude_list.append(credit_defer)   #Adding credit at defer to the exclude list.
        exclude_list.append(credit_fail)    #Adding credit at fail to the exclude list.

        # Write the exclude list to the progression data text file. 
        with open('progression data.txt', 'a') as fp:
            progress_string = ', '.join(str(item) for item in exclude_list)
            fp.write("\nExclude - " + progress_string)
            exclude_list.clear()
    
    while True:
        print("\n")
        print("Would you like to enter another set of data? " )
        run_again = str(input("Enter 'y' for yes or 'q' to quit and save the result: "))
        print("\n")
        if run_again.lower() == "y": 
            break   
            
        elif run_again.lower() == "q":  
           # Saving all the records in the text file.                  
            print("Records have been saved.\n") 
            
            print("Do you want to access the saved records or exit the program ?\n")
            while True:
                #Getting user input for display the results or exit the program.
                display_records = input("Please enter 'r' to display the records or enter 'e' to exit the program: ") 
                
                #Validation for the user input.
                if display_records != "r" and display_records != "e":
                    print("\n")
                    print("Invalid input please enter 'r' to display the records or 'e' to exit the program.\n")
                    continue 
                # Exiting the program.
                elif display_records == "e":
                    print()
                    print("Thankyou for using the program.")
                    quit() #End of the program.  
                else:
                    print()
                    print(top_left_corner+horizontal*79+top_right_corner)
                    print(vertical+"             P R O G R E S S I O N   O U T C O M E S  R E C O R D S            "+vertical)
                    print(bottom_left_corner+horizontal*79+bottom_right_corner)
                    print()

                    # Accessing the saved records in the text file.
                    f=open('progression data.txt','r')   
                    lines = f.readlines()
                    for line in lines:
                        print(line)
                    f.close()
                    print()
                   
                                              
        else:
             print("Invalid input please enter 'y' for yes and 'q' to quit the program and save the result.")
        print()     
        print("----------------------------------------------------------------------------------------------------------------------------")     
        print()
        

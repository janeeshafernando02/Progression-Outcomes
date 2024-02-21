# Date - 20/04/2023
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# UoW Student ID - w1998725
# IIT student ID - 20221110
# Name- Janeesha Fernando

# Part 1 and Part 2 - Student and Staff Version

# The code defines different Unicode characters that are used in drawing the corners and lines of a box.
# Stack Overflow (2010).Box drawing in python[Source code].https://stackoverflow.com/questions/664991/box-drawing-in-python.
top_left_corner = "\u2554"
top_right_corner = "\u2557"
horizontal = "\u2550"
vertical = "\u2551"
bottom_left_corner = "\u255A"
bottom_right_corner = "\u255D"

print(top_left_corner+horizontal*115+top_right_corner)
print(vertical+"             P R O G R E S S I O N   O U T C O M E S  : S T U D E N T   &   S T A F F   V E R S I O N              "+vertical)
print(bottom_left_corner+horizontal*115+bottom_right_corner)
print()

#credit_range is a list representing the range of credit scores from 0-120 
credit_range = range(0,121,20)

# This function check whether the total is correct.
def is_total_incorrect(credit_pass,credit_defer,credit_fail):
    total_credits = credit_pass+credit_defer+credit_fail  
    if total_credits != 120:
        print("Total incorrect.")
        return False
    return True

#This function checks the progression outcome of the student.
def calculate_progression_Outcome(credit_pass,credit_fail):
    if (credit_pass == 120):
        print("Progress")

    elif (credit_pass == 100):   
        print("Progress (module trailer)")

    elif(credit_fail <= 60):   
        print("Do not progress – module retriever")

    elif (credit_fail >= 80):    
        print("Exclude") 

# Students Version
def student():
     print("\n")
     #Prompting the user for the range of credits achieved at pass,defer and fail levels.
     while True: 
        try:
            credit_pass = int(input("Please enter your credits at pass: "))

            if credit_pass not in credit_range:
                print("Out of range\n")
                continue
            
            credit_defer = int(input("Please enter your credit at defer: "))

            if credit_defer not in credit_range:
                print("Out of range\n")
                continue
                
            credit_fail = int(input("Please enter your credit at fail: "))
                
            if credit_fail not in credit_range:
                print("Out of range\n")
                continue
            
        except ValueError:
                print("Integer required.\n")
                print("\n")
                continue    
        
        #Calling the function to check whether the total credits are correct.
        if not is_total_incorrect(credit_pass,credit_defer,credit_fail):
                print("\n")
                continue

        #Calling the function to check the progression of the student.    
        calculate_progression_Outcome(credit_pass,credit_fail)
        print("\n")
        quit("Thankyou for using the program.")  #End of the program.

#Staff Version
def staff():

    # Initializations variables 'progress', 'trailer', 'exclude' and 'retriever' which are used to count the number of outcomes.
    progress = 0
    trailer = 0
    exclude = 0
    retriever = 0

    # Creating a list to store all the progress data.
    progress_list = []

    # Creating a list to store all the module trailer data.
    trailer_list = []

    # Creating a list to store all the  module retriever data.
    retriever_list = []

    # Creating a list to store all the exclude data.
    exclude_list = []

    # Initializing four counts to keep track of progress, trailers, exclusions and retrievals.
    progress_count = 0
    trailer_count = 0
    retriever_count = 0
    exclude_count = 0

    while True:
        print("\n")
        try:
            #Prompting the user for the range of credits achieved at pass,defer and fail levels. 
             credit_pass = int(input("Enter your total PASS credits: "))

             if credit_pass not in credit_range:
                print("Out of range\n")
                continue
            
             credit_defer = int(input("Enter your total DEFER credits: "))

             if credit_defer not in credit_range:
                print("Out of range\n")
                continue
                
             credit_fail = int(input("Enter your total FAIL credits: "))
                
             if credit_fail not in credit_range:
                 print("Out of range\n")
                 continue
            
        except ValueError:
             print("Integer required.\n")
             continue 
       
        #Calling the function to check whether the total credits are correct.
        if not is_total_incorrect(credit_pass,credit_defer,credit_fail):
                continue

        # Check if the student meets the requirements for Progress.
        if (credit_pass == 120):
            # If the condition is true then output "Progress"
             print("Progress")

             progress_list.append(credit_pass)   # Adding credits at pass to the progress list.
             progress_list.append(credit_defer)  # Adding credits at defer to the progress list.
             progress_list.append(credit_fail)   # Adding credits at fail to the progress list.
                
             # Progress count 
             progress += 1

            # Check if the student meets the requirements for Progress (module trailer).    
        elif (credit_pass == 100):
                
            # If the condition is true then output "Progress (module trailer)"
             print("Progress (module trailer)")

             trailer_list.append(credit_pass)   #Adding credit at pass to the trailer list.
             trailer_list.append(credit_defer)  #Adding credit at defer to the trailer list.
             trailer_list.append(credit_fail)   #Adding credit at fail to the trailer list.
            
            # Module trailer count
             trailer += 1

        # Check if the student meets the requirements for "Do not Progress (module retriever)" 
        elif(credit_fail <= 60):

             # If the condition is true then output "Do not Progress (module retriever)"
             print("Do not progress – module retriever")

             retriever_list.append(credit_pass)   #Adding credit at pass to the retriever list.
             retriever_list.append(credit_defer)  #Adding credit at defer to the retriever list.
             retriever_list.append(credit_fail)   #Adding credit at fail to the retriever list.
                
             # Module retriever count 
             retriever += 1
            
            # Check if the student meets the requirements for "Exclude"
        elif (credit_fail >= 80):

             # If the condition is true then output "Exclude"
             print("Exclude") 

             exclude_list.append(credit_pass)    #Adding credit at pass to the exclude list.
             exclude_list.append(credit_defer)   #Adding credit at defer to the exclude list.
             exclude_list.append(credit_fail)    #Adding credit at fail to the exclude list.

             # Module exclude count 
             exclude += 1 
        
        while True:
                print("\n")
                print("Would you like to enter another set of data? " )
                run_again = str(input("Enter 'y' for yes or 'q' to quit and view results: "))
                print("\n")
                if run_again == "y": 
                    break
                
                elif run_again == "q":  
                    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")  
                    print("\n")
                    print(top_left_corner+horizontal*55+top_right_corner)
                    print(vertical+"                    H I S T O G R A M                  "+vertical)
                    print(bottom_left_corner+horizontal*55+bottom_right_corner)
                    print()
                    
                    # Output the Histogram
                    print("\n","Progress",progress," :",progress*" *")
                                            
                    print("\n","Trailer",trailer,"  :",trailer*" *")
                                                    
                    print("\n","Retriever",retriever,":",retriever*" *")
                    
                    print("\n","Exclude",exclude,"  :",exclude*" *")
                    
                    #Calculating the total count.
                    total_count=progress+retriever+trailer+exclude   

                    print("\n")
                    print(total_count,"outcomes in total.")
                    print("\n")
                    
                    for total_count in range(0,total_count):

                    # Create an empty list to store output
                        output_list=[]
                        
                        # Check if there is progress
                        if progress > 0:
                            print("Progress - ",end=" ")
                    
                            # Adding credits pass, credits defer and credit fail from progress_list to output_list
                            for a in range(0,3):
                                output_list.append(progress_list[progress_count])
                                progress_count += 1

                            print(*output_list,sep=" , ")

                            # Clearing the output_list in order to store next set of data.
                            output_list.clear() 

                            # Decrement the progress counter
                            progress -= 1    
                            print("\n")     
                        
                        # Check if there is a module trailer 
                        elif trailer>0:
                            print("Progress (module trailer) - ",end=" ")
                            
                            # Adding credits pass, credits_defer and credit fail from trailer list to output list
                            for a in range(0,3):
                                output_list.append(trailer_list[trailer_count])
                                trailer_count += 1

                            print(*output_list,sep=" , ") 
                            
                            # Clearing the output_list in order to store next set of data.
                            output_list.clear()   

                            # Decrement the trailer counter
                            trailer -= 1
                            print("\n")   
                        
                        # Check if there is a module retriever
                        elif retriever>0:
                            print("Do not progress (module retriever) - ",end=" ")
                            
                            # Adding credits pass, credits defer and credit fail from retriever list to output list
                            for a in range(0,3):
                                output_list.append(retriever_list[retriever_count])
                                retriever_count += 1

                            print(*output_list, sep=" , ")
                            # Clearing the output_list in order to store next set of data.
                            output_list.clear() 
                            
                            # Decrement the retriever counter
                            retriever -= 1
                            print("\n")

                        #Check if there is an exclude    
                        elif exclude>0:
                            print("Exclude - ",end=" ")
                            
                            # Adding credits pass, credits defer and credit fail from exclude list to output list
                            for a in range(0,3):
                                output_list.append(exclude_list[exclude_count])
                                exclude_count += 1

                            print(*output_list,sep =" , ")    

                            # Clearing the output_list in order to store next set of data.
                            output_list.clear()

                            # Decrement the exclude counter
                            exclude -= 1
                            
                       
                    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")             
                  
                else:
                    print("Invalid Input")
        
run_again = "y"
while True:
    print("\n")

    # Get the user type
    user_type = input("Please enter whether you are a student(s) or a staff member(sm): ")  

    if user_type == "s":
        print()
        print(top_left_corner+horizontal*84+top_right_corner)
        print(vertical+"                W E L C O M E  T O  T H E  S T U D E N T  V E R S I O N             "+vertical)
        print(bottom_left_corner+horizontal*84+bottom_right_corner)
        print()
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
        print()
        student()    #Calling the function for student version.

    elif user_type == "sm":
        print()
        print(top_left_corner+horizontal*76+top_right_corner)
        print(vertical+"             W E L C O M E  T O  T H E  S T A F F  V E R S I O N            "+vertical)
        print(bottom_left_corner+horizontal*76+bottom_right_corner)
        print() 
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------")  
        print()
        staff()      #Calling the function for staff version.

    else:
        print()
        print("Invalid format. Please enter (s) if you are a student or (sm) if you are a staff member.")

    
    

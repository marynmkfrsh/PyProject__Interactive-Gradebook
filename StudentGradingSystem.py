# This is an Interactive Student Grading Book. The idea for this project came from the internet.
# Note that this program has much more functionality than what was proposed in the idea on the internet.
# The idea was for a very basic gradebook that only allowed for adding removing students and grades and displayed a dictionary.
# The goal of this project: to practice some things I've learned, and learn more from getting stuck and having to refer to the internet.
# Notation decision is inconsistent: First, I opted for CamelCase but then in some places I use underscores.
# Used py -m pip install pandas  via command prompt to install numpy and pandas in Windows.

# To be enhanced: aesthetics



#############################################
#           Importing Libraries
#############################################


import statistics
import pandas as pd
import numpy as np
# import matpolotlib.pyplot as plt
# import seaborn as sns
from sys import exit



#############################################
#       Creating Main Class
#############################################

class operations:

    #Function that displays the main menu
    def mainMenu():
        print('''
         [1] Add/Remove Student
         [2] Enter/Edit Grades
         [3] Display Data-base
         [4] Change password
         [5] Statistics
         [6] Search
         [7] Exit \n
          ''')
        optionVar = input('What would you like to do: ')
        print("\n")
        return optionVar



		
    #Function for adding student to gradebook; students are columns; note that all record (grades) will be empty thus appearing as NaN in the dataframe  
    def addStudent(book):
        name = str(input('Who would you like to add: '))
        book[name] = {}
        print('Success!')
		

    #Function for removing student from gradebook; students are columns
    def removeStudent(book):
        name = str(input('Who would you like to remove: '))
        check = str(input('Are you sure? '))
        try:
            if check == 'yes' or check == 'Yes':
                del book[name]
                print('job complete')
            elif check == 'no' or check == 'No':
                print('Ok. Not deleted.')
            else:
                print('Input not understood, please try again')
        except Exception as e:
            print(str(e))
            print('That person is not in the list.')



    #Function for adding grade to gradebook
    def addGrade(book):
		
        try:
            name = str(input('Student name: '))
            test = str(input('Test: '))
            grade = float(input('Test score: '))

        except Exception as f:
            print(str(f))
            print('Uh-Oh! Seems like you didn\'t enter a numerical grade.')
        
        try:
            book[name][test] = grade
            print(book[name][test])
            print('\nSuccessful!\n')
        
        except Exception as e:
            print(str(e))
            print('\n \n Uh-Oh! Something went wrong! Student does not exist in book. \n ')
                


    #Function for removing grade from gradebook
    def removeGrade(book):
        name = str(input('Student name: '))
        test = str(input('Test: '))
        
        try:
            del book[name][test]
            print('\nSuccessful!\n')
        
        except Exception as e:
            print(str(e))
            print("Error! Student or test doesn't exist.")




    #Function for searching the gradebook
    def searchFor(book):
        df = pd.DataFrame(book)
        user_input = None

        try:
            user_input = int(input("[1] Name [2] Test [3] Specific [4] \n\n"))
            pass
        except Exception as e:
            print(str(e))
            print("Not an acceptable input")
            return 0
        

        if user_input == 1:
            name = str(input("Enter Name: "))
            try:
                print(df[name])
                pass
            except Exception as e:
                print(str(e))
                print("This name does not exist in book.")
                pass

        elif user_input == 2:
            test = input("Enter Test: ")
            try:
                print(df.loc[test])
                pass
            except Exception as e:
                print(str(e))
                print("This test does not exist in the book.")
                pass
            pass

        elif user_input == 3:
            try:
                student = str(input('Student name: '))
                test = str(input('Test: '))
                print('\n', df[student][test], '\n')
                pass
            except Exception as e:
                print(str(e))
                print('\n That student or test does not exist! \n')
                

        elif user_input == 4:
            return 0
        else:
            print("That is not an option. Select again. \n")
            operations.searchFor(book)
            

		
    #Function that provides summary statistics
    def bookstats(book):
        df = pd.DataFrame(book)
        user_input = None

        try:
            user_input = int(input("[1] Overall [2] Test [3] Return \n\n"))
            pass
        except Exception as e:
            print(str(e))
            print("Unexpected input, try again.")
            operations.bookstats(book)
            pass

        if user_input == 1:
            print(df.describe())
            pass
        elif user_input == 2:
            test = input("Enter Test: ")
            print("\n\n")
            print(df.loc[test].describe())
            pass
        elif user_input == 3:
            return 0
        else:
            print("That is not an option, try again.")
            operations.bookstats(book)
            pass
        
        
        
		
    #Function to display the gradebook	
    def grdbkPrint(book):
        df = pd.DataFrame(book)
        print('\n', df, '\n')
        	


    #Function to change password
    def changePass():
        '''
        The password is stored in a local file named shadow.txt 
        '''
        
        newPass = input('Enter the new password: ')
        newPass = newPass + ' '
        shFile = open('shadow.txt', 'w')
        shFile.write(newPass)
        shFile.close()

        print(f'New password: {newPass}')
        # Testing something else
        #print('New password: ', newPass[0:-1])



#############################################
#        Initializing the gradebook
############################################# 


gradeBook = {}
names = ['Allison', 'Bob', 'Dan', 'Navid', 'Maryam', 'Sara', 'Nickolas', 'Megan', 'Julia', 'Ghazal']
testnames = ['Test' + ' ' + str(i+1) for i in range(len(names))]

for indx, name in enumerate(names):
    gradeBook[name] = {}
    for tname in testnames:
        gradeBook[name][tname] = np.random.randint(low = 30, high = 101)


#############################################
#                  main()
#############################################

#####Password Check#####

passwdVar = input('Password: ')

passwd = str(open('shadow.txt', 'r').read())
passwd = passwd[0:-1]

if passwdVar != passwd:
    for num in range(3):
        Var = input('Password is incorrect, try again: ')
        if Var == passwd:
            break
        elif num < 2:
            continue
        else:
            print('ALERT! You have been logged out')
            exit()
            
print('Good Job! Next step now! \n \n \n')

print('While using this program when prompted, please make sure to enter all tests and names as they appear. All options are to be chosen via numeric input. \n\n\n" 


#####End Password Check#####




#####Main Loop#####


option = 0      # This is the main menu user option

# The while loop controlling the program operation
while option != 7:

    option = int(operations.mainMenu())

    if option == 1:
        choice = int(input('\n [1] Add [2] Remove [3] Return  : '))
        if choice == 1:
            operations.addStudent(gradeBook)
        elif choice == 2:
            operations.removeStudent(gradeBook)
        elif choice == 3:
            continue
        else:
            print("Not an option. \n")
            continue
			
    elif option == 2:
        choice = int(input('\n [1] Add [2] Remove [3] Return   : '))
        if choice == 1:
            operations.addGrade(gradeBook)
        elif choice == 2:
            operations.removeGrade(gradeBook)
        elif choice == 3:
            continue
        else:
            print("Not an option. \n")
            continue
        
    elif option == 3:
        operations.grdbkPrint(gradeBook)
		
    elif option == 4:
        operations.changePass()
        
    elif option == 5:
        operations.bookstats(gradeBook)
        
    elif option == 6:
        operations.searchFor(gradeBook)
        
    elif option == 7:
        print('\n Thank you for using the program. \n')
        exit()
    else:
        print('That is not an option, please enter a number: ')

    

#####Program End#####





        

# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# Molly Weaver, 03/13/21, Added code to complete assignment 9
# ------------------------------------------------------------------------ #

# Import Modules

import DataClasses as DC
import IOClasses as IOC
import ProcessingClasses as PC

# Start Data -------------------------------------------------------------------- #

# Declaration of variables and constants
strFileName = 'EmployeeData.txt'    # file to save data
lstOfEmployeeObj = []               # list to save employee objects
strChoice = ""                      # users' menu choice
lstNewEmployee = []                 # list to save new employee info

# End Data -------------------------------------------------------------------- #

# Start Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of employee objects when script starts
lstOfEmployeeObj = PC.FileProcessor.read_data_from_file(strFileName)

while(True):
    IOC.EmployeeIO.print_menu_items()  # Show user a menu of options
    strChoice = IOC.EmployeeIO.input_menu_options()  # Get user's menu option choice

# Process user's menu choice
    if strChoice.strip() == "1":  # Menu option 1 -> Show user current data in the list of employee objects
        IOC.EmployeeIO.print_current_list_items(lstOfEmployeeObj)

    elif strChoice == "2":  # Menu option 2 -> Let user add data to the list of employee objects
        objNewEmployee = IOC.EmployeeIO.input_employee_data()
        lstOfEmployeeObj.append(objNewEmployee)

    elif strChoice == "3":  # Menu option 3 -> Let user save current data to file
        PC.FileProcessor.save_data_to_file(strFileName, lstOfEmployeeObj)

    elif strChoice == "4":  # Let user exit program
        print("Goodbye!")
        break

# End Main Body of Script  ---------------------------------------------------- #

# ---------------------------------------------------------- #
# Title: Test Harness
# Description: A main module for testing
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created script
# Molly Weaver 03/09/21 Added code to complete HW09
# ---------------------------------------------------------- #
if __name__ == "__main__":
    import DataClasses as D  # data classes
    import ProcessingClasses as P  # processing classes
    import IOClasses as I  # input/output classes
else:
    raise Exception("This file was not created to be imported")

# Test data module
objP1 = D.Employee(1, "Bob", "Smith")
objP2 = D.Employee(2, "Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test processing module
P.FileProcessor.save_data_to_file("EmployeeData.txt", lstTable)
lstFileData = P.FileProcessor.read_data_from_file("EmployeeData.txt")
for row in lstFileData:
    p = D.Employee(row[0], row[1], row[2])
    print(p.to_string().strip(), type(p))

# Test IO classes
I.EmployeeIO.print_menu_items()
# I.EmployeeIO.print_current_list_items(lstTable)
e1 = I.EmployeeIO.input_employee_data()
print(e1)

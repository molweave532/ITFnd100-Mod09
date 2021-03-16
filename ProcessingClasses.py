# ---------------------------------------------------------- #
# Title: Processing Classes
# Description: A module of multiple processing classes
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created script
# Molly Weaver 03/09/21 Added code to complete HW09
# ---------------------------------------------------------- #
if __name__ == "__main__":
    raise Exception("This file is not meant to run by itself")
    # meant to be imported

class FileProcessor:
    """Processes data to and from a file and a list of objects:

    methods:
        save_data_to_file(file_name,list_of_objects):

        read_data_from_file(file_name): -> (a list of objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
    """

    @staticmethod
    def save_data_to_file(file_name: str, list_of_objects: list):
        """ Write data to a file from a list of object rows

        :param file_name: (string) with name of file
        :param list_of_objects: (list) of objects data saved to file
        :return: (bool) with status of success status
        """
        success_status = False
        try:
            file = open(file_name, "w")
            for row in list_of_objects:
                file.write(row.__str__() + "\n")
            file.close()
            success_status = True
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return success_status

    @staticmethod
    def read_data_from_file(file_name: str):
        """ Reads data from a file into a list of object rows

        :param file_name: (string) with name of file
        :return: (list) of object rows
        """
        list_of_rows = []
        try:
            file = open(file_name, "r")
            for line in file:
                row = line.split(",")
                list_of_rows.append(row)
            file.close()
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return list_of_rows

class DatabaseProcessor:
    """Pickles data to and from a file and a list of employee objects:

    methods:
        save_data_to_file(file_name, list_of_employee_objects)

        read_data_from_file(file_name)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Molly Weaver, 03/13/2021, Modified code to complete assignment 9
    """

    @staticmethod
    def read_data_from_pickle_file(file_name):
        """ Reads data from a pickled file

        :param file_name: (string) with name of file
        :return: list_of_rows
        """
        import pickle

        file_unpickle = open(file_name, "rb")
        list_of_employees = pickle.load(file_unpickle)
        file_unpickle.close()
        return list_of_employees

    @staticmethod
    def save_data_to_pickle_file(file_name, list_of_employees):
        """ Saves data from a list of product objects

        :param file_name: (string) with name of file
        :param list_of_rows: (list) you want written to file
        :return: list_of_rows
        """
        import pickle

        file_pickle = open(file_name, "wb")
        pickle.dump(list_of_employees, file_pickle)
        file_pickle.close()
        return list_of_employees


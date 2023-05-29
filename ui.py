import os




class Ui:
    def __init__(self):
        self.logo = ''' 
         /$$$$$$$                            /$$                 /$$$$$$$                  /$$ /$$           /$$                              
        | $$__  $$                          | $$                | $$__  $$                | $$|__/          | $$                              
        | $$  \ $$ /$$   /$$ /$$$$$$$   /$$$$$$$ /$$   /$$      | $$  \ $$  /$$$$$$   /$$$$$$$ /$$  /$$$$$$ | $$  /$$$$$$   /$$$$$$  /$$   /$$
        | $$$$$$$ | $$  | $$| $$__  $$ /$$__  $$| $$  | $$      | $$$$$$$/ |____  $$ /$$__  $$| $$ /$$__  $$| $$ /$$__  $$ /$$__  $$| $$  | $$
        | $$__  $$| $$  | $$| $$  \ $$| $$  | $$| $$  | $$      | $$__  $$  /$$$$$$$| $$  | $$| $$| $$  \ $$| $$| $$  \ $$| $$  \ $$| $$  | $$
        | $$  \ $$| $$  | $$| $$  | $$| $$  | $$| $$  | $$      | $$  \ $$ /$$__  $$| $$  | $$| $$| $$  | $$| $$| $$  | $$| $$  | $$| $$  | $$
        | $$$$$$$/|  $$$$$$/| $$  | $$|  $$$$$$$|  $$$$$$$      | $$  | $$|  $$$$$$$|  $$$$$$$| $$|  $$$$$$/| $$|  $$$$$$/|  $$$$$$$|  $$$$$$$
        |_______/  \______/ |__/  |__/ \_______/ \____  $$      |__/  |__/ \_______/ \_______/|__/ \______/ |__/ \______/  \____  $$ \____  $$
                                                /$$  | $$                                                                 /$$  \ $$ /$$  | $$
                                                |  $$$$$$/                                                                |  $$$$$$/|  $$$$$$/
                                                \______/                                                                  \______/  \______/ 
        '''

        self.menu = ''' 
        Menu 
        1. List Test Codes
        2. List of Patients
        3. Test Descriptions
        4. Show Patient Details
        5. Show Tests for Patients
        6. Show a Test By Patients
        7. Add a New Test
        8. Add a New Patient
        9. Add Test Taken By a Patient
        10. Exit
        
        
        
        '''

    @staticmethod
    def clear_screen():
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')

    def show_logo(self):
        print(self.logo)
        input("           Press Enter to Continue")
        self.clear_screen()

    def get_menu_selection(self):
        print(self.menu, end='')
        selection = input()
        print('\n')
        if not selection.isdigit():
            selection = -1
        else:
            selection = int(selection)
            if -1 < selection > 10:
                selection = -1
        return selection
    
    @staticmethod
    def show_patient_list(patients):
        print("Patients:")
        print("---------\n")
        for patient in patients:
            print(patient)


    @staticmethod
    def show_test_list(tests):
        print("Test Types:")
        print("-----------\n")
        for test in tests:
            print(test)

    @staticmethod
    def print_details(name, add, phone):
        print(name)
        print("-------")
        print(f"Address: {add}")
        print(f"Phone Number: {phone}")

    def askPatientName(self):
        name = self.user_input("What is the Name of the Patient? ")
        return name
    
    
    def askTestName(self):
        name = self.user_input("What is the Code of the Test? ")
        return name
    
    def askTest(self):
        test = self.user_input("What is the Code of the Test? ")
        return test
    
    
    @staticmethod
    def error_message():
        print("Unfortunatly it appears an error has occured, this may be caused by a Test or Patient already exsists under that name, or something has been input incorrectly.")

    @staticmethod
    def print_test_by_Patient(results, name):
        """
            Description:
                Prints the name of the patient and all tests under the name given with the results variable
            Args:
                name(str): The name of the patient
                results(str): The code of the test
        """
        if results ==[]:
            print("No Results were found under that Code, please try again!")
        print("")
        print(f"Patient Name: {results} \n")
        for tests in name:
            print(f"Test Type: {tests[0]}")
            print(f"Date: {tests[1]}")
            print(f"Results: {tests[2]} \n")
         

    @staticmethod
    def print_test_stuff(name, desc, cost):
        """
            Description:
                Prints the name of the test as well as its description and cost
            Args:
                name(str): The name of the test
                desc(str): The description of the test
                cost(int): The cost of the test
        """
        print(name)
        print("------")
        print(f"Descirption: {desc}")
        print(f"Cost: {cost}")

    @staticmethod
    def print_teststaken(teststaken, name):
        print(f"Name: {teststaken}")
        print("------")
        print(f"Tests Taken By This Patient: {name}")

    def add_new_patient(self):
        isTrue = True
        name = self.user_input("What is the Patient's name? (NAME) ")
        dob = self.user_input("What is the Patient's D.O.B? (YYYY-MM-DD) ")
        add = self.user_input("What is the Patient's Address? (ST-NUM, STREET, SUBURB, STATE)")
        postcode = self.user_input("What is the Patient's Postcode? (POSTCODE) ")
        height = self.user_input("What is the Patient's Height? (NUM IN CM) ")
        weight = self.user_input("What is the Patient's Weight? (WIGHT IN KG) ")
        phone = self.user_input("What is the Patient's Phone Number (NUMBER) ")

        if name == "":
            isTrue = False
        if dob == "":
            isTrue = False
        if add == "":
            isTrue = False
        if  postcode == "":
            isTrue = False
        if height == "":
            isTrue = False
        if weight == "":
            isTrue = False
        if phone =="":
            isTrue = False

        return name, dob, add, postcode, height, weight, phone, isTrue

    def add_test_taken(self):
        isTrue = True
        name = self.user_input("What is the Name of the Patient? (NAME) ")
        test = self.user_input("What is the Test Code? (THREE LETTER CODE) ")
        datetime = self.user_input("What was the Date this Test was taken? (YYYY-MM-DD) ")
        result = self.user_input("What was the Result of the Test? (TEST RESULTS) ")

        if name == "":
            isTrue = False
        if test == "":
            isTrue = False
        if datetime == "":
            isTrue = False
        if  result == "":
            isTrue = False

        return name, test, datetime, result, isTrue

    def add_new_test(self):
        isTrue = True
        code = self.user_input("What is the Code of the Test? (THREE LETTER CODE) ")
        name = self.user_input("What is the Name of the Test? (NAME) ")
        desc = self.user_input("What is the Description of the Test? (DESCRIPTION) ")
        cost = self.user_input("What is the Cost of the Test? (IN DOLLARS, NO CENTS) ")


        if code == "":
            isTrue = False
        if name == "":
            isTrue = False
        if desc == "":
            isTrue = False
        if  cost == "":
            isTrue = False


        return code, name, desc, cost, isTrue



    @staticmethod
    def user_input(question: str):
        userInput = input(question)
        return userInput



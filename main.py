from ui import Ui
from data_store import DataStore

ui = Ui()
data_store = DataStore()
ui.show_logo()

running = True

while running:
    selection = ui.get_menu_selection()

    if selection == 1:  # List test codes
        tests = data_store.select_test_type_codes()
        ui.show_test_list(tests)

    elif selection == 2:  # List Patients
        patients = data_store.select_patient_list()
        ui.show_patient_list(patients)

    elif selection == 3:  # Show Test description
        try:
            name = ui.askTestName()
            desc, cost = data_store.select_test_type_summary(name)
            ui.print_test_stuff(name, desc, cost)
        except Exception:
            ui.error_message()


       
    elif selection == 4:  # Show Patient details
        name= ui.askPatientName()
        try:
            while data_store.has_patient(name) == False:
                ui.error_message()
                name = ui.askPatientName()
            else:
                phone, add = data_store.select_patient(name)
                ui.print_details(name, add, phone)
        except Exception:
            ui.error_message()


    elif selection == 5:  # Show tests for a patient
        name = ui.askPatientName()
        try:
            while data_store.has_patient(name) == False:
                ui.error_message()
                name = ui.askPatientName()
            else:
                teststaken = data_store.select_patient_results_all_tests(name)
                ui.print_teststaken(name, teststaken)
        except Exception:
            ui.error_message()




    elif selection == 6:  # Show a test by patient
        name = ui.askPatientName()
        code = ui.askTest()
        try:
            while data_store.has_patient(name) == False:
                ui.error_message()
                name = ui.askPatientName()
            else:
                test = data_store.select_patient_results_by_test(name, code)
                ui.print_test_by_Patient(name, test)
        except Exception:
            ui.error_message()
            
            

    elif selection == 7:  # Add new Test
        code, name, desc, cost, isTrue = ui.add_new_test()

        while data_store.has_test_type(code, name, desc, cost) == False:
            ui.error_message()
            code, name, desc, cost, isTrue = ui.add_new_test()
        else:
            data_store.insert_update_test_type(code, name, desc, cost)

        while isTrue == False:
            ui.error_message()
            code, name, desc, cost, isTrue = ui.add_new_test()
        else:
            data_store.insert_update_test_type(code, name, desc, cost)

    elif selection == 8:  # Add new Patient
        name, dob, add, postcode, height, weight, phone, isTrue = ui.add_new_patient()

        while isTrue == False:
            ui.error_message()
            name, dob, add, postcode, height, weight, phone, isTrue = ui.add_new_patient()
        else:
            data_store.insert_patient(name, dob, add, postcode, height, weight, phone)

    elif selection == 9:  # Add test taken by patient
        try:
            name, test, result, datetime = ui.add_test_taken()
            data_store.insert_patient_test_results(name, test, result, datetime)
        except Exception:
            ui.error_message()

        

    elif selection == 10:
        running = False

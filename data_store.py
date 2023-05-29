from typing import ClassVar, Dict, List, Union


class DataStore:
    """
    This class provides the interface for the Vikings Radiology application
    It holds the data store and functions to read and manipulate the patient test data.

    Attributes:
        test_type [Dict[str, List[Union[str, int]]] A test name, Description and Cost
        patient [Dict[str, List[str]]] A patient, their details
        tests_taken [Dict[str, List[List[str]]]] A List of patient tests and results
    """

    def __init__(self):
        self.test_type: ClassVar[Dict[str, List[Union[str, int]]]] = {}
        self.patient: ClassVar[Dict[str, List[str]]] = {}
        self.tests_taken: ClassVar[Dict[str, List[List[str]]]] = {}

        self.data_import()

    def insert_update_test_type(self, code: str, name: str, desc: str, cost: int):
        """"
            Description:
                Inserts a new test type or replaces the existing one in the system
            Args:
                code (str): Shortened name of the test type
                name (str): The name of the test type
                desc (str): Description of the test type
                cost (int): Price of the test
        """""

        self.test_type[code] = [name, desc, cost]

    def select_test_type_summary(self, name: str) -> List[Union[str, int]]:
        """
            Description
                Selects the test type and returns description and cost
            Args:
                name (str): The name of the test

            Returns:
                The Description and Cost of the queried test type
                or an empty list if no test of that name exists
        """
        return self.test_type[name][1], self.test_type[name][2]

    def select_test_type_codes(self) -> List[str]:
        """
            Description
                Obtains all the Codes for the different test types

            Returns:
                A list of all the test type codes
        """
        return list(self.test_type)

    def select_patient_list(self) -> List[str]:
        """
            Description
                Obtains the names of all the clients in the system

            Returns:
                A list of all the patients names
        """
        return list(self.patient)

    def has_patient(self, name):
        """
            Description
                Checks to see if the patient name exists in the records

            Returns:
                True if patient record exists, false if it doesn't
        """
        for name in self.patient:
            if self.patient == name:
                return True
            else:
                False
        return name in self.patient

    def has_test_type(self, code, name, desc, cost):
        """
            Description
                Checks to see if the Test Type Code exists in the records

            Returns:
                True if Test Type record exists, false if it doesn't
        """
        for code in self.test_type:
            if self.test_type == code:
                return True
            else:
                False
        for code in self.test_type:
            if self.test_type == name:
                return True
            else:
                False
        for code in self.test_type:
            if self.test_type == desc:
                return True
            else:
                False
        return code in self.test_type
    def has_code(self, code):
        """
            Description
                Checks to see if the Test Type Code exists in the records

            Returns:
                True if Test Type record exists, false if it doesn't
        """
        for code in self.test_type:
            if self.test_type == code:
                return True
            else:
                False


    def insert_patient(self, name: str, dob: int, add: str, postcode: str, height: str, weight: str, phone: int):
        """
            Description:
                Inserts a new patient record into the system
            Args:
                name (str): The new patient being added to the system
                dob (int): The patients date of birth
                add (str): The new patient's address
                postcode (str): The new patient's postcode
                height (int): Patient height
                weight (int): Patient weight
                phone (int): Patient's phone number
        """
        self.patient[name] = [dob, add, postcode, height, weight, phone]

    def select_patient(self, name: str) -> List[Union[str, int]]:
        """
            Description:
                Selects the patient and returns the patient's contact information
            Args:
                add: The address of the patient
                phone (int): The phone number of the patient
                name (str): The name of the patient being searched.

            Returns:
                Patient name, patient address, patient phone number
        """

        return self.patient[name][1], self.patient[name][5]

    def insert_patient_test_results(self, name: str, test: str, result: int, datetime: str):
        """
            Description:
                Inserts a new test result into the system.
            Args:
                name (str): The name of the patient being searched.
                test (str): The name of the test taken.
                result (int): The value of the test result.
                datetime (int): The date and time the test was taken.
        """
        self.tests_taken[name].append([test, result, datetime])

    def select_patient_results_all_tests(self, name: str) -> List[List[str]]:
        """
            Description:
                Selects the patient and returns test results
            Args:
                name (str): The name of the patient

            Returns:
                All test results for the given patient
                Empty List if no tests for patient exist
        """
        return self.tests_taken[name]

    def select_patient_results_by_test(self, name: str, test: str) -> List[List[str]]:
        """
            Description:
                Selects the patient and test and returns test results specific to identified patient and test
            Args:
                name (str): The name of the patient
                test (str): The code of the test

            Returns:
                All test results for patient / test combination
        """
        returnList = []
        for TestsTaken in self.tests_taken[name]:
            if TestsTaken[0] == test:
                returnList.append(TestsTaken)
        return returnList
     
        

    def data_import(self):
        # ###################################### #
        # ###### Populate Test Type Data ####### #
        # ###################################### #
        # ###### Name, Description, Price ###### #
        # ###################################### #
        self.test_type['XRY'] = [
            "X-Ray",
            "A penetrating form of high-energy electromagnetic radiation.",
            145
        ]

        self.test_type['CAT'] = [
            "Computed Tomography (CT) Scan",
            "Uses multiple x-ray measurements from different angles to produce tomographic images of the body allowing the user to see inside the body without opening.",
            290
        ]

        self.test_type['MRI'] = [
            "Magnetic Resonance Imaging",
            "Utilises strong magnetic fields and magnetic gradients to generate images of the organs of the body.",
            445
        ]

        self.test_type['USD'] = [
            "Ultrasound Scan",
            "Utilises the therapeutic application of ultrasound. Creates images of internal body structures such as tendons, muscles, joints, blood vessels and internal organs.",
            195
        ]

        # ############################################ #
        # ########## Populate Patient Data ########### #
        # ############################################ #
        # ## DOB, Address, Postcode, height, weight ## #
        # ############################################ #
        self.patient['Harry'] = ['1984-06-14', '47 Nowhere Avenue, Voidville, QLD', '4378', 168, 58, "0499-885-131"]
        self.patient['Gary'] = ['1974-11-02', '938 Long Road, Largetown, QLD', '4928', 181, 87, "0472-336-490"]
        self.patient['Sally'] = ['2003-02-24', '3 Short Street, Littleton, QLD', '4552', 179, 67, "0413-458-391"]
        self.patient['Larry'] = ['1966-08-30', '56 Oldie Avenue, Retrovale, QLD', '4981', 184, 108, "0401-922-384"]
        self.patient['Barry'] = ['1993-10-07', '82 Newbie Street, Newtown, QLD', '4710', 168, 58, "0499-885-131"]
        self.patient['Jennifer'] = ['1989-03-28', '15 Lonely Lane, Remote Waters, QLD', '4523', 194, 84, "0892-224-019"]

        # ########################################## #
        # ####### Populate Tests Taken Data ######## #
        # ########################################## #
        # ####### [[ Result, Date, Room ], ] ####### #
        # ########################################## #
        self.tests_taken['Harry'] = [
            ['XRY', '2020-10-07', 'Compound Fracture of the Radius.'],
            ['XRY', '2020-10-07', 'Greenstick Fracture of the Ulna.'],
            ['USD', '2019-10-07', 'Grade three tear of the hamstring.']
        ]

        self.tests_taken['Gary'] = [
            ['MRI', '2019-10-07', 'Pulmonary Embolism present in lower right lung lobe.'],
        ]

        self.tests_taken['Sally'] = [
            ['CAT', '2019-10-07', 'Inconclusive evidence of Pancreatic Cancer to confirm pathology result.'],
            ['XRY', '2019-10-07', 'No evidence of fracture.']
        ]

        self.tests_taken['Larry'] = [
            ['XRY', '2019-10-07', 'Compound Fracture of the Humerous'],
            ['MRI', '2019-10-07', 'Highlights on Liver consistent with cancerous cells.'],
            ['USD', '2019-10-07', 'Complex tendonopathy of the Satorius. Grade 1 Quadricep tendon tear.']
        ]

        self.tests_taken['Barry'] = [
            ['USD', '2019-10-07', 'Evidence of 4cm tear of Plantar Fascia on right foot.'],
        ]

        self.tests_taken['Jennifer'] = [
            ['USD', '2019-10-07', 'Evidence of 2cm tear of Right Deltoid.'],
            ['MRI', '2019-10-07','Inconclusive evidence to confirm pathology result suggestion of smoking induced Lung Cancer.'],
            ['XRY', '2019-10-07', 'Compound Fracture of the Femur.']
        ]

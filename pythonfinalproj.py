class Doctor:   
    def __init__(self):
        self.id = "None"
        self.name = "None"
        self.spec = "None"
        self.hours = "None"
        self.qual = "None"
        self.room = "None"

    def formatDrInfo(self,list_to_convert):
        self.string_data = '_'.join(list_to_convert)
        return self.string_data + '\n'

    def enterDrInfo(self):
        self.id = input("Enter the doctor's ID:\n")
        self.name = input("Enter the doctor's name:\n")
        self.spec = input("Enter the doctor's specility:\n")
        self.hours = input("Enter the doctor's timing (e.g., 9am-6pm):\n")
        self.qual = input("Enter the doctor's qualification:\n")
        self.room = input("Enter the doctor's room number:\n")
        return [self.id,self.name,self.spec,self.hours,self.qual,self.room]

    def readDoctorsFile(self):
        self.open_file = open("doctors.txt", "r")
        self.test_list = self.open_file.readlines()
        self.open_file.close()
        return self.test_list

    def searchDoctorById(self):
        self.doctor_list = self.readDoctorsFile()
        self.temp_list = []
        
        for i in range(len(self.doctor_list)):
            self.temp_list.append([])
            self.temp_list[i] = self.doctor_list[i].split("_")

        self.check = input("\n Enter the doctor ID:\n")
        
        self.flag = False
        for i in range(len(self.temp_list)):
            if self.temp_list[i][0] == self.check:
                self.displayDoctorInfo(self.temp_list[i])
                self.flag = True
        if self.flag == False:
            print("Can't find the doctor with the same ID on the system")

    def searchDoctorByName(self):
        self.doctor_list = self.readDoctorsFile()
        self.temp_list = []
        for i in range(len(self.doctor_list)):
            self.temp_list.append([])
            self.temp_list[i] = self.doctor_list[i].split("_")

        self.check = input("\n Enter the doctor name:\n")
        
        self.flag = False
        for i in range(len(self.temp_list)):
            if self.temp_list[i][1] == self.check:
                self.displayDoctorInfo(self.temp_list[i])
                self.flag = True
        if self.flag == False:
            print("Can't find the doctor with the same name on the system")
        
    def displayDoctorInfo(self,doctor_list):
        self.doctor_list = doctor_list
        self.doctor_list[4] = self.doctor_list[4].upper() 
        print(f"{'Id': <8}{'Name': <25}{'Specialty': <18}{'Timing': <18}{'Qualification': <18}{'Room Number': <0}"+'\n')
        print(f"{self.doctor_list[0]: <8}{self.doctor_list[1]: <25}{self.doctor_list[2]: <18}{self.doctor_list[3]: <18}{self.doctor_list[4]: <18}{self.doctor_list[5]: <0}")

    def editDoctorInfo(self):
        self.doctor_list = self.readDoctorsFile()
        self.temp_list = []
        for i in range(len(self.doctor_list)):
            self.temp_list.append([])
            self.temp_list[i] = self.doctor_list[i].split("_")

        self.check = input("Please enter the id of the doctor that you want to edit their information:\n")
        
        self.flag = False
        for i in range(len(self.temp_list)):
            if self.temp_list[i][0] == self.check:
                self.temp_list[i][1] = input("\nEnter new Name:\n")
                self.temp_list[i][2] = input("\nEnter new Specilist in:\n")
                self.temp_list[i][3] = input("\nEnter new Timing: \n")
                self.temp_list[i][4] = input("\nEnter new Qualification: \n")
                self.temp_list[i][5] = input("\nEnter new Room number:\n")
                self.doctor_list[i] = self.formatDrInfo(self.temp_list[i])
                self.writeListOfDoctorsToFile(self.doctor_list)
                self.flag = True
        if self.flag == False:
            print("Can't find the doctor with the same ID on the system\n")

    def displayDoctorsList(self):
        self.doctor_list = self.readDoctorsFile()
        self.temp_list = []

        for i in range(len(self.doctor_list)):
            self.temp_list.append([])
            self.temp_list[i] = self.doctor_list[i].split("_")
        
        del self.temp_list[0] #removes file header
    
        print(f"{'Id': <8}{'Name': <25}{'Specialty': <18}{'Timing': <18}{'Qualification': <18}{'Room Number': <0}"+'\n')
        for i in range(len(self.temp_list)):
            print(f"{self.temp_list[i][0]: <8}{self.temp_list[i][1]: <25}{self.temp_list[i][2]: <18}{(self.temp_list[i][3].lower()): <18}{(self.temp_list[i][4].upper()): <18}{self.temp_list[i][5]: <0}")

    def writeListOfDoctorsToFile(self,doctor_list):
        self.open_file = open("doctors.txt", "w")
        self.index = 0
        for entries in doctor_list:
            self.open_file.write(doctor_list[self.index])
            self.index +=1
        self.open_file.close()

    def addDrToFile(self):
        self.doctor_to_add = self.enterDrInfo()
        self.doctor_to_add = self.formatDrInfo(self.doctor_to_add)
        self.doctor_list = self.readDoctorsFile()
        
        self.index = 0
        for entries in self.doctor_list:
            if self.doctor_list[self.index].endswith('\n') == False:
                self.doctor_list[self.index] = self.doctor_list[self.index] + '\n'
            self.index += 1

        self.doctor_list.append(self.doctor_to_add)
        self.writeListOfDoctorsToFile(self.doctor_list)

class Facility:  
    def __init__(self):
        self.facility_name = "None"

    def addFacility(self):
        '''Adds and writes the facility name to the file'''
        self.open_file = open("facilities.txt", "r")
        self.facility_list = self.open_file.readlines()
        self.open_file.close()
        
        self.facility_name = input("Enter Facility name: \n")
        
        self.facility_list.append(self.facility_name)

        self.writeListOffacilitiesToFile(self.facility_list)

    def displayFacilities(self):
        '''Displays the list of facilities'''
        self.open_file = open("facilities.txt", "r")
        self.facility_list = self.open_file.readlines()
        self.open_file.close()

        self.facility_list[0] = "The " + self.facility_list[0]
        
        for i in range(len(self.facility_list)):
            if self.facility_list[i].endswith('\n') == False:
                print(self.facility_list[i]+'\n')
            else:
                print(self.facility_list[i])

    def writeListOffacilitiesToFile(self,new_entry):
        '''Writes the facilities list to facilities.txt'''
        self.open_file = open("facilities.txt", "w")
  
        self.index = 0
        for entries in new_entry:
            if new_entry[self.index].endswith('\n') == False:
                new_entry[self.index] = new_entry[self.index] + '\n'
            self.open_file.write(new_entry[self.index])
            self.index += 1

        self.open_file.close()

class Laboratory:
    def __init__(self):
        self.name = "None"
        self.cost = 0

    def addLabToFile(self):
        self.lab_to_add = self.enterLaboratoryInfo()
        self.lab_to_add = self.formatLabInfo(self.lab_to_add)
        self.lab_list = self.readLaboratoriesFile()

        self.index = 0
        for entries in self.lab_list:
            if self.lab_list[self.index].endswith('\n') == False:
                self.lab_list[self.index] = self.lab_list[self.index] + '\n'
            self.index += 1

        self.lab_list.append(self.lab_to_add)
        self.writeListOfLabsToFile(self.lab_list)  
    def writeListOfLabsToFile(self,lab_list):
        self.open_file = open("laboratories.txt", "w")
        self.index = 0
        for entries in lab_list:
            self.open_file.write(lab_list[self.index])
            self.index +=1
        self.open_file.close() 
    def displayLabsList(self):
        self.lab_list = self.readLaboratoriesFile()
        self.temp_list = []

        for i in range(len(self.lab_list)):
            self.temp_list.append([])
            self.temp_list[i] = self.lab_list[i].split("_")

        del self.temp_list[0] #removes file header

        print(f"{'Lab': <8}{'cost ': <0}"+'\n')
        for i in range(len(self.temp_list)):
            print(f"{self.temp_list[i][0]: <8}{self.temp_list[i][1]: <0}")

    def formatLabInfo(self,list_to_convert):
        self.string_data = '_'.join(list_to_convert)
        return self.string_data + '\n' 
    def enterLaboratoryInfo(self):
        self.name = input("Enter Laboratory facility:\n")
        self.price = input("Enter Laboratory cost:\n")
        return [self.name,self.price]
    def readLaboratoriesFile(self):
        self.open_file = open("laboratories.txt", "r")
        self.test_list = self.open_file.readlines()
        self.open_file.close()
        return self.test_list

class Patient:
    def formatPatientInfo(self,list_to_convert):
        self.string_data = '_'.join(list_to_convert)
        return self.string_data + '\n'   
    def enterPatientInfo(self):
        self.pid = input("Enter the patient's ID:\n")
        self.name = input("Enter the patient's name:\n")
        self.disease = input("Enter the patient's disease:\n")
        self.gender  = input("Enter the patient's gender:\n")
        self.age = input("Enter the patient's age:\n")

        return [self.pid,self.name,self.disease,self.gender,self.age]     
    def readPatientsFile(self):
        self.open_file = open("patients.txt", "r")
        self.test_list = self.open_file.readlines()
        self.open_file.close()
        return self.test_list
    def searchPatientById(self):
        self.patient_list = self.readPatientsFile()
        self.temp_list = []
        
        for i in range(len(self.patient_list)):
            self.temp_list.append([])
            self.temp_list[i] = self.patient_list[i].split("_")

        self.check = input("\n Enter the patient ID:\n")
        
        self.flag = False
        for i in range(len(self.temp_list)):
            if self.temp_list[i][0] == self.check:
                self.displayPatientInfo(self.temp_list[i])
                self.flag = True
        if self.flag == False:
            print("Can't find the patient with the same ID on the system")   
    def displayPatientInfo(self,patient_list):
        self.patient_list = patient_list
        print(f"{'Id': <8}{'Name': <25}{'disease': <18}{'gender': <18}{'age': <18}"+'\n')
        print(f"{self.patient_list[0]: <8}{self.patient_list[1]: <25}{self.patient_list[2]: <18}{self.patient_list[3]: <18}{self.patient_list[4]: <18}")  
    def editPatientInfo(self):
        self.patient_list = self.readPatientsFile()
        self.temp_list = []
        for i in range(len(self.patient_list)):
            self.temp_list.append([])
            self.temp_list[i] = self.patient_list[i].split("_")

        self.check = input("Please enter the id of the patient that you want to edit their information:\n")
        
        self.flag = False
        for i in range(len(self.temp_list)):
            if self.temp_list[i][0] == self.check:
                self.temp_list[i][1] = input("\nEnter new Name:\n")
                self.temp_list[i][2] = input("Enter the patient's disease:\n")
                self.temp_list[i][3] = input("Enter the patient's gender:\n")
                self.temp_list[i][4] = input("Enter the patient's age:\n")

                self.patient_list[i] = self.formatPatientInfo(self.temp_list[i])
                self.writeListOfPatientsToFile(self.patient_list)
                self.flag = True
        if self.flag == False:
            print("Can't find the patient with the same ID on the system\n") 
    def displayPatientsList(self):
        self.patient_list = self.readPatientsFile()
        self.temp_list = []

        for i in range(len(self.patient_list)):
            self.temp_list.append([])
            self.temp_list[i] = self.patient_list[i].split("_")
        
        del self.temp_list[0] #removes file header
    
        print(f"{'Id': <8}{'Name': <25}{'Disease': <18}{'Gender': <18}{'Age': <18}"+'\n')
          
        for i in range(len(self.temp_list)):
            #print(self.temp_list)
            print(f"{self.temp_list[i][0]: <8}{self.temp_list[i][1]: <25}{self.temp_list[i][2]: <18}{self.temp_list[i][3]: <18}{self.temp_list[i][4]: <18}")

    def writeListOfPatientsToFile(self,patient_list):
        self.open_file = open("patients.txt", "w")
        self.index = 0
        for entries in patient_list:
            self.open_file.write(patient_list[self.index])
            self.index +=1
        self.open_file.close()   
    def addPatientToFile(self):
        self.patient_to_add = self.enterPatientInfo()
        self.patient_to_add = self.formatPatientInfo(self.patient_to_add)
        self.patient_list = self.readPatientsFile()
        
        self.index = 0
        for entries in self.patient_list:
            if self.patient_list[self.index].endswith('\n') == False:
                self.patient_list[self.index] = self.patient_list[self.index] + '\n'
            self.index += 1

        self.patient_list.append(self.patient_to_add)
        self.writeListOfPatientsToFile(self.patient_list)    

class Menu:
    
    def Display_Menu(self):
        self.repeat = True
        while self.repeat:
            self.option = input('Welcome to Alberta Hospital (AH) Managment system\nSelect from the following options, or select 0 to stop:\n1 - 	Doctors\n2 - 	Facilities\n3 - 	Laboratories\n4 - 	Patients\n')
            
            if int(self.option) == 1:
                self.cycle = True
                self.obj_handle = Doctor()
                while self.cycle:
                    self.option = input('\nDoctors Menu:\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n')
                    if int(self.option) == 1:
                        self.obj_handle.displayDoctorsList()
                        print("\nBack to the previous Menu") 
                    elif int(self.option) == 2:
                        self.obj_handle.searchDoctorById()
                        print("\nBack to the previous Menu") 
                    elif int(self.option) == 3:
                        self.obj_handle.searchDoctorByName()
                        print("\nBack to the previous Menu")
                    elif int(self.option) == 4:
                        self.obj_handle.addDrToFile()
                        print("\nBack to the previous Menu")
                    elif int(self.option) == 5:
                        self.obj_handle.editDoctorInfo()
                        print("\nBack to the previous Menu")
                    elif int(self.option) == 6:
                        self.cycle = False
                        print("")

            elif int(self.option) == 2:
                self.cycle = True
                self.obj_handle = Facility()
                while self.cycle:
                    self.option = input('Facilities Menu:\n1 - Display Facilities list\n2 - Add Facility\n3 - Back to the Main Menu\n')
                    if int(self.option) == 1:
                        self.obj_handle.displayFacilities()
                        print("Back to the previous Menu") 
                    elif int(self.option) == 2:
                        self.obj_handle.addFacility()
                        print("\nBack to the previous Menu") 
                    elif int(self.option) == 3:
                        self.cycle = False
                        print("")
            
            elif int(self.option) == 3:
                self.cycle = True
                self.obj_handle = Laboratory()
                while self.cycle:
                    self.option = input('Laboratories Menu:\n1 - Display laboratories list\n2 - Add laboratory\n3 - Back to the Main Menu\n')
                    if int(self.option) == 1:
                        self.obj_handle.displayLabsList()
                    elif int(self.option) == 2:
                        self.obj_handle.addLabToFile()
                    elif int(self.option) == 3:
                        self.cycle = False
                    print("Back to the previous Menu\n") 
            
            elif int(self.option) == 4:
                self.cycle = True
                self.obj_handle = Patient()
                while self.cycle:
                    self.option = input('Patients Menu:\n1 - Display patients list\n2 - Search for patient by ID\n3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu\n')
                    if int(self.option) == 1:
                        self.obj_handle.displayPatientsList()
                    elif int(self.option) == 2:
                        self.obj_handle.searchPatientById()
                    elif int(self.option) == 3:
                        self.obj_handle.addPatientToFile()
                    elif int(self.option) == 4:
                        self.obj_handle.editPatientInfo()
                    elif int(self.option) == 5:
                        self.cycle = False
                    print("Back to the previous Menu\n")
            else:
                self.repeat = False          

run_obj = Menu()
run_obj.Display_Menu()
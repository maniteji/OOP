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
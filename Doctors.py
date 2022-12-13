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
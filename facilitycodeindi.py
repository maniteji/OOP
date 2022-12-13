class Facility:  
    def _init_(self):
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
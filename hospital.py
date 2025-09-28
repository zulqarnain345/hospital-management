class hospital:
    def __init__(self):
        print(f"{'-'*20} welcome to my hospital system {'-'*20}")
        print(f"\n 1)Add new patient \n 2)View all patients \n 3)Search patient by"
              "name \n 4)Discharge \n 5) exit")
        while True:

            self.num1=int(input("choise the option in 1,2,3,4... :: "))
            if self.num1 in [1,2,3,4,5]:
                break
            else:
                print("plz select the option: ")
    def add_new_patient(self):
        print(f"\n{'-'*20} enter the detail of the new patient {'-'*20}\n")

        self.name=input("enter the name of the patient:: ")
        if not self.name.isalpha():
            print("name shoud only contain letters ") 
       

        while True:
            try:
                self.age=int(input("enter the age of the patient:: "))
                if (self.age <= 0):
                    print("you can't add the age in negative ")

                else:
                    break
            except ValueError:
                print("you enter the nagtive age. ")  

        self.diseas=input("enter the diseas of patient:: ")
        if not self.diseas.isalpha():
            print("diseas should only contain letters ") 

        self.save()



    def save(self):
        with open('hospital.txt',"a")as f:
            f.write(f"\n{'-'*20} patient data {'-'*20}\n")
            f.write(f"NAME OF PATIEN:: {self.name} \n")
            f.write(f"AGE OF PATIEN:: {self.age} \n")
            f.write(f"DISEAS OF PATIEN:: {self.diseas} \n")
            f.write(f"{'-'*30}\n")

    def view_patient_list(self):
        print(f"{'-'*20} all patient list {'-'*20}")
        with open('hospital.txt',"r")as f:
            for line in f:
                print(line.strip())

    def search_patient(self):
        print(f"{'-'*20} search patient by name {'-'*20}")

        self.name1=input("enter the name of the patient you want to search:: ")
        if not self.name1.isalpha():
            print("name should be latters ")

        self.found =False
        with open("hospital.txt", "r") as f:
            lines = f.readlines()

        for i in range(len(lines)):
            if self.name1.lower() in lines[i].lower():  
                self.found = True
                print("\nPatient Data Found:")
                print(lines[i].strip())
                print(lines[i+1].strip())
                print(lines[i+2].strip())
                break

        if not self.found:
            print("No data found")  
                    


    def discharge(self):
        print(f"{'-'*20} discharge patient {'-'*20}")
        self.name2 = input("enter the name of the patient:: ").strip()

        self.found = False
        new_line = []

        with open("hospital.txt", "r") as f:
            lines = f.readlines()

            for i in range(0, len(lines), 5):
                block = lines[i:i+5]

                if len(block) < 2: 
                    continue

                name_line = block[1].strip()
                name = name_line.replace("NAME OF PATIEN::", "").strip()

                if self.name2.lower() == name.lower():
                    self.found = True
                    print(f"Patient data deleted: {name}")
                    continue  

                new_line.extend(block)

        with open("hospital.txt", "w") as f:
            f.writelines(new_line)

        if not self.found:
            print(" No patient with this name present in the list")

    def choise(self):
        match (self.num1):
            case 1:
                self.add_new_patient()
            case 2:
                self.view_patient_list()
            case 3:
                self.search_patient()
            case 4:
                self.discharge()
            case 5:
                print("thanks!! EXIT...")     



h=hospital()

h.choise()        
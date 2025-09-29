class employee:
    def __init__(self):
        print(f"{'-'*20} welcome to my employee system {'-'*20}")
        
    def choice(self):
        while True:
            print("1) Add Employee")
            print("2) View Employees")
            print("3) Search Employe")
            print("4) Update Employe")
            print("5) Delete Employe")
            print("6) Exit")

            try:
                choice = int(input("Select the option in digits 1,2...: "))
            except ValueError:
                print("Please enter a number")
                continue
            if choice == 1:
                self.add_employee()
            elif choice == 2:
                self.view_empole()
            elif choice == 3:
                self.search_employee()
            elif choice == 4:
                self.update_employee()
            elif choice == 5:
                self.delete_employee()
            elif choice == 6:
                print("Thanks for visiting!")
                break   
            else:
                print("Invalid choice, try again")

            
        
    
    def update_employee(self):
        self.idno2=input("enter the idno of the user:: ").strip()
        self.found=False
        with open("file_employee.txt","r")as f:
            line=f.readlines()
            self.new_line=[]
            for i in range(0,len(line),6):
                self.block = line[i:i+6]

                if self.idno2 in self.block[0]:
                    self.found=True
                    print("\n USER FOUND \n")
                    print(line[i].strip())
                    print(line[i+1].strip())
                    print(line[i+2].strip())
                    print(line[i+3].strip())
                    print(line[i+4].strip())
                    print(f"1)NAME. \n2)IDNO. \n3)SALARY. \n4)POST. \n5)EMAIL.")

                    self.change=input("what you want to update choice in 1,2,3...:: ")
                    self.change()


                    break

            if not self.found:
                print("no data found")

    def change(self):
        match self.change:
            case 1:
                self.name4=input("Enter the name of the new employee:: ")
                if not self.name4.replace(" "," ").isalnum():
                    print("NAME should only contain name and number and space ")
                self.block[2] = f"NAME:: {self.name4}\n"
            case 2:
                self.idno2=int(input("enter the id no of the new employee:: "))
                self.block[1] = f"NAME:: {self.idno2}\n"
            case 3:
                self.email2=input("enter the mail of the employee:: ")
                self.block[3] = f"NAME:: {self.email2}\n"
            case 4:
                self.salary2=input("enter the salary of the employee:: ")
                self.block[4] = f"NAME:: {self.salary2}\n"

            case 5:
                print("1)FIX.\n2)INTERNNSHIP ")
                self.post1=" "
                while True:

                    self.post2=int(input("select from the option:: "))   
                    if self.post2 in [1,2]:
                        if self.post2==1:
                            self.post1="fix"
                        else:
                            self.post1="internship"
                        break
                    else:
                        print("select from the given option ")
                self.block[5] = f"NAME:: {self.post2}\n"
        
        self.new_line.extend(self.block)
        with open("file_employee.txt", "w") as f:
            f.writelines(self.new_line)
      

    def add_employee(self):
        
        print(f"{'-'*20} ADD employee DATA {'-'*20}")
        self.name=input("Enter the name of the new employee:: ")
        if not self.name.replace(" "," ").isalnum():
            print("NAME should only contain name and number and space ")
        self.idno=int(input("enter the id no of the new employee:: "))
        try:
            self.salary=int(input("enter the salary of the employee:: "))
            if(self.salary<=0):
                print("the salary is not in negative")
        except ValueError:
            print("salary not be in nagative ")

        self.email=input("enter the mail of the employee:: ")
        print("1)FIX.\n2)INTERNNSHIP ")
        self.post1=" "
        while True:

            self.post=int(input("select from the option:: "))   
            if self.post in [1,2]:
                if self.post==1:
                    self.post1="fix"
                else:
                    self.post1="internship"
                break
            else:
                print("select from the given option ")
                    
             

        with open("file_employee.txt","a")as f:
            f.write(f"IDNO:: {self.idno}\n")
            f.write(f"NAME:: {self.name}\n")
            f.write(f"EMAIL:: {self.email}\n")
            f.write(f"SALARY:: {self.salary}\n")
            f.write(f"POST:: {self.post1}\n")
            f.write(f"{'-'*30}")

            
    def view_empole(self):
        
        print(f"{'-'*20} employee list {'-'*20}\n")

        with open("file_employee.txt","r")as f:
            for line in f:
                print(line.strip())

    def search_employee(self):
        print(f"\n{'-'*20} search the employee {'-'*20}\n")
        self.idno1=input("enter the id no of the employee:: ").strip()
        with open("file_employee.txt")as f:
            lines=f.readlines()
            found= False
            for i in range(0,len(lines),6):
                if self.idno1 in lines[i]:
                    found =True
                    print("USER FOUND \n")
                    print(lines[i].strip())
                    print(lines[i+1].strip())
                    print(lines[i+2].strip())
                    print(lines[i+3].strip())
                    print(lines[i+4].strip())

                    break
            if not found:
                print("NO USER FOUND BY THIS ID NO")  

    def delete_employee(self):
        print(f"\n{'-'*20} delete employee {'-'*20}\n")
        self.idno1=input("enter the id no of the employee:: ")

        with open("file_employee.txt")as f:
            lines=f.readlines()
            new_line=[]
            found= False
            for i in range(0,len(lines),6):
                if self.idno1 in lines[i]:
                    print(f"delete user: {lines[i].strip()}")
                    found =True
                    continue
                new_line.extend(lines[i:i+6])


            with open("file_employee.txt","w")as f:
                f.writelines(new_line)
            if not found:
                print("NO USER FOUND BY THIS ID NO")    
                    
    
e=employee()
e.choice()

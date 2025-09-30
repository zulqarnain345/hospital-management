class cafe:
    def __init__(self):
        print(f"{'-'*8} Welcome to the MY CAFE {'-'*8}")
        self.selected_dishes = []   # list to save multiple dish names
        self.selected_prices = []   # list to save multiple prices



    def menu(self):
        print("1) MANAGE THE MENU.")  
        print("2) TAKE THE ORDER. ") 
        print("3) VIEW SALE REPORT.")
        print("4) EXCIT.") 
        while True:
            self.select=int(input("select the function you want "
            "in the form of 1,2,3... "))
            if(self.select in [1,2,3,4]):
                break
            else:
                print("plz select from the give option") 
    
    def order(self):
        self.count=0
        print("MENU \n")
        self.read_menu()
        while True:
            self.dish=input("enter the name of the dish:: ")
            self.count=self.count+1
            dish_item=self.check_the_dish()
            if dish_item:
                break
            else:
                print("plz check the dish name again in the menu \n")
        while True:
            try:
                self.quality=int(input("enter the qualnity of the dish "))
                if self.quality <=0:
                    print("quantity must be positive and more then zero ")
                    continue
                break

            except ValueError:                                                   # ✅ added validation
                print("Quantity must be a number")
                return
        self.reorder()
    def reorder(self):   
        print("1)YES.")
        print("2)NO.")
        while True:
            try:
                self.order1=int(input("you want to order more yes or" \
                " no select from the option  "))
            except ValueError:
                    print("please enter a number (1 or 2)")
                    continue

            if self.order1==1:
                self.order()
            elif self.order1==2:
                print("THANKS FOR THE ORDER  YOU ORDER IS READY IN 10 MINT.")
                print(" ")
                self.bill()
                break    

            else:
                print("plz select from the option.")
    
    def total_bill(self):
        print(f"the total dish you enter is {self.count}")


    def bill(self):
        self.total_bill()
        print(" BILL  ")
        print(" ")
        self.total_price = 0

        for i in range(len(self.selected_dishes)):
            print(f"{i+1}) dish:: {self.selected_dishes[i]} = price:: {self.selected_prices[i]}")
            self.total_price += self.selected_prices[i]
        
        print("total price is: ",self.total_price)
        print("1)CASH.")
        print("2)CARD.")
        while True:
            self.payment_method=int(input("enter the payment mathod in 1,2: "))
            if self.payment_method not in [1,2]:
                print("plz select from the option ")
            if self.payment_method == 1:
                print("ON CASH 16% TAX INCLUDE ")
                self.total_amount=(0.16) * (self.total_bill)
                print(f"TOTAL AMOUNT AFTER TAX IS {self.total_amount}")
                break
            elif self.payment_method==2:
                print("ON CARD 6% TAX INCLUDE ")
                self.total_amount=0.6*self.total_bill
                print(f"TOTAL AMOUNT AFTER TAX IS {self.total_amount}")

                break


        
                    
    def check_the_dish(self):

        found=False
        with open("cafe.txt","r")as f:
            line=f.readlines()

        for i in range(0,len(line),3):
            item_line=line[i].replace("ITEM::", "").strip()
            item_price=line[i+1].replace("PRICE::", "").strip()

            if self.dish.lower() == item_line.lower():

                found=True
                self.selected_dishes.append(f"{item_line} x {self.quality}")  
                self.selected_prices.append(float(item_price) * self.quality) 
                return{"dish": item_line, "price": float(item_price * self.quality)}



        if not found:
             return None

        



                


                






    def manage_menu(self):
        print("MANAGE THE MENU\n")
        print("1) ADD NEW ITEM.")
        print("2) REMOVE THE ITEM.")

        while True:
            self.manage_menu_item=int(input("select the option by 1,2.. "))
            if self.manage_menu_item in [1,2]:
                
                break
            else:
                print("plz select from the given option")

        if(self.manage_menu_item==1):
            print(f"YOU SELECT THE OPTION 1 \n")
            self.read_menu()
            self.dish_name=input("enter the new dish name:: ")
            self.price=int(input("enter the price of the dish:: "))

            with open("cafe.txt","a")as f:
                f.write(f"ITEM:: {self.dish_name} 2 \n")
                f.write(f"PRICE:: {self.price} \n")
                f.write(f"{'-'*20}\n")
                print("ITEM ADD TO THE MENU \n")
            print("1) YES ")
            print("2) NO ")
            while True:  
                self.show=int(input("if you want to show read the menu " \
                "again select the optoin in 1,2 "))
                
                if(self.show==1):
                    self.read_menu() 
                    break
                elif(self.show==2):
                    print("NEW ITEM ADD TO THE MENU")
                    break
                else:
                    print("plz select from the option")      
        if(self.manage_menu_item==2):
            print(f"YOU SELECT THE OPTION 2 \n")
            self.remove_item()


    def remove_item(self):
        self.delete=input("enter the dish name that you want" \
        " to remove from the menu:: ")
        found=False
        new_lines=[]

        with open("cafe.txt","r")as f:
            line=f.readlines()

        for i in range(0,len(line),3):
            item_line=line[i].strip()
            item_price=line[i+1].strip()
            s=line[i+2]

            item_name = item_line.replace("ITEM::", "").strip()

            if item_name.lower()==self.delete.lower():
                print(f"delete item {item_line},{item_price}")
                found=True
                continue
            
            new_lines.extend([item_line + "\n", item_price + "\n", s])
        
        with open("cafe.txt","w")as f:
            f.writelines(new_lines)
        if not found:
            print(f"no item found with this name {self.delete}")   


    def read_menu(self):
            with open("cafe.txt","r")as f:
                print("YOR HOLE MENU IS THIS \n")
                for line in f:
                    data=f.read().strip()

                print(data)                       

    def select1(self):
        if(self.select==1):
           self.manage_menu()
        elif(self.select==2):
            self.order()
        elif(self.select==3):
            pass
        elif(self.select==4):
            pass        


c=cafe()

c.menu()
c.select1()


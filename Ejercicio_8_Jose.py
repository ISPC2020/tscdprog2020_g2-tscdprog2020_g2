class clientPortfolio:
    # Constructor
    def __init__(self, lst):
        # Attributes
        self.__customerList = lst

    # Methods
    # Menu
    def mainMenu(self):
        """This method shows the menu and allows to choose options """
        # Main loop
        while True:
            print("""
                        1)  Add Customer
                        2)  Customer List
                        3)  Search Customer
                        4)  Edit Customer
                        5)  Close Client Portfolio """)

            option = int(input("\nEnter the option: "))

            # Options
            if option == 1:
                self.addCustomer()
            elif option == 2:
                self.show()
            elif option == 3:
                idNumber = input("Enter the ID number: ")
                self.searchCustomer(idNumber)
            elif option == 4:
                self.editCustomer()
            elif option == 5:
                break

    def show(self):
        """This method allows to show all the clients of the portfolio """
        # In case the portfolio is empty
        if len(self.__customerList) == 0:
            print("\tEmpty portfolio")

        # Display loop
        for i in self.__customerList:
            print("-----------------------------")
            print("Name: ", i[0], "\nID: ", i[1], "\nPhone: ", i[2], "\nEmail: ", i[3])
            print("-----------------------------")

    def addCustomer(self):
        """This method allows adding customer (Name; ID number; Phone; Email)"""
        # Input information
        name = input("Enter contact name: ")
        ID_number = input("Enter ID number: ")
        phone = int(input("Enter contact phone: "))
        email = input("Enter contact Email: ")
        # Add to the list
        self.__customerList.append([name, ID_number, phone, email])

    def editCustomer(self):
        """This method allows to edit contacts according to their position """
        # Choose position
        ID_ToSearch = input("Enter contact number: ")
        position = self.__customerList.index(ID_ToSearch)

        # Delete the old customer and replace for edited customer
        self.__customerList.pop(position) and self.__customerList.insert(position, self.addCustomer())
        # Delete "None"
        for i in self.__customerList:
            if i is None:
                self.__customerList.remove(i)

    def searchCustomer(self, identificationNumber):
        """This method allows to search a customer for your ID number"""
        ID_ToSearch = identificationNumber
        # Search loop
        for i in self.__customerList:
            if ID_ToSearch in i:  # In case it matches, show
                print("-----------------------------")
                print("Name: ", i[0], "\nID: ", i[1], "\nPhone: ", i[2], "\nEmail: ", i[3])
                print("-----------------------------")

    def customerList(self):
        """This method return the customer list"""
        return self.__customerList


class bankAccount:
    # Constructor
    def __init__(self):
        self.__amount = 0
        self.__period_of_time = 0
        self.__interestRate = 0

    # Methods
    def show_customerInformation(self, identificationNumber, lst):
        """This method allows to display customer information through the ID number"""
        # Call the method of the 'clientPortfolio' class
        customerInfo = clientPortfolio(lst)
        customerInfo.searchCustomer(identificationNumber)
        print("Mount: ", self.__amount)

    def deposit(self, amount):
        """This methods allows to deposit money into the customer account"""
        self.__amount += amount

    def extract(self, amount):
        """This methods allows to extract money into the customer account"""
        self.__amount -= amount

    def fixedRent(self, amount, periodOfTime, interestRate):  # Plazo fijo
        """This method allow to constitute the fixedRent"""
        self.__amount = amount
        self.__period_of_time = periodOfTime
        self.__interestRate = interestRate

        # Calculating interest
        interest = (self.__amount * self.__interestRate) / 100  # Calculating interest

        # Information block
        print("Fixed rent")
        print("The interest earned: ", interest)
        print("Money available in ", self.__period_of_time, "days")
        print("Interest rate: ", self.__interestRate)


class bank:
    # Constructor
    def __init__(self):
        # Attributes
        self.clientPortfolio_lst = []
        self.__customers = []
        self.__customersList = {}
        self.__customer = None

    # Methods
    def operate(self):
        """This is the main method of execution"""
        # First loop, where the main functions are selected
        while True:
            print("""
            1) Client Portfolio

            2) Bank Accounts

            3) Close""")

            option = int(input("\nEnter the option: "))

            # Client portfolio
            if option == 1:
                portfolio = clientPortfolio(self.clientPortfolio_lst)
                portfolio.mainMenu()
                # Load the customer ID number in the list
                self.__customers = [i[1] for i in portfolio.customerList()]

            # Bank operations
            elif option == 2:
                # Converts ID number to objects and stores them in the dictionary
                for i in self.__customers:
                    self.__customersList[i] = bankAccount()

                # Input the Id number
                id_number = input("Enter the ID number: ")
                # Identify the customer by the id entered
                self.__customer = self.__customersList.get(id_number)

                # Second loop, where banking operations are selected
                while True:
                    print("""
                    1) Deposit
                    2) Extract
                    3) FixedRent
                    4) Show Information
                    5) back
                    """)

                    operateOption = int(input("\nEnter the option: "))

                    if operateOption == 1:
                        self.__customer.deposit(int(input("Enter the mount to deposit: ")))
                    elif operateOption == 2:
                        self.__customer.extract(int(input("Enter the mount to extract: ")))
                    elif operateOption == 3:
                        self.__customer.fixedRent(int(input("Enter the mount to deposit: ")),
                                                  int(input("Enter the period of time: ")),
                                                  float(input("Enter the interest rate: ")))
                    elif operateOption == 4:
                        self.__customer.show_customerInformation(id_number, self.clientPortfolio_lst)
                    # Go back to the previous loop
                    elif operateOption == 5:
                        break
            # End of execution
            elif option == 3:
                break


Terminal_1 = bank()
Terminal_1.operate()
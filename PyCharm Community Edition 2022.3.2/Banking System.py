class User:
    def __init__(self, first_name, last_name, gender, street_address, city,
                 email, cc_number, cc_type, balance, account_number):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.street_address = street_address
        self.city = city
        self.email = email
        self.cc_number = cc_number
        self.cc_type = cc_type
        self.balance = balance
        self.account_number = account_number
        userList.append(self)

    def displayInfo(self):
        print(self.first_name)
        print(self.last_name)
        print(self.gender)
        print(self.street_address)
        print(self.city)
        print(self.email)
        print(self.cc_number)
        print(self.cc_type)
        print(float(self.balance))
        print(self.account_number)


def generateUsers():
    import csv
    with open('bankUsers.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', quotechar="'")
        for line in filereader:
            User(line[0], line[1], line[2], line[3], line[4], line[5], line[6],
                 line[7], float(line[8]), line[9])


def findUser():
    user_to_find = input("enter tha name of the user:")
    for user in userList:
        if user.first_name + " " + user.last_name == user_to_find:
            user.displayInfo()
            return user
    print("No user was found with that name")
    return None


def overdrafts():
    overdrafters = 0
    total = 0
    for user in userList:
        if user.balance < 0:
            print(user.first_name + " " + user.last_name)
            overdrafters += 1
            total += user.balance
    print(overdrafters)
    print(f"{total:.2f}")


def missingEmails():
    idiots = 0
    for user in userList:
        if user.email == "":
            print(user.first_name + " " + user.last_name)
            idiots += 1
    print(idiots)


def bankDetails():
    losers = 0
    value = 0
    index_of_max = 0
    balance_max = 0
    index_of_min = 0
    balance_min = 0
    for i, user in enumerate(userList):
        losers += 1
        value += user.balance
        if user.balance > balance_max:
            index_of_max = i
            balance_max = user.balance
        if user.balance < balance_min:
            index_of_min = i
            balance_min = user.balance
    print(losers)
    print(f"{value:.2f}")
    print(index_of_max)
    print(index_of_min)


def transfer():
    from_account = input("Enter the account number from which you want to "
                         "transfer money: ")
    from_user = None
    for user in userList:
        if user.account_number == from_account:
            from_user = user
            break
    if from_user:
        print("Name:", from_user.first_name, from_user.last_name)
        print("Current balance:", from_user.balance)
    else:
        print("Account not found.")
        return
    amount = float(input("Enter the amount to transfer: "))
    if amount <= 0:
        print("Invalid amount.")
        return
    if amount > from_user.balance:
        print("Insufficient balance.")
        return
    to_account = input("Enter the account number to transfer money to: ")
    to_user = None
    for user in userList:
        if user.account_number == to_account:
            to_user = user
            break
    if to_user:
        print("Name:", to_user.first_name, to_user.last_name)
    else:
        print("Account not found.")
        return
    from_user.balance -= amount
    to_user.balance += amount
    print("Transfer successful.")
    print(from_user.first_name, from_user.last_name, "new balance:", from_user)


userList = []
generateUsers()

userChoice = ""
print("Welcome")

while userChoice != "Q":
    print("What function would you like to run?")
    print("Type 1 to find a user")
    print("Type 2 to print overdraft information")
    print("Type 3 to print users with missing emails")
    print("Type 4 to print bank details")
    print("Type 5 to transfer money")
    print("Type Q to quit")
    userChoice = input("Enter choice: ").upper()
    print()

    if userChoice == "1":
        findUser()
    elif userChoice == "2":
        overdrafts()
    elif userChoice == "3":
        missingEmails()
    elif userChoice == "4":
        bankDetails()
    elif userChoice == "5":
        transfer()
    print()

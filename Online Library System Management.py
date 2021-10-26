# create object book with 2 attributes:
# name of the book
# & number of copies available
class Book:
    def __init__(self, name, num_avail):
        self.name = name
        self.num_avail = num_avail

# create paton object with 3 attributes:
# name of the patron,
# the list of books he/she checks out,
# & money he/she owes
class Patron:
    def __init__(self, name):
        self.name = name
        self.cobooks = {}
        self.acct_bal = 0

    # calculate the money owed by the patron
    def PayFees(self, amount):
        # the amount the patron wants to pay
        self.amount = amount
        # the amount left he/she must pay
        self.acct_bal -= self.amount

    def DailyUpdate(self):
        # Each time DailyUpdate is run, add 1 to the number of days the book is checked out
        for i in self.cobooks:
            self.cobooks[i] += 1
            # if the book has not been checked after every 5 days,
            # charge the patron 12 dollars each time
            if self.cobooks[i] % 5 ==0:
                self.acct_bal += 12

# create the library object combining books and patrons
class Library:
    def __init__(self):
        self.patrons = []
        self.books = []

    # CheckOut takes 2 objects: book & patron as inputs
    def CheckOut(self, book, patron):
            # access and check the number of copies available of the book object
            if book.num_avail == 0:
                print("No copies left!")
            # access the names of all the books checked out by the patron,
            # to check if the one
            elif book.name in patron.cobooks.keys():
                print("You already have this book!")
            # access the number of books the patron already checked out,
            # to check if it reaches the maximum quantities or not.
            elif len(patron.cobooks) > 2:
                print("You have checked out the maximum number of books!")
            # otherwise,
            # add the book to the list of checked out books of the patron
            # the number of copies available of it decreases by 1
            else:
                patron.cobooks[book.name] = 0
                book.num_avail -= 1

    # CheckIn takes 2 objects: book & patron as inputs
    def CheckIn(self, book, patron):
        # access the names of the books the patron checked out
        # to check if the one checked in had been checked out
        if book.name not in patron.cobooks.keys():
            print("You can't check in a book that wasn't checked out!")
        # 'if it had been checked out, remove it out of the list of checked out books of the patron
        # the number of copies available of it increases by 1
        else:
            patron.cobooks.pop(book.name)
            book.num_avail += 1


    def DailyUpdate(self):
        # loop through the patrons,
        for i in self.patrons:
            # then run DailyUpdate each of them
            i.DailyUpdate()

    # FindPatron takes the names of the patrons,
    # then check if they are in the library system
    def FindPatron(self, name):
        for i in self.patrons:
            if name in i.name:
                return i
        return 0

    # FindBook takes the names of the books,
    # then check if they are in the library system
    def FindBook(self, name):
        for i in self.books:
            if name in i.name:
                return i
        return 0

    # view all information
    def ViewRecords(self):
        # view all books:
        print("Book Records:\n")
        # their names and their available copies
        for i in self.books:
            print("Name: ", i.name, ", Copies: ", i.num_avail)
        # view all patrons:
        print("Patron List:\n")
        # their names, account balance & the days  their checked out books have been checked out
        for i in self.patrons:
            print("Name: ", i.name, ", Account Balance: ", i.acct_bal)
            for j in i.cobooks:
                print("{0} checked out for {1} day(s)".format(j, i.cobooks[j]))



if __name__ == "__main__":
    library = Library()
    library.books.append(Book("Pythons in the Wild", 3))
    library.books.append(Book("Gems and Perls", 1))
    library.books.append(Book("Ada Karenina", 4))
    library.books.append(Book("The Old Man and the C", 2))
    library.patrons.append(Patron("Bob"))
    library.patrons.append(Patron("Sally"))




    while True:
        print("Welcome to the automated Library system!")
        print("1) Log in as Administrator")
        print("2) Log in as Patron")
        choice = input("Please choose an option above (or enter q to quit): ")
        if choice == "q":
            break
        if choice == "1":
            print("--------------------")
            print("Hello Administrator!")
            while True:
                print("1) View Records")
                print("2) Perform Daily Update")
                choice = input("Please choose an option above (or enter q to logout): ")
                if choice == "q":
                    break
                elif choice == "1":
                    library.ViewRecords()
                elif choice == "2":
                    print("Performing Daily Update.....")
                    library.DailyUpdate()
        if choice == "2":
            while True:
                name = input("Please enter your name (or enter q to quit): ")
                if name == "q":
                    break
                patron = library.FindPatron(name)
                if patron == 0:
                    print("This patron name is not on file...")
                else:
                    while True:
                        print("--------------------")
                        print("Welcome {}!".format(patron.name))
                        print("1) Find a book to check out or in")
                        print("2) View and pay fees")
                        choice = input("Please choose an option above (or enter q to logout): ")
                        if choice == "q":
                            break
                        elif choice == "1":
                            while True:
                                name = input("Enter the name of a book (or enter q to go back): ")
                                if name == "q":
                                    break
                                book = library.FindBook(name)
                                if book == 0:
                                    print("This book name is not on file...")
                                else:
                                    print("1) Check out this book")
                                    print("2) Check in this book")
                                    choice = input("Please choose an option above (or enter q to go back): ")
                                    if choice == "q":
                                        continue
                                    elif choice == "1":
                                        library.CheckOut(book, patron)
                                    elif choice == "2":
                                        library.CheckIn(book, patron)
                        elif choice == "2":
                            print("Your account balance is: {}".format(patron.acct_bal))
                            amount = float(input("Enter how much you'd like to pay at this time (or enter 0 to go back): "))
                            patron.PayFees(amount)

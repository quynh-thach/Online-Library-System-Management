class Library:
    def __init__(self):
        self.customers = []
        self.books = []


    def CheckOut(self, book, patron):
        if book.num_avail == 0:
            print("No copies left!")
            
        elif book.name in patron.cobooks.keys():
            print("You already have this book!")
        
        elif len(patron.cobooks) > 2:
            print("You have checked out the maximum number of books!")
         
        else:
            patron.cobooks[book.name] = 0
            book.num_avail -= 1

  
    def CheckIn(self, book, patron):
        if book.name not in patron.cobooks.keys():
            print("You can't check in a book that wasn't checked out!")
       
        else:
            patron.cobooks.pop(book.name)
            book.num_avail += 1


    def DailyUpdate(self):
        for i in self.customers:
            i.DailyUpdate()

   
    def FindCustomer(self, name):
        for i in self.customers:
            if name in i.name:
                return i
        return 0

   
    def FindBook(self, name):
        for i in self.books:
            if name in i.name:
                return i
        return 0

   
    def ViewRecords(self):
        print("Book Records:\n")
        for i in self.books:
            print("Name: ", i.name, ", Copies: ", i.num_avail)
        print("Customer Records:\n")
        for i in self.patrons:
            print("Name: ", i.name, ", Account Balance: ", i.acct_bal)
            for j in i.cobooks:
                print("{0} checked out for {1} day(s)".format(j, i.cobooks[j]))

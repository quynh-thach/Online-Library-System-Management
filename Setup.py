if __name__ == "__main__":

'''
Use the following syntax to add the more records of books and customers
'''

    library = Library()
    library.books.append(Book("Pythons in the Wild", 3))
    library.books.append(Book("Gems and Perls", 1))
    library.books.append(Book("Ada Karenina", 4))
    library.books.append(Book("The Old Man and the C", 2))
    library.customers.append(Patron("Bob"))
    library.customers.append(Patron("Sally"))




    while True:
        print("Welcome to the Online Library System!")
        print("Enter 1 to log in as Administrator")
        print("Enter 2 to log in as Customer")
        print("Enter Q to quit")
        
        choice = input("Please choose an option above: ")
        if choice == "Q":
            break
            
        if choice == "1":
            print("--------------------")
            print("Hello Administrator!")
            while True:
                print("Enter 1 to 'view records'")
                print("Enter 2 to see 'daily update'")
                print("Enter Q to quit")
                
                choice = input("Please choose an option above: ")
                
                if choice == "Q":
                    break
                    
                elif choice == "1":
                    library.ViewRecords()
                    
                elif choice == "2":
                    print("Updating...")
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
                        print("Welcome {}!".format(customer.name))
                        print("Press 1 to to check out or in")
                        print("Press 2 to view and make a payment")
                        print("Enter Q to quit")
                        
                        choice = input("Please choose an option above: ")
                        
                        if choice == "Q":
                            break
                            
                        elif choice == "1":
                            while True:
                                name = input("Enter the name of a book (or enter Q to go back): ")
                                if name == "Q":
                                    break
                                book = library.FindBook(name)
                                if book == 0:
                                    print("Not on file...")
                                else:
                                    print("Enter 1 to check out")
                                    print("Enter 2 to check in")
                                    print("Enter Q to quit")
                                    
                                    choice = input("Please choose an option above: ")
                                    if choice == "Q":
                                        continue
                                        
                                    elif choice == "1":
                                        library.CheckOut(book, patron)
                                        
                                    elif choice == "2":
                                        library.CheckIn(book, patron)
                                        
                        elif choice == "2":
                            print("Your account balance is: {}".format(customer.acct_bal))
                            amount = float(input("Enter your payment (or enter 0 to go back): "))
                            customer.PayFees(amount)

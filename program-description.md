# OVERVIEW
In the library system, the **name** and the **number of copies** of a book is recorded. Books are available for being checked out and in. The **MAXIMUM** number of books can be checked out at a time is **3**. A customer can check out only **ONE** copy of a specific book. A book MUST be checked back in by day 7 after being checking out. After 7 days, if it is not yet checked back in, a **penalty fee** of **$15** is added to one's account balance. Those checking books out have an **account balance** used to make payments. The **library administrator** can: 1) view the records of the books, 2) view the records of the customers, 3) look up specific books or customers, 4) update the account balances everyday.

# PSEUDOCODE 
## BOOK OBJECT
1. Create a function to record for a book:
  - Parameters: name, number of copies available.

## CUSTOMER OBJECT
2. Create a function to record a customer:
  - Parameters: name, checked-out books, account balance.
3. Create a function for payment:
  - Parameters: payment.
  - Output: updated account balance.
4. Create a function to update the record of the customer everyday:
  * Each time the function is run, date increases by 1.
  * After 7 days,charge $15 if not check in what checked out. 

## LIBRARY PROCEDURE OBJECT
5. Create 2 empty lists for books and customers.
  * add data later. 
6. Create a function for check-out procedure
  - Parameters: book, customer
7. Create a function for check-in procedure
  - Parameters: book, customer
8. Create a function for daily update.
   * used to tracking check-out days.
9. Create a function to see if a customer is in the library system.
  - Arguments: the name of the customer.
10. Create a function to look up a specific book.
  - Arguments: name of the book.
11. Create a function to see all kinds of records.
  
## LIBRARY SYSTEM SETUP
   Use if/else to control the flow of procedures.

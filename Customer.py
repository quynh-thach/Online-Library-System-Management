class Customer:
    def __init__(self, name):
        self.name = name
        self.cobooks = {}
        self.acct_bal = 0
        
    def PayFees(self, pay):
        self.pay = pay
        self.acct_bal -= self.pay

    def DailyUpdate(self):
        for i in self.cobooks:
            self.cobooks[i] += 1
            if self.cobooks[i] % 7 ==0:
                self.acct_bal += 15

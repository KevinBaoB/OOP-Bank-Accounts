from account import Account

class SavingsAccount(Account):
    def __init__(self, ID, balance,date):
        super().__init__(self, ID, balance,date)
        if self.balance < 10:
            raise Exception("Cannot have savings less than 10$!")
    
    
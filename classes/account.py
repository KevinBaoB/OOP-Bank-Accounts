import csv
import os


class Account:
    def __init__(self, ID, balance, date):
        self.ID = ID
        if int(balance) < 0:
            raise Exception("You cannot input a NEGATIVE account balance!")
        else:
            self.balance = balance
            self.date = date


    def withdraw(self, amount):
        if self.balance < amount:
            raise Exception("\nWARNING ATTEMPTING OVERDRAFT! \n You cannot withdraw more than you have in your account.\n")
        else:
            self.balance = self.balance - amount
            return f"You withdrew ${amount}.\nYour new account balance is ${self.balance}.\n"
        
    def __repr__(self):
        return f"""
        ID: {self.ID}
        Account Balance: {self.balance}
        Date Account Made: {self.date}
        """
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        return f"You deposited ${amount}.\nYour new account balance is ${self.balance}.\n"
    
    def get_account_balance(self):
        return f"\nYou have ${self.balance} in your account\n________________________________\n"
    
    def get_account_made_date(self):
        return self.date

    def find_id(ID):
        the_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(the_path, '../support/account_owners.csv')
        with open(path) as id_files:
            account_id_reader = csv.DictReader(id_files)
            for id in account_id_reader:
                if int(id["account_id"])== ID:
                    return id["owner_id"]

    

    @classmethod
    def all_accounts(cls):
        the_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(the_path, '../support/accounts.csv')
        with open(path) as account_files:
            account_reader = csv.DictReader(account_files)
            accounts_arr = []
            for account in account_reader:
                accounts_arr.append(Account(**dict(account)))
            return accounts_arr


# print(Account.find_id(1215))
# print(Account.all_accounts())
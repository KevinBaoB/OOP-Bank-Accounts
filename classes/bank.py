from account import Account
from owner import Owner

class Bank:
    def __init__(self, name):
        self.name = name

    def get_owner_by_id(self, id_number):
        owner_num = Account.find_id(id_number)
        
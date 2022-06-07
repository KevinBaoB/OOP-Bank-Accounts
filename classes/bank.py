from account import Account
from owner import Owner

class Bank:
    def __init__(self, name):
        self.name = name

    def get_owner_by_id(id_number):
        owner_num = Account.find_id(id_number)
        for owner in Owner.all_owners():
            if int(owner["owner_ID"]) == id_number:
                return f"""
                {owner["first_name"]} {owner["last_name"]}
                """

print(Bank.get_owner_by_id(14))
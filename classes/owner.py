import csv
import os
from account import Account

class Owner:
    def __init__(self,owner_ID, last_name, first_name, street_address, city, state):
        self.owner_ID = owner_ID
        self.last_name = last_name
        self.first_name = first_name
        self.street_address = street_address
        self.city = city
        self.state = state

    def __repr__(self):
        return self.owner_ID, self.first_name, self.last_name
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"



    @classmethod
    def all_owners(cls):
        the_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(the_path, '../support/owners.csv')
        with open(path) as owner_files:
            owner_reader = csv.DictReader(owner_files)
            owner_arr = []
            for owner in owner_reader:
                owner_arr.append(owner)
            return owner_arr

print(Owner.all_owners())
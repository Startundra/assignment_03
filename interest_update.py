"""
Description: Applies interest rate to users accounts
Author: Isaac Reid 
Date: 01/10/23
Usage: Run in the terminal
"""

import pprint

# Global variables
accounts_list = []

# Class which holds acc. info
class Account:
    def __init__(self, account_number, balance, interest_rate):
        self.account_number = str(account_number)
        self.balance = float(balance)
        self.interest_rate = float(interest_rate)

    # Will change balance by amount without checking for funds
    def update_balance(self, amount):
        self.balance += amount      
    
    #
    def apply_monthly_interest(self, flag_print_balance):
        opening_balance = self.balance
        self.balance += (self.balance * self.interest_rate) / 12
        if flag_print_balance:
            print(
                f"\nOpening Balance: {opening_balance}" +
                f" Closing Balance: {self.balance}"  +
                f" ({self.interest_rate}% interest earned)\n")
# Returns a dictionary of account balances
def read_account_balances():
    account_balances = {}
    account_balances_file = open("account_balances.txt")

    for line in account_balances_file:
        
        account = ""
        balance = ""
        flag_balance = False

        #
        for char in line:

            if char == "|": 
                flag_balance = True
            
            elif flag_balance:
                balance += str(char)

            else:
                account += str(char)
        balance = float(balance)
        account_balances.update({account:balance})
    account_balances_file.close()
    return account_balances

# doesnt create anything actually it just populates i'm such a fraud
def create_accounts(balance_dictionary):
    global accounts_list

    for key in balance_dictionary:
        if  balance_dictionary[key] < 0:                   # item[1] == account_balance
            interest_rate = 10
        elif balance_dictionary[key] < 1000:
            interest_rate = 1
        elif balance_dictionary[key] < 5000:
            interest_rate = 2.5
        elif balance_dictionary[key] < 10000:
            interest_rate = 5
        else:
            pass
        accounts_list.append(Account(key, balance_dictionary[key], interest_rate))

# Does converting to class and then back going back to dict for printing count as petty?
def print_accounts_pretty():          
    global accounts_list
    accounts_pretty_dict = {}
    for acc in accounts_list:               # acc == account'
        accounts_pretty_dict.update({
            acc.account_number:{
                acc.balance, 
                acc.interest_rate
                }
            })
    print(len(accounts_list))
    pprint.pprint(accounts_pretty_dict)

# Populate accounts list
create_accounts(read_account_balances())

# pretty print
print_accounts_pretty()

#interest update
for acc in accounts_list:
    acc.apply_monthly_interest(False)

#Pretty Print 2: Electric boogaloo
print_accounts_pretty()

"""
Description: <<placeholder>>
Author: Isaac Reid 
Date: 01/10/23
Usage: Run in the terminal
"""

account_balances = {}



def read_account_balances():

    account_balances_file = open("account_balances.txt")

    for line in account_balances_file:
        global account_balances
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

        account_balances.update({account:balance})

read_account_balances()

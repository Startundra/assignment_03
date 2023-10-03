"""
Description: Applies interest rate to users accounts
Author: Isaac Reid 
Date: 01/10/23
Usage: Run in the terminal
"""
import time
import pprint
import datetime
import csv
# Global variables
accounts_list = []
csv_file_string = ""

# Class which holds acc. info
class Account:

    # duh doy its bob the constructor
    def __init__(self, account_number, balance, interest_rate):
        self.account_number = str(account_number)
        self.balance = float(balance)
        self.interest_rate = float(interest_rate)

    # Will change balance by amount without checking for funds
    def update_balance(self, amount):
        self.balance += amount      
    
    # applies monthly interest and overwrites the balance value of self
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

# generates a valid csv filename for the current date and returns as a string
def generate_csv_filename(first_name, last_name):
    current_time = datetime.datetime.now()
    csv_filename = (
        str(current_time.year)
        + "-"
        + str(current_time.month)
        + "-"
        + str(current_time.day)
        + "-"
        + str(first_name[0]).upper(), str(last_name[0]).upper()
        + ".csv"
    )
    return csv_filename

# Writes a CSV file using current accounts class list
def write_csv_file():
    global accounts_list
    with open(str(generate_csv_filename("john", "doe")), "w", newline = '') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Account", "Balance"])
        for acc in accounts_list:
            csv_writer.writerow([acc.account_number, acc.balance])
        csv_file.close()
            
# Generates a csv_dict and prints it, does not save the dictionary
def generate_csv_dict(csv_filepath):
    with open (str(csv_filepath)) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print({row["Account"], row["Balance"]})
    return None

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

# Pretty Print 2: Electric boogaloo
print_accounts_pretty()

# CSV File
csv_file_string = generate_csv_filename("Robertson", "Screwdriver")
write_csv_file()

# CSV Dict
generate_csv_dict("('2023-10-3-J', 'D.csv')")
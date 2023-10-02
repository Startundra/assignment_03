"""
Description: <<placeholder>>
Author: Isaac Reid
Date: 27/09/23
Usage: Spread on bread like butter (or run in the terminal)git 
Notes: ATM width is 40 chrs
"""
import random as r
transaction_optiosn = ["D", "W", "Q",]

users_current_balance = float(r.randint(-1000, 10000))

user_is_quitter = False


# gets users choice from the manu
def interface_main():
    print(
        """
        ***************************************         
                PIXELL RIVER FINANCIAL
                    ATM Simulator
        Your current balance is: $#,###.##

                    Deposit: D
                    Withdraw: W
                    To Quit: Q
        ***************************************
        """)

while not user_is_quitter:
    break
"""
Description: <<placeholder>>
Author: Isaac Reid
Date: 27/09/23
Usage: Spread on bread like butter (or run in the terminal)git 
Notes: ATM width is 40 chrs
"""

import random as r
import os
from time import sleep

transaction_options = ["D", "W", "Q",]
users_current_balance = float(r.randint(-100000, 1000000))/100
user_is_quitter = False


# gets users choice from the menu
def interface_main():
    global users_current_balance

    print(
        f"""
        ***************************************         
                PIXELL RIVER FINANCIAL
                    ATM Simulator
        Your current balance is: ${"%.2f" % users_current_balance}

                    Deposit: D
                    Withdraw: W
                    To Quit: Q
        ***************************************
        """)
    
    done = False
    while not done: 
        global user_is_quitter

        try: 
            menu_choice = input("Enter your selection: ").upper()

        except:
            print("""
                ***************************************
                            INVALID SELECTION
                ***************************************
                  """)
            
        else:

            # ----------------Deposit----------------------
            if menu_choice[0] == "D":
                transaction_amount = float(input("Enter the amount of transaction: "))
                users_current_balance += transaction_amount
                print(
                    f"""         
                    ***************************************
                    Your current balance is: ${"%.2f" % users_current_balance}
                    ***************************************
                    """
                )

            # ----------------Withdraw---------------------
            elif menu_choice[0] == "W":
                transaction_amount = float(input("Enter the amount of transaction: "))

                if transaction_amount > users_current_balance:
                    print(
                        """
                        ***************************************
                        INSUFFICIENT FUNDS
                        ***************************************
                        """)
                    
                else:
                    users_current_balance -= transaction_amount
                    print(
                        f"""
                        ***************************************
                        Your current balance is: ${"%.2f" % users_current_balanced}
                        ***************************************
                        """
                    )

            # -------------------------Quit----------------------
            elif menu_choice[0] == "Q":
                user_is_quitter = True
                done = True
                
            else:
                print(
                    """
                    ***************************************
                                INVALID SELECTION
                    ***************************************
                    """
                )
            
                


while not user_is_quitter:
    interface_main()

sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')


quit()
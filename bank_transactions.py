"""
Description: <<placeholder>>
Author: Isaac Reid
Date: 27/09/23
Usage: Spread on bread like butter (or run in the terminal)git 
Notes: ATM width is 40 chrs
"""

import random as r
transaction_optiosn = ["D", "W", "Q",]

users_current_balance = float(r.randint(-100000, 1000000))/100

user_is_quitter = False


# gets users choice from the manu
def interface_main():
    global users_current_balance

    print(
        f"""
        ***************************************         
                PIXELL RIVER FINANCIAL
                    ATM Simulator
        Your current balance is: ${users_current_balance:2}

                    Deposit: D
                    Withdraw: W
                    To Quit: Q
        ***************************************
        """)
    
    done = False
    while not done: 

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
                    Your current balance is: ${users_current_balance:2}
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
                        Your current balance is: ${users_current_balance:2}
                        ***************************************
                        """
                    )

            # -------------------------Quit----------------------
            elif menu_choice[0] == "Q":

                #return "Q"
                quit()

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



quit()
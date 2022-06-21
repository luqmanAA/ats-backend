# Write a program that simulates a bank USSD application. A user interacting with your program should be able to 
# a) Check balance b) Transfer cash c) Load airtime d) Load data e) Generate a four-digit otp  Note: All action must authorise with a pin.
# The user must set a transaction pin initially

import random

try:
    pin = input("Welcome, kindly set your 4-digit PIN: ")
    global balance
    balance = 5000
    def ussd_app():
        service_options = {
            1: check_balance,
            2: transfer_cash,
            3: load_airtime,
            4: load_data,
            5: generate_otp
            }
        selected_service = int(input("Please select an option:\
            \n1. - Check balance\
            \n2. - Transfer Cash\
            \n3. - Load airtime\
            \n4. - Load data\
            \n5. - Generate OTP \n"))
        if selected_service in service_options:
            return service_options[selected_service]()
        else: return "No such service"

    ## Check balance

    def check_balance():
        entered_pin = input("Enter PIN at N10 charge to confirm: ")
        if entered_pin == pin:
            return (f"Your account balance is: {balance - 10}")
        return ("The PIN you entered is invalid")

    ## Transfer cash
    def transfer_cash():
        amount = int(input("Enter the amount to transfer: "))
        account_number = input("Enter the account number: ")
        entered_pin = input(f"You want to transfer N{amount} to {account_number}, kindly enter your PIN to confirm: ")
        if entered_pin == pin:
            # balance -= amount
            return (f"Your transfer of N{amount} to {account_number} is successful")
        return ("The PIN you entered is invalid")

    ## Load Airtime for self and third-party
    def load_airtime(): 
        selected_receiver = int(input("Purchase airtime for: \n1. - Self \n2. - Third party \n0. - Back\n"))
        if selected_receiver == 0:
            return ussd_app()

        elif selected_receiver == 1:
            entered_pin = input("Enter PIN to continue: ")
            if entered_pin == pin:
                airtime_amount = int(input("Enter the amount (50 - 10000): "))
                # balance -= airtime_amount
                return (f"Your transaction is being processed.")
            return ("The PIN you entered is invalid")

        elif selected_receiver == 2:
            entered_pin = input("Enter PIN to continue: ")
            if entered_pin == pin:
                beneficiary_number = int(input("Enter the beneficiary phone number: "))
                airtime_amount = int(input("Enter the amount (50 - 10000): "))
                # balance -= airtime_amount
                return (f"Your transaction is being processed.")
            return ("The PIN you entered is invalid")

    ## Load Data for self and third-party
    def load_data():
        selected_receiver = int(input("Purchase data for: \n1. - Self \n2. - Third party \n 0. - Back \n"))
        data = {
            1: ["1GB for 1 day", 300],
            2: ["350MB for 7 days", 300],
            3: ["1.5GB for 30days", 1000],
            4: ["2GB for 30 days", 1200],
            5: ["3GB for 30 days", 1500],
            6: ["6GB for 30 days", 2500]
            }
        if selected_receiver == 0:
            return ussd_app()

        elif selected_receiver == 1:
            entered_pin = input("Enter PIN to continue: ")
            if entered_pin == pin:
                data_amount = int(input("Select bundle: \
                    \n1. - 1GB 1day N300 \
                    \n2. - 350MB 7 days N300\
                    \n3. - 1.5GB 30days N1000\
                    \n4. - 2GB 30 days N1200\
                    \n5. - 3GB 30 days N1500\
                    \n6. - 6GB 30 days N2500 \
                    \n0. - Back \n"))

                if data_amount == 0:
                    return ussd_app()
                # balance -= data[data_amount][1]
                return f"Your subscription of {data[data_amount][0]} was successful."
            return ("The PIN you entered is invalid")

        elif selected_receiver == 2:
            entered_pin = int(input("Enter PIN to continue: "))
            if entered_pin == pin:
                beneficiary_number = int(input("Enter the beneficiary phone number: "))
                data_amount = int(input("Select bundle: \
                    \n1. - 1GB 1day N300 \
                    \n2. - 350MB 7 days N300\
                    \n3. - 1.5GB 30days N1000\
                    \n4. - 2GB 30 days N1200\
                    \n5. - 3GB 30 days N1500\
                    \n6. - 6GB 30 days N2500 \
                    \n 0. - Back \n"))

                if data_amount == 0:
                    return ussd_app()
                return f"Your subscription of {data[data_amount]} was successful."
            return ("The PIN you entered is invalid")

    #Generate OTP
    def generate_otp():
        entered_pin = input("Enter PIN to receive your OTP: ")
        if entered_pin == pin:
            otp = [str(random.randint(0,9)) for n in range(4) ]
            return(f"Your OTP is {''.join(otp)} and it's valid for 60 seconds")
        return ("The PIN you entered is invalid")

    print(ussd_app())

except KeyboardInterrupt:
    print("\nGoodbye. Thanks for banking with us")
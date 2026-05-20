print("Welcome")
print("1.Buy Airtime/Data")
print("2.Pay Bills")
print("3.Send Money")
print("4.Settings")
print("5.Check Balance")
print("6.Exit")

balance = 4000
bank_pin=1234

choice=input("Enter one of the option")
if choice == "1":
    print("1.Buy Airtime for self")
    print("2.Buy Airtime for others")
    print("3.Buy Data Bundle")
    airtime=input("Pick an option")

    if airtime == "1":
        amount=int(input("Enter amount"))
        if amount > balance:
            print("Insufficient balance")
        else:
            pin=int(input("Enter your pin"))
            if pin == bank_pin:
                print(f"{amount} airtime added to your line")
                balance -=amount
                print(f"Your new balance is {balance}")
            else:
                print("Incorrect Pin. Transaction Cancelled")
    elif airtime == "2":
        phone_number=int(input("Enter Beneficiary phone number(11 digits)"))
        if phone_number != 11:
            print("Invalid phone number! Use 11 digits")
        else:
            amount=int(input("Enter your amount: "))
            if amount > balance:
                print("Insufficient balance")
            else:
                pin=int(input("Enter your pin"))
                if pin == bank_pin:
                    print(f"{amount} airtime sent to {phone_number}")
                    balance -=amount
                    print(f"Your balance is {balance}")
                else:
                    print("Incorrect Pin.Transaction cancelled")
    elif airtime == "3":
        print("\n Select Your Data Bundle")
        print("1.100MB-NGN100 (1days)")
        print("2.200MB-NGN200 (3days)")
        print("3.300MB-NGN300 (7Days)")                
        print("4.350MB-NGN300 (7Days)")
        option=input("Select your data plan:")
        if option == "1":
            amount_data= 100
            bundle ="100MB"
            validity= "1days"
        elif option == "2":
            amount_data= 200
            bundle ="200MB"
            validity="3days"
        elif option == "3":
            amount_data= 300
            bundle ="300MB"
            validity="7days"
        elif option == "4":
            amount_data= 300
            bundle ="350MB"
            validity="7days"
        if option in ["1","2","3","4"]:
            if amount_data > balance:
                print("Insufficient balance")#
            else:
                pin = int(input("Enter your pin"))
                if pin == bank_pin:
                    balance -=amount_data
                    print(f"You have successfully purchase {bundle} data bundle,valid for {validity}")
                    print(f"Your new blance is {balance}")
                else:
                    print("Incorrect pin.Transaction cancelled")
elif choice =="2":
    print("1.DSTV/GOTV subscription")
    print("2.Electricity Bill")
    bill=input("Enter your option")
    if bill == "1":
        print("1.DSTV")
        print("2.GOTV")
        tv=input("Enter your choice")
        if tv == "1" or tv == "2":
            tv_card=input("Enter your smartcard number: ")
            amount=int(input("Enter your amount: "))
            if amount > balance:
                print("Insufficient Balance")
            else:
                tv_pin=int(input("Enter your pin"))
                if tv_pin == bank_pin:
                    balance -=amount
                    print(f"{'DSTV' if tv == '1' else 'GOTV'} subscription of NGN {amount} renewed successfully")
                else:
                    print("Incorrect pin.Transaction cancelled")
    elif bill == "2":
        meter_number=int(input("Enter your meter number: "))
        amount=int(input("Enter amount"))
        if amount > balance:
            print("Insufficient balance")
        else:
            pin=int(input("Enter your pin"))
            if pin == bank_pin:
                print(f"Electricity bill of NGN {amount} paid for meter {meter_number}")
                balance -=amount
                print(f"Your new balance is {balance}")
            else:
                print("Incorrect Pin. Transaction Cancelled")
elif choice == "3":
    print("1.Transfer to Other bank")
    print("2.Transfer to same bank")
    transfer=int(input("Choose: "))
    if transfer == "1":
        account=input("Enter account number: ")
        if account == 10:
            bank_name=input("Enter bank name")
            amount=int(input("Enter amount: "))
            if amount > 0:
                pin=int(input("Enter pin: "))
                if pin == bank_pin:
                    print(f"NGN {amount} sent to {account}")
                else:
                    print("Incorrect pin")
            else:
                print("Invalid amount,try again")
    elif transfer == "2":
         account=input("Enter account number: ")
         if account == 10:
            amount=int(input("Enter amount: "))
            if amount > 0:
                pin=int(input("Enter pin: "))
                if pin == bank_pin:
                    print(f"NGN {amount} sent to {account}")
                else:
                    print("Incorrect pin")
            else:
                print("Invalid amount,try again")
    else:
        print("Invalid option")
elif choice =="4":
    print("SETTINGS")
    print("1.change pin")
    settings=int(input("Choose: "))
    if settings =="1":
        new_pin=int(input("Enter your new pin: "))
        confirm_pin=int(input("Confirm new pin: "))
        if new_pin == confirm_pin:
            pin = new_pin
            print("Pin changed successfully")
        else:
            print("Pin do not match.Please try again")
elif choice == "5":
    pin=int(input("Enter your pin: "))
    if pin == bank_pin:
        print(f"Your balance is NGN {balance}")
    else:
        print("Incorrect pin")
elif choice == "6":
    print("Thank you for banking with us")
else:
    print("Invalid Input")
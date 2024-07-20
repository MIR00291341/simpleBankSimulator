import random

accounts = {}
opt = "y"

while opt == "y":
    print("\n Welcome to My Bank \n1. Create Account \n2. Deposit \n3. Withdraw \n4. Check Balance \n5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        account = input("Enter name: ")
        num = random.randint(10000, 99999)
        balance = int(input("Enter Intial Deposit Amount: "))
        accounts[num] = {"name": account, "balance":balance}
        print("Account details:", account, num, accounts[num]["balance"])

    elif choice == "2":
        num = int(input("Enter account number: "))
        if num in accounts:
            dep = float(input("Enter deposit amount: "))
            accounts[num]["balance"] += dep
            print("Mr.",accounts[num]["name"],"You have Deposited successfully.",dep, "New balance:", accounts[num]["balance"])

        else:
            print("Account not found")

    elif choice == "3":
        num = int(input("Enter account number: "))
        if num in accounts:
            withdrew = float(input("Enter withdrawal amount: "))
            if withdrew> accounts[num]["balance"]:
                print("Insufficient balance")
            else:
                accounts[num]["balance"] -= withdrew
                print("Mr.",accounts[num]["name"],"You Have Withdrawal successful.",withdrew ,"New balance:", accounts[num]["balance"])
        else:
            print("Account not found")

    elif choice == "4":
        num = int(input("Enter account number: "))
        if num in accounts:
            print("Mr.",accounts[num]["name"],"Your Current balance is:", accounts[num]["balance"])
        else:
            print("Account not found")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid option. Please try again.")

    opt = input("Do you want to continue? (y/n): ")

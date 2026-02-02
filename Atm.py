pin = 799532
attempts = 0
max_attempts = 3
amount = 10000  # Initial balance

# Pin verification loop
while attempts < max_attempts:
    new = int(input("Enter your PIN: "))
    
    if new == pin:
        print("PIN is correct.")
        break  # Exit the loop if the PIN is correct
    else:
        attempts += 1
        if attempts < max_attempts:
            print("Incorrect PIN. Try again.")
        else:
            print("You entered the wrong PIN too many times. Your card is blocked.")
            exit()  # Exit the program after the card is blocked

# ATM options
def ATM():
    global amount  # Use the global 'amount' variable to update balance

    # Main ATM menu
    while True:
        print("\nSelect an option:")
        print("1. Check Balance")
        print("2. Withdrawal")
        print("3. Deposit")
        print("4. Exit")

        choice = input("Select your choice (1/2/3/4): ")

        if choice == '1':
            print(f"Your current balance is {amount}")
        elif choice == '2':
            withdrawal_amount = float(input("Enter the amount to withdraw: "))
            if withdrawal_amount <= amount:
                amount -= withdrawal_amount
                print(f"Withdrawal successful. Available balance: {amount}")
            else:
                print("Insufficient funds!")
        elif choice == '3':
            deposit_amount = float(input("Enter the amount to deposit: "))
            amount += deposit_amount
            print(f"Deposit successful. Total balance is {amount}")
        elif choice == '4':
            print("Thank you for visiting the ATM!")
            break  # Exit the ATM loop
        else:
            print("Invalid choice! Please select a valid option.")

# Call the ATM function after successful PIN verification
ATM()

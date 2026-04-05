while True:
    name = input("Enter your name or 'q' to quit: ")

    if name.lower() == 'q':
        print("Quitting the program.")
        break

    try:
        account_balance = float(input("Enter your current account balance: "))
        amount = float(input("Enter amount to withdraw (-) or deposit (+): "))
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
        continue

    new_balance = round(account_balance + amount, 2)

    if amount > 0:
        print(f"{name}, deposit successful.")
        print(f"New account balance: ${new_balance:.2f}")

    elif amount < 0:
        print(f"{name}, withdrawal processed.")
        if new_balance < 0:
            print("Warning: Account is overdrawn.")
        print(f"New account balance: ${new_balance:.2f}")

    else:
        print("No change in account balance.")

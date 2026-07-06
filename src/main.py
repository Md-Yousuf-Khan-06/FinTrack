payment_methods= {
            1: "Cash",
            2: "UPI",
            3: "Bank Transfer",
            4: "Card"
        
        }
income_records=[]
choice=0
while choice!=6:
    print("\nFINTRACK")
    print("Personal Finance Management System\n")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Search Transactions")
    print("5. Monthly Summary")
    print("6. Exit\n")
    choice=int(input("Enter Your Choice: "))
    if choice==1:
        amount = int(input("Enter income amount: "))
        source = input("Enter income source: ")
        print("Select payment method:\n 1. Cash\n 2. UPI\n 3. Bank Transfer\n 4. Card")
        payment_method_choice = int(input("Enter your payment method choice:\n"))
        user_payment_method=payment_methods[payment_method_choice]
        income={
                "amount":amount,
                "source":source,
                "payment_method":user_payment_method
            }
        income_records.append(income)
        # print(income_records)
        print("\n✅ Payment added successfully!\n")
        # print("Income feature is under development.")
    elif choice==2:
        print("Expense feature is under development.")
    elif choice==3:
        # print("Viewing transactions...")
        print("======TRANSACTIONS======")
        for income in income_records:
            print(f"Amount: {income['amount']}")
            print(f"Source: {income['source']}")
            print(f"Payment Method: {income['payment_method']}")
            print("-------------------------")
    elif choice==4:
        print("Searching transactions...")
    elif choice==5:
        print("Generating monthly summary...") 
    elif choice==6:
        print("Thank you for using FinTrack!")
    else:
        print("Invalid choice! Please try again.")

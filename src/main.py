payment_methods= {
            1: "Cash",
            2: "UPI",
            3: "Bank Transfer",
            4: "Card"
        }


def select_payment_method():
    print("Select payment method:\n 1. Cash\n 2. UPI\n 3. Bank Transfer\n 4. Card")
    payment_method_choice = int(input("Enter your payment method choice:\n"))
    user_payment_method=payment_methods[payment_method_choice]
    return user_payment_method

def display_expense(expense):
            print(f"Amount: {expense['amount']}")
            print(f"Category: {expense['category']}")
            print(f"description: {expense['description']}")
            print(f"Payment Method: {expense['payment_method']}")
            print("-------------------------")

income_records=[]
expense_records=[]


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
        payment=select_payment_method()
        income={
                "amount":amount,
                "source":source,
                "payment_method":payment
            }
        income_records.append(income)
        print("\n✅ Payment added successfully!\n")


    elif choice==2:
        expense_amount=int(input('Enter the expense amount:'))
        category=input("Enter the expense category:")
        description=input("Enter things you bought:")
        payment=select_payment_method()
        expense={
            "amount":expense_amount,
            "category":category,
            "description": description,
            "payment_method":payment
        }
        expense_records.append(expense)
        print("Expense added successfully")


    elif choice==3:
        print("======TRANSACTIONS======")

        print("----INCOME----")
        for income in income_records:
            print(f"Amount: {income['amount']}")
            print(f"Source: {income['source']}")
            print(f"Payment Method: {income['payment_method']}")
            print("-------------------------")

        print("----EXPENSE----")
        for expense in expense_records:
            display_expense(expense)
        


    elif choice==4:
        print("Search by:\n 1. Category\n 2. Description\n 3. Payment Method\n 4. Back to Menu")
        user_choice=int(input("Enter Your Choice: "))

        if user_choice==1:
            category= input("Enter Category: ")
            found=False
            for expense in expense_records:
               if category.lower() in expense["category"].lower():
                   found=True
                   display_expense(expense)
            if not found:
               print("No matching transactions found")

        elif user_choice==2:
            description =input("Enter Description: ")
            found=False
            for expense in expense_records:
                if description.lower() in expense["description"].lower():
                    found=True
                    display_expense(expense)
            if not found:
                print("No matching transactions found.")

        elif user_choice==3:
            payment_method=select_payment_method()
            found=False
            for expense in expense_records:
                if payment_method in expense["payment_method"]:
                    display_expense(expense)
                    found=True
            if not found:
                print("No matching transactions found.")
            
            # input("Enter Payment Method: ")

        # print("Searching transactions...")






    elif choice==5:
        print("Generating monthly summary...") 
    elif choice==6:
        print("Thank you for using FinTrack!")
    else:
        print("Invalid choice! Please try again.")

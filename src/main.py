import datetime
from validation import get_valid_amount, get_valid_text, get_valid_choice
from storage import load_data, save_data
from payment import select_payment_method
from summary import monthly_summary
from transactions import delete_transactions, search_transactions, view_transactions


income_records=[]
expense_records=[]

def add_income():
    amount = get_valid_amount("Enter the income amount: ")
    source = get_valid_text("Enter income source: ")
    payment=select_payment_method()
    current=datetime.datetime.now()
    income={
            "amount":amount,
            "source":source,
            "payment_method":payment,
            "current_date":current.strftime("%d-%m-%Y"),
            "current_time":current.strftime('%I:%M %p')
            }
    income_records.append(income)
    save_data(income_records, expense_records)
    print("\n✅ Income added successfully!\n")

def add_expense():
    expense_amount=get_valid_amount("Enter the expense amount: ")
    category = get_valid_text("Enter the expense category: ")
    description = get_valid_text("Enter things you bought: ")
    payment=select_payment_method()
    current=datetime.datetime.now()
    expense={
        "amount":expense_amount,
        "category":category,
        "description": description,
        "payment_method":payment,
        "current_date":current.strftime("%d-%m-%Y"),
        "current_time":current.strftime('%I:%M %p')
        }
    expense_records.append(expense)
    save_data(income_records,expense_records)
    print("\n✅ Expense added successfully!\n")


def main_menu():
    choice=0
    while choice!=7:
        print("\nFINTRACK")
        print("Personal Finance Management System\n")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. Search Transactions")
        print("5. Monthly Summary")
        print("6. Delete Transaction\n")
        print("7. Exit\n")
        choice=get_valid_choice("Enter Your Choice:", 1, 7)
        if choice==1:
            add_income()

        elif choice==2:
            add_expense()
        
        elif choice==3:
            view_transactions(income_records, expense_records)

        elif choice==4:
            search_transactions(expense_records)

        elif choice==5:
            monthly_summary(income_records, expense_records)

        elif choice==6:
            delete_transactions(income_records, expense_records)

        elif choice==7:
            print("Thank you for using FinTrack!")
        else:
            print("Invalid choice! Please try again.")
   

income_records, expense_records = load_data()
main_menu()




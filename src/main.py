from validation import get_valid_choice
from storage import load_data
from summary import monthly_summary
from transactions import delete_transactions, search_transactions, view_transactions
from income import add_income
from expense import add_expense

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
            add_income(income_records, expense_records)

        elif choice==2:
            add_expense(income_records, expense_records)
        
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




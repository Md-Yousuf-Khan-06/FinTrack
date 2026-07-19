from validation import get_valid_choice,get_valid_text
from payment import select_payment_method
from storage import save_data

def display_income(income):
        print(f"Amount: {income['amount']}")
        print(f"Source: {income['source']}")
        print(f"Payment Method: {income['payment_method']}")
        print(f"Payment Date: {income['current_date']}")
        print(f"Payment Time: {income['current_time']}")
        print("-------------------------")

def display_expense(expense):
        print(f"Amount: {expense['amount']}")
        print(f"Category: {expense['category']}")
        print(f"Description: {expense['description']}")
        print(f"Payment Method: {expense['payment_method']}")
        print(f"Payment Date: {expense['current_date']}")
        print(f"Payment Time: {expense['current_time']}")
        print("-------------------------")

def view_transactions(income_records, expense_records):
    print("======TRANSACTIONS======")
    if not income_records:
        print("No income records found")
    else:
        print("----INCOME----")
        for income in income_records:
            display_income(income)

    if not expense_records:
        print("No expense records found")
    else:
        print("----EXPENSE----")
        for expense in expense_records:
            display_expense(expense)

def search_transactions(expense_records):
    print("Search by:\n 1. Category\n 2. Description\n 3. Payment Method\n 4. Back to Menu")
    user_choice=get_valid_choice("Enter Your Choice: ",1 ,4)
    if user_choice==1:
        category = get_valid_text("Enter Category: ")
        found=False
        for expense in expense_records:
            if category.lower() in expense["category"].lower():
                found=True
                display_expense(expense)
        if not found:
            print("No matching transactions found.")

    elif user_choice==2:
        description = get_valid_text("Enter Description: ")
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
            if payment_method == expense["payment_method"]:
                display_expense(expense)
                found=True
        if not found:
            print("No matching transactions found.")
    elif user_choice==4:
         # continue
        print("Returning back to main menu")

def delete_transactions(income_records,  expense_records):
    if not expense_records:
        print("No expense records found.")
    else:
        for number, expense in enumerate(expense_records, start=1):
            print(f"{number}. {expense['category']} | ₹{expense['amount']} | {expense['description']}")
        choice = get_valid_choice("Enter a Valid Choice: ", 1, len(expense_records))
        expense_records.pop(choice-1)
        save_data(income_records, expense_records)
        print("✅ Transaction deleted successfully!")
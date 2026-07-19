import datetime
from validation import get_valid_amount, get_valid_text
from payment import select_payment_method
from storage import save_data


def add_expense(income_records, expense_records):
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
import datetime
from validation import get_valid_amount, get_valid_text
from payment import select_payment_method
from storage import save_data


def add_income(income_records, expense_records):
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
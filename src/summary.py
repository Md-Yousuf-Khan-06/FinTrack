def monthly_summary(income_records, expense_records):
    total_income=0
    total_expense=0
    for income in income_records:
        total_income += income["amount"]
    for expense in expense_records:
        total_expense += expense["amount"]
    balance=total_income-total_expense
    print("\n====== MONTHLY SUMMARY ======")
    print(f"Total Income : {total_income}")
    print(f"Total Expense: {total_expense}")
    print(f"Balance      : {balance}")
    if balance>0:
        print("Net Saving Status: Profit✅")
    elif balance<0:
        print("Net Saving Status: Loss❌")
    else:
        print("Net Savings Status: Break Even")
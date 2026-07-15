import json
import datetime

payment_methods= {
            1: "Cash",
            2: "UPI",
            3: "Bank Transfer",
            4: "Card"
        }
income_records=[]
expense_records=[]

def select_payment_method():
    print("Select payment method:\n 1. Cash\n 2. UPI\n 3. Bank Transfer\n 4. Card")
    while True:
        try:
            payment_method_choice = int(input("Enter your payment method choice:\n"))
            if payment_method_choice in payment_methods:
                return payment_methods[payment_method_choice]
                
            else:
                print("Enter valid payment choice")
        except  ValueError:
            print("Enter valid payment choice")

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

def save_data():
    data = {
        "income": income_records,
        "expense": expense_records
    }
    with open("data.json","w") as file:
        json.dump(data, file, indent=3)
def load_data():
    global income_records
    global expense_records
    try:
        with open("data.json","r") as file:
            data=json.load(file)
            income_records= data["income"]
            expense_records=data["expense"]
    except FileNotFoundError:
        income_records=[]
        expense_records=[]
        print("No previous data found. Starting with empty records.")

def get_valid_amount(prompt):
    while True:
        try:
            amount=int(input(prompt))
            if amount>0:
                return amount
            else:
                print("Amount must be greater than 0")
        except ValueError:
            print("Invalid Input, Please enter valid input")
def get_valid_text(prompt):
    while True:
        text=input(prompt).strip()
        if text=="":
            print("Enter valid text")
        else:
            return text
        

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
    save_data()
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
    save_data()
    print("\n✅ Expense added successfully!\n")

def view_transactions():
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

def search_transactions():
    print("Search by:\n 1. Category\n 2. Description\n 3. Payment Method\n 4. Back to Menu")
    user_choice=get_valid_choice("Enter Your Choice: ",1 ,4)
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
            if payment_method == expense["payment_method"]:
                display_expense(expense)
                found=True
        if not found:
            print("No matching transactions found.")
    elif user_choice==4:
         # continue
        print("Returning back to main menu")

def monthly_summary():
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

def main_menu():
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
        choice=get_valid_choice("Enter Your Choice:", 1, 6)
        if choice==1:
            add_income()

        elif choice==2:
            add_expense()
        
        elif choice==3:
            view_transactions()

        elif choice==4:
            search_transactions()

        elif choice==5:
            monthly_summary()

        elif choice==6:
            print("Thank you for using FinTrack!")
        else:
            print("Invalid choice! Please try again.")
def get_valid_choice(prompt, minimum, maximum):
        while True:
            try:
                choice=int(input(prompt))
                if minimum<=choice<=maximum:
                    return choice
                else:
                    print("Enter a Valid choice")
            except ValueError:
                print("Invalid choice. Please enter a number between 1 and 6.")       
load_data()
main_menu()




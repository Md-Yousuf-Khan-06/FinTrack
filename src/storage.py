import json


def save_data(income_records, expense_records):
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
            return data["income"], data["expense"]
    except (FileNotFoundError, json.JSONDecodeError):
        print("No previous data found. Starting with empty records.")
        return [], []
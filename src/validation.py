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
def get_valid_choice(prompt, minimum, maximum):
        while True:
            try:
                choice=int(input(prompt))
                if minimum<=choice<=maximum:
                    return choice
                else:
                    print("Please enter a valid choice.")
            except ValueError:
                print(f"Invalid choice. Please enter a number between {minimum} and {maximum}.")   
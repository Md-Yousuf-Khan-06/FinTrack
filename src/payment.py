payment_methods= {
            1: "Cash",
            2: "UPI",
            3: "Bank Transfer",
            4: "Card"
        }
def select_payment_method():
    print("Select payment method:\n 1. Cash\n 2. UPI\n 3. Bank Transfer\n 4. Card")
    while True:
        try:
            payment_method_choice = int(input("Enter your payment method choice:\n"))
            if payment_method_choice in payment_methods:
                return payment_methods[payment_method_choice]
                
            else:
                print("Please enter a valid payment choice.")
        except  ValueError:
            print("Please enter a valid payment choice.")
while True:
    try:
        money = float(input("Enter the value of money in dollars to convert to cents. \n>>> "))
        str_money = str(money)
        dollars, cents = str_money.split(".")
        if len(cents) > 2:
            print("Money can only have up to 2 decimal places.")
        else:
            float_total_cents = money * 100
            total_cents, zero = str(float_total_cents).split(".")
            print(f"${money:.2f} is equivalent to {total_cents} cents")
    except ValueError:
        print("Dollars should be in the form of '0.50', '2.00', '6.90', etc")
        continue
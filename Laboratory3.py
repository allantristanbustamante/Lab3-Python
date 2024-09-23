salary = float(input("Enter your monthly salary: "))
loan = float(input("Enter the loan amount you are requesting: "))

# Check if customer is eligible for a loan
if salary >= 30000.00 and loan <= 10 * salary:
    print("You are eligible for a loan!")
    monthly_pay = int(input("Input how many months would you to pay the loan? "))
    interest_rate = 0.10
    total_amount = loan * (1 + interest_rate)
    monthly_payment = total_amount / monthly_pay
    print(f"Your monthly payment will be ₱{monthly_payment:.2f} for {monthly_pay} months.")

else:
    if salary < 30000.00:
        print("Sorry, your salary is too low. You cannot avail the loan.")
    else:
        print("Sorry, but the loan amount you asked for is too much given your income.")
def get_loan_schedule(loan_amount, annual_rate, monthly_payment):
    balances = [loan_amount]
    monthly_interest_rate = (annual_rate / 100) / 12

    while loan_amount > 0:
        loan_amount = loan_amount * (1 + monthly_interest_rate)
        loan_amount = max(0, loan_amount - monthly_payment)
        balances.append(round(loan_amount))

    return balances

# print(get_loan_schedule(1000, 0, 200))
# print(get_loan_schedule(1000, 5, 200))
# print(get_loan_schedule(10, 50, 1))
# print(get_loan_schedule(5500, 8, 400))
# print(get_loan_schedule(50000, 5.2, 1650))
# Initialize opening balance
opening_balance = 200000

# Transaction details
deposit = 100000
funding_transfer = 25000
loan_repayment = 10000
interest_rate = 0.05  # 5%
withdrawal = 20000

# Calculate interest (half-yearly)
interest = (opening_balance + deposit + funding_transfer) * (interest_rate / 2)

# Calculate closing balance
closing_balance = (
    opening_balance
    + deposit
    + funding_transfer
    + loan_repayment
    + interest
    - withdrawal
)

# Display results
print("Customer 's' Account Statement:")
print(f"1. Opening Balance:     ₹{opening_balance:,.2f}")
print(f"2. Deposit:             ₹{deposit:,.2f} (+)")
print(f"3. Funding Transfer:    ₹{funding_transfer:,.2f} (+)")
print(f"4. Loan Repayment:      ₹{loan_repayment:,.2f} (+)")
print(f"5. Interest (5% half-yearly): ₹{interest:,.2f} (+)")
print(f"6. Withdrawal:          ₹{withdrawal:,.2f} (-)")
print("----------------------------------------")
print(f"Closing Balance:       ₹{closing_balance:,.2f}")
from email.charset import SHORTEST


customer_name = input ("Welcome, what is your name?")
string_balance = 5000.25
print(f"Hello {customer_name},your starting balance is {string_balance}")
Paycheck = float(input ("How much of the paycheck do you want to deposit?"))
Expenditure_item = input ("What did you buy ")
Expenditure = float(input (f"How much did the {Expenditure_item} cost?"))
user_name = customer_name
balance = string_balance
deposits = Paycheck
expense_item = Expenditure_item
expense_amount = Expenditure
def checking_balance(user_name, balance, deposits, expense_item, expense_amount):
    ending_balance = balance + deposits - expense_amount
    print(f"Your ending balance is {ending_balance}")

checking_balance(customer_name, string_balance, 1000, Expenditure_item, Expenditure)

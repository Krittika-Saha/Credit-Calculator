# imported math
import math
# user input
print("Enter the credit principal:")
credit_principal = int(input())
print
user_wish = (input("""
What do you want to calculate?
type "m" for number of monthly payments,
type "p" for the monthly payment
"""))
if user_wish == 'm':
    print("Enter the monthly payment:")
    monthly_payment = int(input())
    months_required = math.ceil(credit_principal/monthly_payment)
    # math.ceil is a function that returns the smallest integer not less than x (here, credit_principal/monthly_payement):D.
    if months_required > 1:
        print(f"It will take {months_required} months to repay the credit")
    elif months_required == 1:
        print(f'It will take {months_required} month to repay the credit')
elif user_wish == 'p':
    print("Enter the number of months:")
    months = int(input())
    monthly_payment2 = math.ceil(credit_principal/months)
    lastpayment = credit_principal - (months - 1) * monthly_payment2
    # months * monthly_payment2 = credit_principal so when we subtract 1 from the months, we get the total payment of all the other months except the last one. And we can find its value by subtract the total payment from the credit_principal. Hope it helps! :D 
    if monthly_payment2 == lastpayment:
        print(f"Your monthly payment = {lastpayment}")
    else:
        print(f'Your monthly payment = {monthly_payment2} and the last payment = {lastpayment}.')
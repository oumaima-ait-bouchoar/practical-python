# mortgage.py
#
# Exercise 1.7



# principal = 500000.0
# rate = 0.05
# payment = 2684.11

# additional_payment_first_year = 12*1000
# total_paid = 12*payment + additional_payment_first_year
# principal_after_first_year = principal * (1+rate) - total_paid
# months = 12 

# while principal_after_first_year > 0:
#     principal_after_first_year = principal_after_first_year * (1+rate/12) - payment
#     total_paid = total_paid + payment
#     print(months, total_paid, principal_after_first_year)
#     months +=1

# print('Total paid', round(total_paid,2))
# print('In {} months'.format(months))

principal = 500000.0
rate = 0.05
payment = 2684.11


total_paid = 0
months = 0
additional_payment = 1000

while principal > 0:
    while months < 12:
        principal = principal * (1+rate/12) - payment - additional_payment
        total_paid = total_paid + payment + additional_payment
        months +=1
    principal = principal * (1+rate/12) - payment 
    total_paid = total_paid + payment
    months +=1
    print(months, total_paid, principal)

print('Total paid', round(total_paid,2))
print('In {} months'.format(months))
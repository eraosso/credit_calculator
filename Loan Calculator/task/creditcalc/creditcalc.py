import math
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--type', help='Calculates differentiated payments')
# parser.add_argument('type', type=str, choices=['diff', 'annuity'],
#                     help='Calculates differentiated payments')
parser.add_argument('--principal', help='Loan Principal', type=float)
parser.add_argument('--periods', type=int,
                    help='number of months needed to repay the loan')
parser.add_argument('--interest', help='interest rate for the loan', type=float)
parser.add_argument('--payment', help='monthly payment', type=float)

args = parser.parse_args()

parametros = [args.type, args.principal, args.periods, args.interest, args.payment]

if parametros[3] is None:
    print('Incorrect parameters')
    exit()
elif parametros[2] is not None and parametros[2] < 0:
    print('Incorrect paramenters')
    exit()
elif parametros[0] == 'diff' and parametros[4] is not None:
    print('Incorrect parameters')
    exit()
elif parametros[0] != 'diff' and parametros[0] != 'annuity':
    print('Incorrect parameters')
    exit()
else:
    pass

total = 0
interest = parametros[3] / (12 * 100)

if parametros[0] == 'diff':
    for i in range(1, parametros[2] + 1):
        diff_i = (parametros[1] / parametros[2]) \
                 + interest * (parametros[1] - ((parametros[1] * (i - 1)) / parametros[2]))
        total += math.ceil(diff_i)
        print("Month {}: payment is {}".format(i, math.ceil(diff_i)))
    print("\nOverpayment = {}".format(math.ceil(total - parametros[1])))
    exit()

if parametros[0] == 'annuity' and parametros[1] is not None and parametros[2] is not None:
    monthly_payment = parametros[1] * ((interest * ((1 + interest) ** parametros[2]))\
                                   / (((1 + interest) ** parametros[2]) - 1))
    total = math.ceil(monthly_payment) * parametros[2]
    print("Your annuity payment = {}!".format(math.ceil(monthly_payment)))
    print("Overpayment = {}".format(math.ceil(total - parametros[1])))

if parametros[0] == 'annuity' and parametros[1] is None:
    principal = parametros[4] / ((interest * ((1 +  interest)**parametros[2]))\
                                 /(((1+interest)**parametros[2]) - 1))
    print("Your loan principal = {}!".format(int(principal)))
    total = parametros[4] * parametros[2]
    print("Overpayment = {}".format(math.ceil(total-principal)))

if parametros[0] == 'annuity' and parametros[2] is None:
    number_of_months = math.log((parametros[4]\
                                 / (parametros[4]\
                                    - (interest * parametros[1]))), (1 + interest))

    number_of_months = math.ceil(number_of_months)
    number_of_years = int(number_of_months / 12)
    months = int(((number_of_months / 12) - number_of_years) * 12)
    total = parametros[4] * number_of_months
    if months != 0:
        print('It will take {} years and {} months to repay this loan!'.format(number_of_years, months))
    else:
        print('It will take {} years to repay this loan!'.format(number_of_years, months))
    print("Overpayment = {}".format(int(total - parametros[1])))


# print('What do you want to calculate?')
# print('type "n" - for number of monthly payments,')
# print('type "a" - for annuity monthly payment amount,')
# print('type "p" - for loan principal:')
# what = str(input())
# if what == 'n':
#     print('Enter the loan principal:')
#     principal = float(input())
#     print('Enter the monthly payment:')
#     monthly_payment = float(input())
#     print('Enter the loan interest:')
#     loan_interest = float(input())
#
#     interest = loan_interest / (12 * 100)
# elif what == 'a':
#     print('Enter the loan principal:')
#     principal = float(input())
#     print('Enter the number of periods:')
#     num_periods = int(input())
#     print('Enter the loan interest:')
#     loan_interest = float(input())
#
#     interest = loan_interest / (12 * 100)
#
#     monthly_payment = principal * ((interest * ((1 + interest) ** num_periods)) / (((1 + interest) ** num_periods) - 1))
#     print('Your monthly payment = {}!'.format(math.ceil(monthly_payment)))
# else:
#     print('Enter the annuity payment:')
#     payment = float(input())
#     print('Enter the number of periods:')
#     num_periods = int(input())
#     print('Enter the loan interest:')
#     loan_interest = float(input())
#     interest = loan_interest / (12 * 100)
#
#
#     print('Your loan principal = {}!'.format(int(principal)))
# import math
# print('What do you want to calculate?')
# print('type "n" - for number of monthly payments,')
# print('type "a" - for annuity monthly payment amount,')
# print('type "p" - for loan principal:')
# what = str(input())
# if what == 'n':
#     print('Enter the loan principal:')
#     principal = float(input())
#     print('Enter the monthly payment:')
#     monthly_payment = float(input())
#     print('Enter the loan interest:')
#     loan_interest = float(input())
#
#     interest = loan_interest / (12 * 100)
#     number_of_months = math.log((monthly_payment / (monthly_payment - (interest * principal))), (1 + interest))
#
#     #    number_of_months = math.log((monthly_payment/(monthly_payment - (interest * principal))), (1 + interest))
#     number_of_months = math.ceil(number_of_months)
#     number_of_years = int(number_of_months / 12)
#     months = int(((number_of_months / 12) - number_of_years) * 12)
#
#     print('It will take {} years and {} months to repay this loan!'.format(number_of_years, months))
# elif what == 'a':
#     print('Enter the loan principal:')
#     principal = float(input())
#     print('Enter the number of periods:')
#     num_periods = int(input())
#     print('Enter the loan interest:')
#     loan_interest = float(input())
#
#     interest = loan_interest / (12 * 100)
#
#     monthly_payment = principal * ((interest * ((1 + interest) ** num_periods)) / (((1 + interest) ** num_periods) - 1))
#     print('Your monthly payment = {}!'.format(math.ceil(monthly_payment)))
# else:
#     print('Enter the annuity payment:')
#     payment = float(input())
#     print('Enter the number of periods:')
#     num_periods = int(input())
#     print('Enter the loan interest:')
#     loan_interest = float(input())
#     interest = loan_interest / (12 * 100)
#
#     principal = payment / ((interest * ((1+interest)**num_periods))/(((1+interest)**num_periods) - 1))
#
#     print('Your loan principal = {}!'.format(int(principal)))

#     if (principal // monthly_payment) == 1:
#         number_of_months = principal / monthly_payment
#         if number_of_months == 1:
#             print("It will take {} month to repay the loan".format(int(number_of_months)))
#         else:
#             print("It will take {} months to repay the loan".format(int(number_of_months)))
#     else:
#         number_of_months = math.ceil(principal / monthly_payment)
#         print("It will take {} months to repay the loan".format(int(number_of_months)))
# else:
#     print('Enter the number of months:')
#     number_of_months = int(input())
#     if (principal % number_of_months) == 0:
#         payment = principal / number_of_months
#         print('Your monthly payment = {}'.format(int(payment)))
#     else:
#         payment = math.ceil(principal / number_of_months)
#         last_payment = principal - (number_of_months -1) * payment
#         print('Your monthly payment = {} and the last payment = {}.'.format(payment, int(last_payment)))
#

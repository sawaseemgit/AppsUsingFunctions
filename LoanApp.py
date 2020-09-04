import matplotlib.pyplot as plt


def get_loan_info():  # Get and store loan info & store in dict
    loan = {}
    loan['principal'] = float(input('Enter the loan amount: '))
    loan['rate'] = float(input('Enter the interest rate: ')) / 100
    loan['monthly payment'] = float(input('Monthly payment: '))
    loan['money paid'] = 0
    return loan


def show_loan_info(mloan, num_mths):  # display current loan status
    print(f'***Loan info after {num_mths} months***')
    for k, v in mloan.items():
        print(f'{k.title()}:{v}')


def collect_interest(mloan):  # Update remaining loan
    mloan['principal'] += mloan['principal'] * mloan['rate'] / 12


def make_monthly_payment(mloan):  # monthly payment to payoff principal
    mloan['principal'] -= mloan['monthly payment']
    if mloan['principal'] > 0:
        mloan['money paid'] += mloan['monthly payment']
    else:
        mloan['money paid'] += mloan['monthly payment'] + mloan['principal']
        mloan['principal'] = 0


def summarize_loan(mloan, mon_num, ini_principal):  # display results of paying off loan
    print(f'Congrats! You paid off your loan in {mon_num} months..! ')
    print('Your initial loan was ${} at the rate of {}'.format(ini_principal, mloan['rate']))
    print('Your monthly payment was ${}. '.format(mloan['monthly payment']))
    print('You spent ${} in total'.format(round(mloan['money paid'], 2)))
    interest = round(mloan['money paid'] - ini_principal, 2)
    print(f'You spent ${interest} on interest.')


def create_graph(data, mloan):
    x_values = []  # Months
    y_values = []  # Corresponding principal values
    for point in data:
        x_values.append(point[0])
        y_values.append(point[1])

    plt.plot(x_values, y_values)
    plt.title('{} %Interest With ${} Monthly payment'
                 .format((100*mloan['rate']), mloan['monthly payment']))
    plt.xlabel('Month Number')
    plt.ylabel('Principle of loan')
    plt.show()


print('Welcome to the Loan Calculator App')
month_number = 0
my_loan = get_loan_info()
starting_principle = my_loan['principal']
plot_data = []
show_loan_info(my_loan, month_number)
input('Press Enter to begin paying off your loan')

while my_loan['principal'] > 0:
    if my_loan['principal'] > starting_principle:
        break

    month_number += 1
    collect_interest(my_loan)
    make_monthly_payment(my_loan)
    plot_data.append((month_number, my_loan['principal']))
    show_loan_info(my_loan, month_number)

if my_loan['principal'] <= 0:
    summarize_loan(my_loan, month_number, starting_principle)
    create_graph(plot_data, my_loan)
else:
    print('You can never pay off your loan.!!!\nYou cannot get ahead of the'
          ' interest :-(')

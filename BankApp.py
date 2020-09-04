def get_info():
    print('Welcome to Python Loan Calculator App')
    name = input('Hello, What is your Name: ').title().strip()
    saving_amt = float(input('How much money would you like to set up your '
                             'savings account with: '))
    check_amt = float(input('How much money would you like to set up your '
                            'checking account with: '))
    bank_account = {
        'Name': name,
        'Savings': saving_amt,
        'Checking': check_amt,
    }
    return bank_account


def make_deposit(bank_account, account, money):
    bank_account[account] += money
    print(f"Deposited ${money} into {bank_account['Name']}'s {account.lower()} ")


def make_withdrawal(bank_account, account, money):
    if bank_account[account] - money >= 0:
        bank_account[account] -= money
        print(f"Withdrew ${money} from {bank_account['Name']}'s {account.lower()}")
    else:
        print(f"Sorry, by withdrawing ${money}, you will have negative balance.")


def display_info(bank_account):
    print('Current Account Information:')
    for k, v in bank_account.items():
        if k == 'Name':
            print(f'{k}:{v}')
        else:
            print(f'{k}: ${v}')


my_account = get_info()
repeat = True
while repeat:
    display_info(my_account)  # Display current state of account
    account_type = input('What account would you like to access today?(Savings/Checking):') \
        .title().strip()
    choice = input('What transaction would you like to make today?(Deposit/Withdrawal) ') \
        .title().strip()
    amount = float(input('How much money $: '))

    if account_type == 'Savings' or account_type == 'Checking':
        if choice == 'Deposit':
            make_deposit(my_account, account_type, amount)
            print(f'Your Current account status after the {choice} is:')
            display_info(my_account)
        elif choice == 'Withdrawal':
            make_withdrawal(my_account, account_type, amount)
            print(f'Your Current account status after the {choice} is:')
            display_info(my_account)
        else:
            print('Sorry, this transaction cannot be done today.!')

    else:
        print('Sorry, that is not a valid transaction.!')

    rep_choice = input('Would you like to make another transaction?(Yes/No): ') \
        .lower().strip()
    if rep_choice.startswith('n'):
        repeat = False
        print('Thank you have a great day..!')

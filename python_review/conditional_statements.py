# Conditional Statements

balance = 100
price = 50

if balance >= price:
    answer = input('Do you want to continue? Enter yes or no: ').lower()
    if answer == 'yes':
        print('We\'ll move on.')
        new_balance = balance - price
        print(f'You can book the flight and your new balance will be {new_balance}.')
    elif answer == 'no':
        print('We\'ll stop.')
    else:
        print('Invalid answer.')
else:
    print(f'Insufficient funds!')

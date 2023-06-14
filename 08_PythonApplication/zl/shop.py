'''
Answer for Question 6 - PIAT: The Cheese Shop

Name:
SID:
unikey:

'''


def buy_cheese(gold: int)-> tuple:
    '''
    Feature for players to buy cheddar from shop
    Parameters:
        gold:           int, amount of gold player has
    Returns:
        gold_spent:     int, amount of gold spent
        cheese_bought:  int, amount of cheese bought
    '''
    gold_spent = 0
    cheese_bought = 0

    print(f'You have {gold} gold to spend.')
    command = input('State [cheese quantity]: ').split(' ')
    if len(command) == 1:
        if command[0] != 'back':
            print('Sorry, did not understand.')
        return gold_spent, cheese_bought
    
    cheese_type = command[0]
    cheese_quantity = int(command[1])
    if cheese_type != 'cheddar':
        print('Sorry, did not understand.')
        return gold_spent, cheese_bought

    if cheese_quantity <= 0:
        print('Must purchase a positive amount of cheese.')
        return gold_spent, cheese_bought

    # calculate price
    price = cheese_quantity * 10

    # ensure we are not over spending (buying more than we can)
    # e.g. gold is 100, and gold_spent is currently 70
    # if price is 40, then we should not be able to buy it
    if gold_spent + price <= gold:
        print(f'Successfully purchase {cheese_quantity} cheddar.')
        # keep track of gold remaining 
        gold_spent += price
        cheese_bought += cheese_quantity
    else:
        print('Insufficient gold.')
    return gold_spent, cheese_bought


def display_inventory(gold: int, cheddar: int, trap: str) -> None:
    '''
    Prints contents of inventory
    Parameters:
        gold:        int, current gold that player possess
        cheddar:     int, current amount of cheddar that player possesses
        trap:        str, current name of trap that player posseses
    '''
    print(f'Gold - {gold}')
    print(f'Cheddar - {cheddar}')
    print(f'Trap - {trap}')


def enter_shop(gold, cheddar, trap):
    '''
    Runs the shop
    This allows modular use of using the shop, as it can be called with any 
    combination of gold, cheddar and trap from other files (such as game)
    Parameters:
        gold:        int, current gold that player possesses
        cheddar:     int, current amount of cheddar that player possesses
        trap:        str, name of trap that player posseses
    Returns:
        gold:        int, updated gold that player possess
        cheddar:     int, updated amount of cheddar that player possesses
    '''
    print('Welcome to The Cheese Shop!')
    print('Cheddar - 10 gold')
    while True:
        print()
        print('How can I help ye?')
        print('1. Buy cheese')
        print('2. View inventory')
        print('3. Leave shop')

        option = input()
        if option == '1':
            # the function returns a tuple of gold spent and cheddar bought
            result = buy_cheese(gold)
            gold -= result[0]
            cheddar += result[1]
        elif option == '2':
            display_inventory(gold, cheddar, trap)
        elif option == '3':
            break

    return gold, cheddar


def main():
    '''
    Implement your code here.
    '''
    # we set our initial values here
    gold = 125
    cheddar = 0
    trap = 'Cardboard and Hook Trap'

    # notice we do not get the return value from the enter_shop function
    # this is because we exit the program once we leave the shop
    # so we wouldn't need to know the gold and cheddar after exiting the shop
    enter_shop(gold, cheddar, trap)


if __name__ == '__main__':
    main()

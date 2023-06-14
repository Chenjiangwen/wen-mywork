'''
Answer for Question 7 - PIAT: The Hunt

Name:
SID:
unikey:

'''

'''
Keep this line!
'''
import random

'''
We recommend you import your 'name', 'train' and 'shop' modules to complete this 
question. It will save trouble in needing to copy and paste code from previous 
questions. However if you wish not to, you are free to remove the imports below.
Feel free to import other modules that you have written.
'''
import name
import train
import shop
import q1


def hunt(gold, cheddar_amount, points):
    '''
    Handles the hunt mechanic.
    It includes the inputs and outputs of sounding the horn, the result of 
    the hunt, the gold and points earned, and whether users want to continue 
    after failing consecutively.
    Parameters:
        gold:           int,        the current quantity of gold the player possesses.
        cheddar_amount: int,        the current quantity of cheddar the player possesses.
        points:         int,        the current quantity of points that the player posseses.
    Returns:
        gold:           int,        the updated quantity of gold after the hunt.
        cheddar_amount: int,        the updated quantity of cheddar after the hunt.
        points:         int,        the updated quantity of points after the hunt.
    '''
    fails = 0
    while True:
        if fails == 5:
            stop = input('Do you want to continue to hunt? ')
            # exit condition
            if stop == 'no':
                return gold, cheddar_amount, points
            fails = 0

        print('Sound the horn to call for the mouse...')  
        horn = input('Sound the horn by typing "yes": ')
        # exit condition
        if horn == 'stop hunt':
            return gold, cheddar_amount, points

        if horn != 'yes':
            print('Do nothing.')
            fails += 1

        elif cheddar_amount <= 0:
            print('Nothing happens. You are out of cheese!')
            fails += 1
        
        else:
            cheddar_amount -= 1
        
            p = random.random()
            if p > 0.5:
                print('Nothing happens.')
                fails += 1
            else:
                print('Caught a Brown mouse!')
                fails = 0
                gold += 125
                points += 115

        print(f'My gold: {gold}, My points: {points}')
        print()


def main():
    '''
    Implement your code here.
    '''
    # Initialise our amounts for each variable
    gold = 125
    cheddar_amount = 0
    points = 0
    
    # Use the game title from Q1
    q1.main()
    print()

    hunter_name = input("What's ye name, Hunter?\n")
    # default name to Bob if not valid
    if not name.is_valid_name(hunter_name):
        hunter_name = 'Bob'

    print(f'Welcome to the Kingdom, Hunter {hunter_name}!')

    print("Before we begin, let's train you up!")
    train_command = input('Press "Enter" to start training or "skip" to Start Game: ')
    
    if train_command == 'skip':
        trap_name = "Cardboard and Hook Trap"
    else:
        # we need to print an extra newline if we don't skip training
        print()
        trap_name = train.train()

    print()

    while True:
        print(f'What do ye want to do now, Hunter {hunter_name}?')
        print('1. Exit game')
        print('2. Join the Hunt')
        print('3. The Cheese Shop')
        option = input()

        if option == '1':
            return
        elif option == '2':
            gold, cheddar_amount, points = hunt(gold, cheddar_amount, points)
        elif option == '3':
            # call our shop function which can be used with any gold, cheddar, trap
            # we get the return value as we need to know the updated gold and cheddar
            gold, cheddar_amount = shop.enter_shop(gold, cheddar_amount, trap_name)
        print()


if __name__ == '__main__':
    main()

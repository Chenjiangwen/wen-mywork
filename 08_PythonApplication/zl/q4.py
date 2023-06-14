'''
Answer for Question 4 - The Training

Name:
SID:
unikey:

'''

# some read-only global variables for clear definitions and avoid repetition 
INSTRUCTOR = 'Larry'
DEFAULT_TRAP = 'Cardboard and Hook Trap' 
LEFT_TRAP = 'High Strain Steel Trap'
RIGHT_TRAP = 'Hot Tub Trap'


def intro():
    '''
    Prints the introduction by Larry.
    Only line to print:     "Larry: I'm Larry. I'll be your hunting instructor."
    '''
    print(f"{INSTRUCTOR}: I'm {INSTRUCTOR}. I'll be your hunting instructor.")


def travel_to_camp():
    '''
    Prints the game conversation of travelling and reaching the camp.
    First line to print:    "Larry: Let's go to the Meadow to begin your training!"
    Last line to print:     "Larry: This is your camp. Here you'll set up your mouse trap."
    '''
    print(f"{INSTRUCTOR}: Let's go to the Meadow to begin your training!")
    input('Press Enter to travel to the Meadow...')
    print("Travelling to the Meadow...")
    print(f"{INSTRUCTOR}: This is your camp. Here you'll set up your mouse trap.")


def setup_trap() -> tuple:
    '''
    Prints the game conversation of getting your first trap and setting it.
    First line to print:    "Larry: Let's get your first trap..."
    Last line to print:     Either "Larry places one cheddar on the trap!", or
                            "Larry: Odds are slim with no trap!" depending on if you 
                            chose a trap or not. 
    Returns:
        A tuple containing 2 elements:
        1. trap,            str or None
            - If a trap was chosen, the value is the name of the trap
              e.g. 'High Strain Steel Trap'
            - If no trap was chosen, the value is 'Cardboard and Hook Trap'
        2. cheddar amount,  int
            - If a cheese was placed, value is 1
            - If no cheese was placed, value is 0
    '''
    print(f"{INSTRUCTOR}: Let's get your first trap...")

    input(f'Press Enter to view traps that {INSTRUCTOR} is holding...')

    print(f'{INSTRUCTOR} is holding...')
    print('Left: High Strain Steel Trap')
    print('Right: Hot Tub Trap')

    direction = input('Select a trap by typing "left" or "right": ').strip()
    has_trap = True

    if direction == 'left':
        trap = LEFT_TRAP
    elif direction == 'right':
        trap = RIGHT_TRAP
    else:
        trap = DEFAULT_TRAP

    if direction == 'left' or direction == 'right':
        print(f"{INSTRUCTOR}: Excellent choice.")
        print(f'Your "{trap}" is now set!')
        print(f"{INSTRUCTOR}: You need cheese to attract a mouse.")
        print(f"{INSTRUCTOR} places one cheddar on the trap!")
        return trap, 1
    else:
        print("Invalid command! No trap selected.")
        print(f"{INSTRUCTOR}: Odds are slim with no trap!")
        return trap, 0


def sound_horn() -> str:
    '''
    Prints the game conversation to sound horn
    First line to print:    "Sound the horn to call for the mouse..."
    Last line to print:     'Sound the horn by typing "yes": '
    Returns:
        horn input:     str, the input entered by user for sounding horn
        e.g. 'yes'
        e.g. 'asdhasjkhdsa'
    '''
    print('Sound the horn to call for the mouse...')
    horn_input = input('Sound the horn by typing "yes": ')
    return horn_input


def basic_hunt(cheddar_amount: int, horn_input: str) -> bool:  
    '''
    Prints the hunt and Larry's feedback of hunt.
    First line to print:    Varies depending on the hunt. Could be "Caught a Brown
                            Mouse!" or "Nothing happens."
    Last line to print:     Varies depending on the hunt like above.
    Parameters:
        cheddar_amount:     int, the number of cheese
        horn_input:         str, the input entered by user for sounding horn
    Returns:
        hunt status:        bool, whether the hunt succeeded or not
    '''
    if cheddar_amount > 0 and horn_input == 'yes':
        print('Caught a Brown mouse!')
        print('Congratulations. Ye have completed the training.')
        return True
    elif cheddar_amount > 0 or horn_input == 'yes':
        print('Nothing happens.')
        print('To catch a mouse, you need both trap and cheese!')
        return False
    else:
        print('Nothing happens.')
        return False


def end(hunt_status: bool):
    '''
    Prints the 'Good luck~' message if hunt was successful
    Parameters:
        hunt_status:    bool, whether the hunt succeeded or not
    '''
    if hunt_status:
        print('Good luck~')


def main():
    '''
    Call your functions here.
    Apart from good design, this is so if you import this file in train.py 
    (question 5), it will not run this code. Because this code's __name__ 
    will not be '__main__', but it will instead be 'q4', allowing you to use
    this file to import the functions.
    ''' 
    intro()
    travel_to_camp()
    result = setup_trap()
    trap_name = result[0]
    cheddar_amount = result[1]
    horn_input = sound_horn()
    hunt_status = basic_hunt(cheddar_amount, horn_input)
    end(hunt_status)


if __name__ == '__main__':
    main()

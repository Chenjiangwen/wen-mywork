'''
Answer for Question 5 - The Training Again

Name:
SID:
unikey:

'''

'''
We recommend you import your 'q4' module to complete this question. It will save 
trouble in needing to copy and paste code from previous question. However if you 
wish not to, you are free to remove the import below.
'''
from q4 import intro, travel_to_camp, setup_trap, sound_horn, basic_hunt, end

def train():
    '''
    Handle the logic of training in repetition
    Returns:
        trap_name: the name of the trap given from Larry after training
    '''
    intro()
    travel_to_camp()

    # repeat the codes for setting up trap and doing the hunt
    while True:
        result = setup_trap()
        trap_name = result[0]
        cheddar_amount = result[1]
        horn_input = sound_horn()
        hunt_status = basic_hunt(cheddar_amount, horn_input)
        end(hunt_status)

        print()
        continue_training = input('Press Enter to continue training and "no" to stop training: ')
        # exit condition: no longer continue training
        if continue_training == 'no':
            break

    # return the trap name once we are done training
    return trap_name

# you can make more functions here if you please
# or any global variables

def main():
    '''
    Implement your code here.
    ''' 
    train()

if __name__ == '__main__':
    main()

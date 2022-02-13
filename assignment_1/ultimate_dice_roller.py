#Student Name: Alexander Munro
#Student Number: 10421895

#Import libraries required for script to function
import random
import statistics

#print_heading function to display a heading specified surrounded by a border
#Heading will always be centred
def print_heading(current_heading):
    print('=' * (len(current_heading) + 20))
    heading = current_heading.center(len(current_heading)+18)
    print(f'|{heading}|')
    print('=' * (len(current_heading) + 20))

#invalid_roll function to save typing the whole print statement multiple times
def invalid_roll():
    print('Invalid roll, please enter "h" for help.')

#display welcome heading to user
print_heading('Welcome to dice roller ultimate edition!')

#initiate overall script variables, these will not be reset each cycle or roll of dice
exit = False
total_roll_number = 0
total_exploded_number = 0

#while loop while continue until user exits the script
while exit == False: 
    #prompt user for input and convert to lowercase   
    user_input = str.lower(input('Enter a roll ("h" for help, "x" to exit):'))
    #check if user has asked for help and display help
    if user_input == 'h':
        print_heading('Help!!')
        print('Enter a roll in "[quantity]d[sides]" format.')
        print('e.g. Enter "4d6" to roll four six-sided dice.\n')
        print('Add "!" to the end, e.g. "4d6!", for "exploding dice".')
        print('Dice that roll max number are re-rolled and added.\n')
    #check if user has exited script and display final statistics before exiting
    elif user_input == 'x':
        print_heading('Total Statistics')
        print(f'Total number of rolls: {total_roll_number}')
        print(f'Total number of normal rolls: {total_roll_number - total_exploded_number}')
        print(f'Total number of exploded rolls: {total_exploded_number}')
        print_heading('Goodbye')
        
        exit = True
    #check for a valid dice roll by user
    #check if the user input contains a letter 'd' and split into a list on the letter 'd', if no letter 'd' detected prompt the user it was an invalid roll and restart loop
    elif 'd' in user_input:
        dice_roll = user_input.split('d')
        #check the user input was only split once and now contains 2 values
        if len(dice_roll) == 2:
            #attempt to convert the first value (qunatity) to an integer, if this fails prompt the user it was an invalid roll and restart loop
            try:
                quantity = int(dice_roll[0])
            except:
                invalid_roll()
                continue
            #check to see if the user has chosen exploding dice, if so set exploding_dice to True and attempt to convert the value minus ! to an integer, if this fails prompt the user it was an invalid roll and restart loop
            if dice_roll[1].endswith('!'):
                print('Exploding dice used!')
                exploding_dice = True
                try:
                    sides = int(dice_roll[1][:-1])
                except:
                    invalid_roll()
                    continue
            #if no ! at the end of the second value, set exploding_dice to false and attempt to convert the value to an integer, if this fails prompt the user it was an invalid roll and restart loop
            else:
                exploding_dice = False
                try:
                    sides = int(dice_roll[1])
                except:
                    invalid_roll()
                    continue
            
        else:
            invalid_roll()
            continue
        
        #initiate variables for rolling sessioncounting rolls, explosions and storing values of each
        roll_list = []
        explosion_number_list = []
        roll_number = 0
        explosion_number = 0
        
        #roll dice
        #using the value stored in quantity, loop through each dice roll 'quantity' number of times
        for roll in range(quantity):
            total_roll_number += 1
            exploding_list = []
            #using the random library, assign a random integer between 1 and 'sides' to the individual roll
            individual_roll = random.randint(1, sides)
            roll_list.append(individual_roll)
            #display information about current dice roll
            print(f' Die {roll_number} of {quantity}... You rolled a {individual_roll}!')            
            if exploding_dice == True:
                #if the user has chosen exploding rolls check if the current roll is equal to 'sides' indicating a max roll, set exploding to True and enter the exploding dice loop                
                if individual_roll == sides:  
                    total_exploded_number += 1                  
                    exploding = True
                    exploding_list.append(individual_roll)
                    single_dice_explosion = 0
                    #use a while loop to continue rolling exploding dice until a max roll is not achieved
                    while exploding == True:
                        single_dice_explosion += 1
                        explosion_number += 1                        
                        kaboom_roll = random.randint(1, sides)
                        exploding_list.append(kaboom_roll)
                        roll_list.append(kaboom_roll)
                        #display information about current exploding roll
                        print("   Kaboom!")
                        print(f'   Exploded a {kaboom_roll}, exploding total of {sum(exploding_list)}!')
                        #check to see if a exploding roll has failed to acheive a max roll and exit exploding loop
                        if kaboom_roll != sides:
                            explosion_number_list.append(single_dice_explosion)
                            exploding = False
            roll_number += 1
        #display statistics about current roll session
        print_heading('Roll Statistics')      
        print('Rolls: ',', '.join(map(str,roll_list)))          
        print(f'Total: {sum(roll_list)}')
        print(f'Average: {statistics.mean(roll_list)}')
        print(f'Minimum: {min(roll_list)} ({roll_list.count(min(roll_list))} {"occurence" if roll_list.count(min(roll_list)) < 2 else "occurences"})')
        print(f'Maximum: {max(roll_list)} ({roll_list.count(max(roll_list))} {"occurence" if roll_list.count(max(roll_list)) < 2 else "occurences"})')
        #add extra statistics if the user chose exploding dice
        if exploding_dice == True:
            print(f'Exploded Rolls: {explosion_number}')
            if explosion_number_list:
                print(f'Most explosions of a single dice: {max(explosion_number_list)}')



    else:
        invalid_roll() 
        continue       
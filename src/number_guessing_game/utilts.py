from random import randint


def game():
    print('Welcome to Guess Number Game!\n')
    print('''
    Our rules are quiet simple:
    I'm thinking of a number between 1 and 100.
    You have to guess the correct number.\n\n''')
    
    
    difficulty=input('''    Please select the difficulty level:
    1. Easy (10 chances)
    2. Medium (5 chances)
    3. Hard (3 chances)\n''').strip().lower()
    
    
    
    if difficulty in ['easy','1']:
        chances=10
    elif difficulty in ['medium','2']:
        chances=5
    elif difficulty in ['hard','3']:
        chances=3
    else:
        print('Wrong input')
        return

    
    target=randint(1,100)
    
    user_input=''
    attempt=0
    
    while True:
        user_input=input(': ').strip()
        
        try:
            guess=int(user_input)
        except ValueError:
            print('Invalid input! Integer number expected')
            continue
        
        attempt+=1
        
        
        if guess==target:
            print(f'Congratulations! You guessed the correct number in {attempt} attempts.')
            break
        
        
        if attempt==chances:
            print(f'You lost. The correct number was {target}')
            break
        
        
        if guess>target:
            print(f'Incorrect! The number is less than {guess}.')
        
        else:
            print(f'Incorrect! The number is greater than {guess}.')
            
        print(f'Chances left {chances-attempt}')
           
        
        
        
    
    
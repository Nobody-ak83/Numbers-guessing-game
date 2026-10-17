from number_guessing_game.utilts import game
import time

def main():
    
    while True:
        start_time=time.perf_counter()
        game()
        end_time=time.perf_counter()
        print(f'Your time is {end_time-start_time}')
        
        again=(input('Wanna play again? (Yes/No y/n)').strip().lower())
        
        if again in ['no','n']:
            break
        
        
if __name__=='__main__':
    main()
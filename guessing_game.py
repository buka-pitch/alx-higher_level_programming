#!/usr/bin/python3
import random
import os
def main_game_loop(message="wrong number try again"):
    while True:
        print("welcome to the Guessing Game")
        life=3
        Z_number = random.randint(0,10)
        while life > 0:
            player_answer = int(input("Guess the number\n"))
            if life > 1:
                if player_answer == int(Z_number):
                    print("You Win Congra", 'remaning {} life\n'.format(life))
                    break
                else:
                    life -= 1
                    print(message,'your remaining life is {}'.format(life))
            else:
                print("Game Over",)
                print("DO you want to play again ?")
                yes_or_no = input("yes or No ?")
                if 'yes' in yes_or_no:
                    os.system("cls")
                    break
                else:
                    exit()
                
        
main_game_loop()
        


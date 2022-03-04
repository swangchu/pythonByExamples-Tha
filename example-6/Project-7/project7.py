# This project implements the Rock, Paper and Scissors game.

import random

print("Lets play Rock, Paper and Scissors.")

print("Your opponent is a Robot.")

choice = ("Rock","Paper","Scissors")

play = "Yes"

while play == "Yes":
  
    game ={}
    robot = random.choice(choice)
    
    user = input("Your turn:")
    
    game["robot"] = robot
    
    game["You"] = user
    
    if game["robot"] == choice[0] and game["You"]== choice[0] or game["robot"] == choice[1] and game["You"]== choice[1] or game["robot"] == choice[2] and game[“You"] == choice[2]:
    
        print("Draw")
        
        play = input("Type Yes to continue:")
        
    elif game["robot"] == choice[0] and game[“You"] == choice[1]:
                                             
        print("You Won")
                                             
        print("Robot chose",game["robot"])
                                             
        play = input("Type Yes to continue:")
                                             
    elif game["robot"] == choice[1] and game[“You"] == choice[2]:
                                             
        print("You Won")
                                             
        print("Robot chose",game["robot"])
                                             
        play = input("Type Yes to continue:")
                                             
    else:
                                             
        print("Robot won!!")
                                             
        print("Robot chose",game["robot"])
                                             
        play = input(“Type Yes to continue:”)

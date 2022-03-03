# Program to generate a random number and gets a number from the user.
# Check if the two numbers are equal. 
# If the user entered number is higher or lower than the random number tell the user about it. 
# The program gives choice to the user to terminate the loop.

import random

# The variable randNum stores the random number.

randNum = random.randint(1,100)

# The variable ch stores user’s choice, y for yes and n for no.
ch = “y”

while ch == “y”:
    
    # The variable g stores the user entered number.
    g=int(input(“Guess a no.”))
    
    if g == randNum:
      
         print(“You got it right”)
        
         break
          
    elif g > randNum:
      
         print(“HIGH”)
        
         ch =input(“Continue?y/n”)
          
    else:
      
         print(“HIGH”)
        
         ch =input(“Continue?y/n”)

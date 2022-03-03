# Program to simulate Lottery system. The program generates an alphanumeric, an alphabet followed by a number, and compares with user ticket of same format.
# If the computer generated ticket is same as user’s ticket than display you won message. Otherwise display a message of regret.

import random

# Generate a random integer between 1 and 100
randNum = random.randint(1,100)

# Generate a random letter from ABCDE
apha = random.choice("ABCDE")

# Join the letter and random number like A55
winTicket = apha+str(randNum)

ch = "y"
# Continue the while loop as long as user choice is y which is yes.

while ch == "y":
  
     ticket=input("Ticket no.")
    
     if winTicket == ticket:
        
         print("Won $1,000,000")
          
         break 
        
     else:
      
         print("Try again")
        
         ch =input(“Continue?")

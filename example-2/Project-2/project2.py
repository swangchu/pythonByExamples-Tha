# Project to catgorize depending on the average marks

avg = int(input("Enter your average mark: "))

if avg > 80 and avg < 101:
  
     print("Distinction")
    
elif avg > 70 and avg < 81:
  
     print("First Division")
    
elif avg > 60 and avg < 71:
  
     print("Second Division")
    
elif avg > 39 and avg < 61:
  
     print("Third Division")
    
else:
  
    print("Repeat")
    
    repeat = input("Want to repeat?y/n") 
    
    if not "n":
    
         print("Welcome back")

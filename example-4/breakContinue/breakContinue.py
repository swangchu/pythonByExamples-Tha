# This example use continue and break statement to control the flow of loop

for i in range(7):
  
     if i == 5:
         
         # break statement terminate the loop
         break

     print(i) 
    # The print will output 0 1 2 3 4
    
for j in range(10):
  
     if j == 5:
      
         # contrinue statement will bypass iteration
         continue
          
     print(j) 
    #The output 0 1 2 3 4 6 7

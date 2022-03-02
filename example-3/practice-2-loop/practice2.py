# This example demonstrate to generate multiplication table for a number based on user's choice.

num = int(input(“Enter a number”))

for i in range(1,30):
    
    mul = num * i
    
    print(num ," * ",i,"=" ,mul)
     
# Output : 3 * 1 = 3

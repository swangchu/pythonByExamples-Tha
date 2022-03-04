# Project to simulate calculator

print("Calculator")

print("----------------")

def add(n, m):
  
        sum = n + m
    
        return sum
    
def sub(n,m):
  
        diff = n - m
    
        return diff
    
def mult(n,m):
  
        prod = n * m
    
        return prod
    
cont = "Y"

while cont == "Y":
  
    print("Type +, -, *")
    
    op = input("Your choice:")
    
    num1=int(input("Number1:"))
    
    num2=int(input("Number2:"))
    
    if op == "+":
      
        sum_num=add(num1, num2)
        
        print(“Sum: ",sum_num)
              
    elif op == "-":
              
        diff=sub(num1, num2)
              
        print(“Diff: ”,diff)
              
    else:
              
        prod=mult(num1, num2)
              
        print("Product ",prod)
              
    cont=input("Continue?Y/N")

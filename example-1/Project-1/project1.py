# Get the user input and type cast
# where ever necessary

name = input("Enter name:")

eng = int(input("English mark:"))

dzo = int(input("Dzongkha mark:")) 

math = int(input("Maths mark:")) 

sci = int(input("Science mark:")) 

# Calculate average

avg = int((eng + dzo + math + sci ) / 4)

# Display the result to the user 

print("- - - - - - - - - - - - -") 

print(name)

print("English: ",eng) 

print("Dzongkha: ",dzo) 

print("Mathematics:",math) 

print("Science: ",sci) 

print("--------—- --") 

print("Average ",avg)

print(“- - - - - - - - - - - - ”)

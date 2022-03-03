# This program gets student's name and their english, dzongkha, and math marks. 
# These user inputs are appended to the empty list. It displays the item and has a features to edit the marks.

student = []

name = input("Your name:")

eng = int(input("Eng marks:"))

dzo = int(input("Dzo marks:"))

math =int(input("Math marks"))

student.append(name)

student.append(eng)

student.append(dzo)

student.append(math)

print("-----------------")

print("Name:",student[0])

print("English: ",student[1])

print("Dzongkha:",student[2])

print("Math:",student[3])

print(“------------------")
      
edit = input("Edit?y/n:")
      
while edit == 'y':
      
    print("Enter 1 for Eng.")
      
    print("Enter 2 for Dzo.")
      
    print("Enter 3 for Math.")
      
    index = int(input("choice:"))
      
    item =int(input(“Enter mark:"))
                    
    student[index] = item
                    
    edit = input("Edit?y/n:")
                    
print("----------------------")
                    
for item in student:
                    
print(item)

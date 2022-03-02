# Program to calculate the average weight of the all students in a class.

# The variable totStd stores the class strength.
totStd = int(input(“Total std:"))

# The variable totWt stores the total weight of the class students.
totWt = 0
                   
for i in range(totStd):
                   
     # The variable wt get and stores weight of the individual students.              
     wt = float(input("Enter student number ",i+1,"weight :"))
                   
     totWt = totWt + wt

# The variable avgWt stores the integer form of the class average weight.
avgWt = int(totWt / totStd)
                   
if avgWt > 70:
                   
    print("Average",avgWt,"greater than 70")
                 
else:
                   
    print("Average",avgWt,"smaller than 70")

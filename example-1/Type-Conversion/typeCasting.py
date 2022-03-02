# In this example data type conversion is done
#-----------------------------------------------

costPrice = 88 

# Since 120 is enclosed with double quote it is considered a string rather than an integer.
sellingPrice = “120”

# costPrice which is an integer is converted to float data type 
newCP = float(costPrice)

# costPrice which is an integer is converted to string
anotherCP = str(costPrice)

# sellingPrice which is a string is converted to an integer.
newSP = int(sellingPrice)

print(costPrice)


print(newCP)       # This print function will display 88.0 which is float 

print(anotherCP)  # This print function will display 88 which is a string

print(sellingPrice)

print(newSP)       # This print function will display 120 which is an integer

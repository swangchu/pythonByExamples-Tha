# This example uses dictionary methods

# Empty dictionary is declared
bio={} 

# name is the key and Dawa is a value assined to the key
bio["name"]= "Dawa"

bio["age"]= 18

# using for loop to display the content of the dictionary
for key in bio:
  
     print("Key:",key)
    
     print("value:",bio[key])
      
bio.pop("age")

print(bio)  
#Output  {'name': 'Dawa'}

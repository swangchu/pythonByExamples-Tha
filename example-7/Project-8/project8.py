# Project uses functions and return values

eng1 =int(input("English I:"))
                
eng2 =int(input("English II:"))
                
dzo1 =int(input("DzongkhaI:"))

dzo2 =int(input("DzongkhaII:"))

def eng_marks():
  
    sum = eng1 + eng2
    
    return sum
  
  
def dzo_marks():
  
    sum = dzo1 + dzo2
    
    return sum
  
dzo_avg = dzo_marks() / 2

eng_avg = eng_marks() / 2

if dzo_avg<40 or eng_avg < 40:
  
    print("Repeat")
    
else:
    print("Congrtulation")
    
    print("English: ",eng_avg)
    
    print("Dzogkha: ",dzo_avg)

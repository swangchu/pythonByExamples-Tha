# Example for empty set and set methods

vehicle_no = set() 

vehicle_no.add(“BP-2-B6666”) 

vehicle_no.add(“BP-2_B7777”) 

vehicle_no.add(“BP-2_B1111”) 

print(vehicle_no)
#{‘BP-2-B1111', 'BP-2-B7777', 'BP-2-B6666'} 

vehicle_no.remove(“BP-2-B6666”) 

print(vehicle_no) 
#{'BP-2-B1111', 'BP-2-B7777'}

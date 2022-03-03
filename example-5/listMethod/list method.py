# This examples uses list methods

biodata = ["sonam",16,"Bhutan"]

biodata.append("Samtse")

print(biodata)
# ["sonam", 16, "Bhutan", "Samtse"] 

biodata.pop()

print(biodata)
# ["sonam", 16, "Bhutan"] 

print(biodata.index(16))
# at the index 1

marks = [88, 66,56,71,45] 

marks.sort()

print(marks)
#[45, 56, 66, 71, 88] 

marks.reverse()

print(marks)
#[88, 71, 66, 56, 45] 

print(marks.count(71)) 
# 1 

marks.extend([100,55]) 

print(marks)
# [88, 71, 66, 56, 45, 100, 55] 

marks.remove(100)

print(marks)
# [88, 71, 66, 56, 45, 55]

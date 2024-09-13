# set

#add
dwaves = {"thorin","balin","dwalin"}
dwaves.add("gimli")
print(dwaves)

#clear
dwaves = {"thorin","balin","dwalin"}
dwaves.clear()
print(dwaves)

#pop
dwaves = {"thorin","balin","dwalin"}
dwaves.pop()
print(dwaves)

#union
dwaves1 = {"thorin","balin","dwalin"}
dwaves2 = {"gimli","bofur","thorin"}
dwaves3 = {"fili","kili"}
print(dwaves1.union(dwaves2,dwaves3))

#copy
seta = {11,12,20,30}
setb = seta.copy()
print(setb)

#discard
dwaves = {"thorin","balin","dwalin"}
dwaves.discard("balin")
print(dwaves)

#difference
dwaves1 = {"thorin","balin","dwalin"}
dwaves2 = {"gimli","bofur","thorin"}
dwaves3=dwaves1.difference(dwaves2)
print(dwaves3)

#intersection
num1 = {10,20,30,40,50}
num2 = {10,90,80,70}
print(num1.intersection(num2))

#isdisjoint
num1 = {10,20,30,40,50}
num2 = {10,90,80,70}
print(num1.isdisjoint(num2))
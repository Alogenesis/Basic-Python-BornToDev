tupleExample = ("Winai","Winai2","Winai3")
print(tupleExample)
tupleExample2 = ("Bank1","Kay1")
tupleExample3 = tupleExample+tupleExample2*2
print(tupleExample3)
print(tupleExample3[:3])
'''Tuple list can't remove, add or edit'''
print("Bank1" in tupleExample3)
for i in tupleExample3:
    print(i)
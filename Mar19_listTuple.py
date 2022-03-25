from statistics import mean
#Create an empty list (two ways)
list1 = []
print(list1)
print(type(list1))

list2 = list()
print(list2)
print(type(list2))

#Concatenate with [5,6,7,8]
list3 = [5,6,7,8]
list4 = list1 + list3
print(list4)

#add 8,9,1,5,6,7,8,1 elements to that list
list5 = [8,9,1,5,6,7,8,1]
list4.extend(list5)
print(list5)

#Find frequency of 8 (count)
print("Frequency of 8:",list5.count(8))

#find the mean of the list
print("Mean:",mean(list5))

#find sum (List) + min + Max
print("Sum:",sum(list5))
print("Min:",min(list5))
print("Max:",max(list5))

#Find median of the list
list5.sort()
print("list5 after sorting",list5)
med1 = len(list5)//2
print("median:",list5[med1])

#remove duplicates from list and give output in the format of tuple
list6 = [8,9,1,5,6,7,8,1]
print(tuple(set(list6)))

#Tuple

#Create two tuples (1,4,5,6,7,8) (5,6,7,8,9)
tup1 = (1,4,5,6,7,8)
tup2 = (5,6,7,8,9)

#Find the common elements between two tuples
tup1_set=set(tup1)
tup2_set=set(tup2)
common=(tup1_set & tup2_set)
print("common:",tuple(common))
             
#Concatenate both tuples and remove duplicates from tuple
print("Concatenation output",tup1+tup2)
tup3 = tup1+tup2
print("Without duplicates:",set(tup1+tup2))
#Find the index value of 9 (after concatenation)
print("Index value of 9", tup3.index(9))

#multiply above elements 3 times
print("Multiplied Result",tup3*3)

#Sets

#Create two empty sets
set1 = set()
set2 = set()

#update set1 with 7,8,9,1,2,3,4,5,0
set1 = {7,8,9,1,2,3,4,5,0}
#update set2 with 4,5,6,0
set2 = {4,5,6,0}
print("set1:",set1)
print("set2:",set2)
#check whether set2 is subset of set1 or no ?
print("is subset?",set2.issubset(set1))
#check whether both have common elements are no ?
set3=(set1.intersection(set2))
print("Intersection:",set3)
#remove 8 from set 1 and set 2 ==> find the inferences
set1.remove(8)
# set2.remove(8)   --> KeyError: 8
#discard 0 from set1 and set2
set1.discard(0)
set2.discard(0)
print("After discard set1:",set1)
print("After discard set2:",set2)
#find collection of both sets ===> set1 and set2
set4 = set1.union(set2)
print("Collection:",set4)

#Dict 

#create a dictionary
#{1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}
dict1={1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}
#Extract "bobtn" from above dictionary
print("Extract bobtn from dict1:",dict1[3][0][0:-1:2])
#Extract "arbeg" from above dictionary
print("Extract arbeg from dict1:",dict1[3][2][-1:-6:-1])
#print all keys in dictionary and convert it into tuple

d1 = dict1.keys()
print("Keys in dict1:",d1)
d2 = tuple(d1)
print("After coverting to tuple",d2)
#Find the average of all numbers available under key "2"
num = dict1[2]
Average1 = sum(num)/len(num)
print("Average of numbers",Average1)










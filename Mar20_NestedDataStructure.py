#Task1:

Li1 = [2,3,4,5,[45,56,67,78,[111,222,333,[5555,3333,[10000,50000,"python","computer"],1111,7777,8888],444,555,666,777],89,23,34]]
print("To print 5:",Li1[3])
print("To print 56:",Li1[4][1])
print("To print 222",Li1[4][4][1])
print("To print 50000",Li1[4][4][3][2][1])
print("To print put",Li1[4][4][3][2][3][3:6])
print("To print 5555",Li1[4][4][3][0])
print("To print 7777",Li1[4][4][3][4])
print("To print 666",Li1[4][4][6])
print("To print 89",Li1[4][5])
print("To print on",Li1[4][5])
print("To print 333",Li1[4][4][2])
print("To print 3333",Li1[4][4][3][1])

#Task2:
a = [1,2,3,4,[100,101,102,"Computer_science"],200,203]

#Extract #science #computer
print(a[4][3][0:8])
print(a[4][3][9:])

#Task3 Extract
#666
#201
#102
#999
#777
a1 = [1,2,3,4,[101,102,103,[201,202,[999]], 666, 777]]
print(a1[4][4])
print(a1[4][3][0])

print(a1[4][1])
print(a1[4][3][2][0])
print(a1[4][5])

#Task4: Extract
#ll
#thon

Li2 = [2,3,"python","hello",4,5,0]  

print(Li2[3][2:4])
print(Li2[2][2:])

# Task5 Output Prediction 11 6666 6666 7777 7777 222 7777 [33, 44]
Li3 = [1,2,3,4,5,[11,22,33,44,55,[111,222,333,444],6666,7777],7777]

print(Li3[5][0])
print(Li3[5][6])
print(Li3[5][-2])
print(Li3[5][7])
print(Li3[6])
print(Li3[5][5][1])
print(Li3[-2][-1])
print(Li3[-2][2:4])

#Task6:
#py
#ello
#en
#zoo
#Bot
a2 = {1: [1,2,3,"python"], 2:{10:"hello",20:"welcome",40: "science"}, 99: {3,4,5,6}, 40:{1:"zoology", 2:"Botany"}}

print(a2[1][3][0:2])
print(a2[2][10][1:])
print(a2[2][40][3:5])
print(a2[40][1][0:3])
print(a2[40][2][0:3])

#Task7: Convert below two lists in to a dictionary

Li4=[1,2,3,4,5]
Li5=["python","cpp","c","java","php"]
print(dict(zip(Li4,Li5)))
#output - {1: 'python', 2: 'cpp', 3: 'c', 4: 'java', 5: 'php'}
#Task8: Convert below set in to a list

S1={5,4,3,6,2,7,1}
print(list(S1))
#output - [1, 2, 3, 4, 5, 6, 7]

# Task9: Remove duplicates from below list

Li6=[5,4,3,6,2,7,1,2,3,4,1,2,3,4,5,6,5]
print(set(Li6))
#output - {1, 2, 3, 4, 5, 6, 7}

#Task10: convert below one to tuple

Li7=[5,4,3,6,2,7,1,2,3,4,1,2,3,4,5,6,5]
Tup1=tuple(Li7)
print(Tup1)
print(type(Tup1))








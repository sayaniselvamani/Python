#int ===> float str  bool
#int to float
a1 = 10
b1 = float(a1)
print(f"Datatype of a1:{a1} is {type(a1)}")
print(f"Datatype of b1:{b1} is {type(b1)}")

#int to str
a2 = 20
b2 = str(a2)
print(f"Datatype of a2:{a2} is {type(a2)}")
print(f"Datatype of b2:{b2} is {type(b2)}")

#int to bool
a3 = 30
b3 = bool(a3)
print(f"Datatype of a3:{a3} is {type(a3)}")
print(f"Datatype of b3:{b3} is {type(b3)}")
###########################################
#float ===> int bool str
#float to int
c1 = 20.0
d1 = int(c1)
print(f"Datatype of c1:{c1} is {type(c1)}")
print(f"Datatype of d1:{d1} is {type(d1)}")

#float to bool
c2 = 0.0
d2 = bool(c2)
print(f"Datatype of c2:{c2} is {type(c2)}")
print(f"Datatype of d2:{d2} is {type(d2)}")

#float to str
c3 = 20.0
d3 = str(c3)
print(f"Datatype of c3:{c3} is {type(c3)}")
print(f"Datatype of d3:{d3} is {type(d3)}")
############################################
#bool ===> int float str
#bool to int
A1 = False
B1 = int(A1)
print(f"Datatype of A1:{A1} is {type(A1)}")
print(f"Datatype of B1:{B1} is {type(B1)}")

#bool to float
A2 = True
B2 = float(A2)
print(f"Datatype of A2:{A2} is {type(A2)}")
print(f"Datatype of B2:{B2} is {type(B2)}")

#bool to str
A3 = True
B3 = str(A3)
print(f"Datatype of A3:{A3} is {type(A3)}")
print(f"Datatype of B3:{B3} is {type(B3)}")
###########################################
#str ===> int bool float
#str to int
C1 = 10
# C1 = 'welcome' ValueError: invalid literal for int()
D1 = int(C1)
print(f"Datatype of C1:{C1} is {type(C1)}")
print(f"Datatype of D1:{D1} is {type(D1)}")
#str to bool
C2 = 'welcome'
D2 = bool(C2)
print(f"Datatype of C2:{C2} is {type(C2)}")
print(f"Datatype of D2:{D2} is {type(D2)}")
#str to float
#C3 = 'welcome' ValueError: could not convert string to float: 'welcome'
C3 = '20'
D3 = float(C3)
print(f"Datatype of C3:{C3} is {type(C3)}")
print(f"Datatype of D3:{D3} is {type(D3)}")


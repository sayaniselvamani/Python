# Task1: Get one string from user
# identify the middle character of the string

str1 = input("Enter a string")
midValue = (len(str1)//2)
print("Middle value of string is", str1[midValue])

#Task2: Get a string and strip

str2 = input("Enter a string to strip:")
print(str2.strip("*"))
print(str2.rstrip("*"))
print(str2.lstrip("*"))

#Task3: (name<space>float)
# collect three strings from user:  name<space>float
# split and with index find the sum of float values
string1 = input("Enter the 1st string in format name<space>float:")
string2 = input("Enter the 2nd string in format name<space>float:")
string3 = input("Enter the 3rd string in format name<space>float:")
split1 = string1.split()
split2 = string2.split()
split3 = string3.split()
Sum = float(split1[1]) + float(split2[1]) + float(split3[1])
print("Sum of float values:", Sum)

#Task4:
#collect two strings from user
#string1: python String2: java output ===> jythonpava64hv
str3 = input("Enter the 1st string:")
str4 = input("Enter the 2nd string:")
len1 = len(str3)
len2 = len(str4)
m1 = len1//2
m2 = len2//2
print("Output:",str4[0]+str3[1:]+str3[0]+str4[1:]+str(len1)+str(len2)+str3[m1]+str4[m2])

#Task5:
#Collect two strings from user to concatenate ascii value
#output: p  +  c   ===> ascii value of p + ascii value of c  ====>  198 (ord , chr)
str5 = input("Enter the 1st string")
str6 = input("Enter the 2nd string:") 
len5 = len(str5)//2
print("len5",len5)
len6 = len(str6)//2
print("len6",len6)
m5 = str5[len5]
print(m5)
m6 = str6[len6]
print(m6)
print(int(ord(m5))+int(ord(m6)))

#Task6:
#collect one string from user: string: computer output: c6r

str7 = input("Enter a string")
len7 = len(str7[1:-1])
print("output",str7[0]+str(len7)+str7[-1])

#Hackerrank
#Task7: Say hello world with python
str8 = "Hello, World!"
print(str8)

#Task8: convert all lowercase letters to uppercase letters and vice versa. Length less than 1000.
str9 = "Python is using interpreter"
print(str9.swapcase())

#Task9:You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:

#Hello firstname lastname! You just delved into python.

str10 = input("Enter first name:")
str11 = input("Enter last name:")
print(f"Hello {str10} {str11}! You just delved into python")

#Task10: Mutation : Input string - abracadabra     s = 'abracadabra'
#        position = 5, character = k
str11 = "abracadabra"
str11 = str11[0:5] + "k" + str11[6:]
print("After inclduing k at position 5:", str11)

#Task11: Arithmetic operator

Num1 = int(input("Enter the 1st number:"))
Num2 = int(input("Enter the 2nd number:"))
print("Addition",Num1+Num2)
print("Subrataction",Num1-Num2)
print("Multiplication",Num1*Num2)
    
#Task12: python divison

num1 = int(input("Enter the 1st number:"))
num2 = int(input("Enter the 2nd number:"))
print("Integer Division",num1//num2)
print("Float Division",num1/num2)


#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Rounak Chatterjee
#
# Created:     15-06-2022
# Copyright:   (c) Rounak Chatterjee 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Q1
word=input('Enter a string: ')
length=len(word)
rev_str=''
for i in range(0,length):
   rev_str+=word[length-1-i]
print(rev_str)


#Q2
range_start=int(input('Enter start range'))
range_end=int(input('Énter end range' ))
num=int(input('Enter a number'))

for i in range(range_start,range_end+1):
    if i%num==0:        #Checking remainder for divisibility
        print(i,'is divisible by ',num)



#Q3
import math
a=int(input("Enter first side: "))
b=int(input("Enter second side: "))
c=int(input("Enter third side: "))
if a+b>c and b+c>a and c+b>a:       #Checking if triangle is possible or not
  s=(a+b+c)/2                       #s is semi-perimeter
  area=round(math.sqrt(s*(s-a)*(s-b)*(s-c)),2)
  print(f"The area of triangle is {area}")
else:
  print("Invalid input of sides,triangle not possible")



#Q4
for i in range(1,6):
  c=0                       #c is a counter for printing '*'
  for j in range(1,i+1):
    c+=1
  print('*'*c)



a=4
while a>0:
  d=0                      #d is a counter for printing '*'
  for b in range(1,a+1):
    d+=1
  print('*'*d)
  a-=1
print( )



#Q5
alphabets=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
rows=int(input("Enter number of rows"))
c=0
for i in range(1,rows+1):
  for j in range(1,i+1):
      print(alphabets[c%26],end="")           #use of end keyword for line formatting
      c+=1
  print()




#Q6
range_start=int(input("Enter starting range"))
range_end=int(input("Enter ending range"))
for num in range(range_start,range_end+1):
  c=0
  for i in range(1,num+1):
    if (num%i==0):
      c+=1
  if c==2:                              #prime number is divisible by only 1 and itself
    print(f"{num} is a prime number")


#Q7
for i in range(1,501):
  if i%7==0 and i%11==0:
    print(i)



#Q8
num_list=[]
for x in range(1,11):
  x=int(input("Enter an integer: "))
  num_list.append(x)
print(num_list)
for number in num_list:
  if number>0:
    print(f"{number} is a positive number ")
  if number<0:
    print(f"{number} is a negative number ")
  if number%2==0:
    print(f"{number} is an even number ")
  if number%2==1:
    print(f"{number} is an odd number ")

for i in num_list:
  occ=0                             #counter for occurences of a number in list
  for j in num_list:
    if i==j:
      occ+=1
  print (f"{i} occurs {occ} times")


#Q9
word_list=[]
elements=int(input('Enter total elements in the list'))
for word in range(1,elements+1):
  x=input('Enter a word ')
  word_list.append(x)

for element in word_list:
  occ=0                                 #counter for occurrences in a list
  for element1 in word_list:
    if element==element1:
      occ+=1
  print (f"{element} occurs {occ} times")
# a=[10,20,30,40,50]
# print(type(a))
# list2=[12,10.5,"hello",True,"false"]
# print(list2)

#ACCESSSING ELEMENTS 
# list1=[10,20,30,40,50,]
# print(list1[0])
# print(list1[1])
# print(list1[2])
# print(list1[3])
# print(list1[4])
# print(list1[-1])
# print(list1[-2])
# print(list1[-3])
# print(list1[-4])
#slicing
# slc1=["ntr","balaya","pspk","bob","bhai"]
# print(slc1[:3])
# print(slc1[1:4])
# print(slc1[:2])
# print(slc1[-2:4]) 

# #ADDING ELEMENTS
# kalkicast=["prabahs","kamal","ba-*-*chan","ssr"]
# print(kalkicast=
# kalkicast.append("deesha patani")
# print(kalkicast)
# #searching and checking
# a=[2,4,6,8,10,12,14]
# if 2 in a:
#     print("yes iten is present in the list")
#     print(3 not in a)
# print(a.index(8))
# print(a.count(8))
# st=[25,12,5,31,13,18,7,45,8,55,68]
# st.reverse()
# st.sort()
# print(st)
# st.revers()
# print(st)
# st1=[25,8,4,7,10]
# st1.short(reverse=True)
#coping the list 
# frd1=["A","B","C","D","A","D","4E","c","A"]
# frd2=frd1.copy()
# #frd2[2]="B"
# print(frd1)

#using index loop
# cars=["thar","jaguar","bmw","audi"]
# a=len(cars)
# for  i in range(0,a):
#     print("cars=",i,cars[i])

#adding elements using for loop:

# list1=[]
# for i in range (0,3):
#     fruits=["mango","guava","apple"]
#     print("list1=",i,fruits[i])

# list2=[]
# n=int(input("enter the number of list values:"))
# for i in  range(0,n):
#     a=input("enter the list values: ")
#     list2.append(a)
# print(list2)

#sum of list items=10 20 30 40 50 without using sum().
# list=[10,20,30,40,50]
# sum=0
# for i in list:
#     sum=sum+i
# print(sum)

# list=["y","t","h","o","n"]
# sum="p"
# for i in list:
#     sum=sum+i
# print(sum)

#find the maximum & minimum number from list without using max() and min().
# list=[10,20,30,40,50]
# max=list[0]
# min=list[0]
# for num in list:
#     if num > max:
#         max = num
#     if num < min:
#         min = num
# print(max)
# print(min)

#searching for an element in list
# names=["sai","ravi","vdk","vamshi"]
# searching_names=input("enter the found name: ")
# found=False
# for i in names:
#     if searching_names==i:
#         found=True
# if found:
#     print("YES")
# else:
#     print("No")

#count even and odd numbers
# numbers=[7,10,12,17,18,23,31,45,227,229]
# even_cnt=0
# odd_cnt=0
# for i in range(len(numbers)):
#     if numbers[i]%2==0:
#         even_cnt+=1
#     else:
#         odd_cnt+=1
# print("number of even numbers are: ",even_cnt)
# print("number of odd numbers are: ",odd_cnt)

#reversing a list without revers
# numbers=[7,10,12,17,18,23,31,45,227,229]
# i=len(numbers)
# r_list=[]
# for i in range(i-1,-1,-1):
#     r_list.append(numbers[i])
# print(r_list)

#removing all negative numbers using loop
# numbers=[-55,-9,2,-8,-30,30,45,23,-19,72,-55,-18,7,0]
# postive_list=[]
# for i in  range(len(numbers)):
#     if numbers[i]>0:
#         postive_list.append(numbers[i])
# print(postive_list)


# #multiply each element in the list
# numbers=[56,9,2,8,30,30,45,23,19,72,55,18,7,0]
# m=int(input("enter the number to be multiplied: "))
# after_multiplication=[]
# for i in numbers:
#     after_multiplication.append(i*m)
# print(after_multiplication)

a=[1,2,3,4,5,6,7]
b=7
print(a+b)









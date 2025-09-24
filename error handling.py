#zero  divison error handling 
try:
    a=int(input("enter the numerator"))
    b=int(input("enter the denominator"))
    c=a//b
    print(c)
except ZeroDivisionError:
    print("error:divison by zero is not possible")
    
    #zero divison error handling example 2
try:
    i=3
    n=int(input("enter a number"))
    if n%i==0:
        print("yes:number is muliple of n")
    else:
        print("no:number is not multiple of n")
except ZeroDivisionError:
    print("error:divison by zero is not possible")
# #value error handling
try:
    rollno=int(input("enter your roll no:"))
except ValueError:
    print("error:given value is not an integer datatype")

# index error handling
try:
    list1=[10,20,30,40,50]
    i=int(input("enter the index value"))
    print("the value at index",i,"is",list1[i])
except IndexError:
    print("error:index value is out of range")

    #key error handling
try:
    dict1={"name":"siddhartha","age":19,"college":"MRCET"}
    key=input("enter the key to be searched")
    print("the value at key",key,"is",dict1[key])
except KeyError:
    print("error:key is not found in the dictionary")

    ##type error handling
try:
    list=[10,20,30]
    sum=list+5
    print(sum)
except TypeError:
    print("invalid type operation")

    #name error handling
try:
    print("x")
except NameError:
    print("error:variable is not defined")

    #file not found error handling
try:
    file=open("student.txt","r")
    file.read()
except FileNotFoundError:
    print("error:file is not found:")
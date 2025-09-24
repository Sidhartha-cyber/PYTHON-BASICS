def greet(name):
    print("hello ",name)
greet("siddhu")
#same task without function)

#TYPES OF FUNCTIONAL ARGUMENTS

#A.positional arguments
#when we pass arguments in the same order as the functional parameter,they are called positional argument

def greet(name,rollno):
    print("hello",name,"your rollno is",rollno)#execute the line
greet("siddhu","j4")#function calling

# B keyword arrgument
#when we pass a value or argument by writing the parameter(variable=value),they are called as key argument
def greet(name,rollno):
    print("hello",name,"your roll no is",rollno)#executive the lines
greet(name="siddhu",rollno="j4")
#c default argument
def greet(name="student"):
    print("hello",name)
greet()
greet(name="sai")

#variable length argument:
#L=10,20,30,40,50
def sum1(*list1):
    sum2=0
    for i in range(len(list1)):
        sum2=sum2+list1[i]
    print(sum2)
    print(type(list1))
sum1(10,20,30,40,50)





        
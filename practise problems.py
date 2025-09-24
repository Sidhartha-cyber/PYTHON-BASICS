#write a program to find the average of all numbers in alist.

# Define the list of numbers
numbers = [10, 20, 30, 40, 50]

# Check if the list is not empty to avoid division by zero
if len(numbers) > 0:
    average = sum(numbers) / len(numbers)
    print("The average is:", average)
else:
    print("The list is empty. Cannot calculate average.")

#count hopw many numbers are positive,negative and zero
list=[1,-2,3,0,4,-5,6,0,-7,-8,-6,0]
positive_cnt=0
negative_cnt=0
zero_cnt=0
for i in range(len(list)):
    if list[i]>0:
        positive_cnt+=1
    elif list[i]<0:
        negative_cnt+=1
    else:
        zero_cnt+=1
print("number of the positive numbers are: ",positive_cnt)
print("number of the negative numbers are: ",negative_cnt)
print("number of zero numbers are: ",zero_cnt)

#take the list of the names in print the longest names
names=["sai","varun","vamshi","mahesh","sidhartha"]
i=0

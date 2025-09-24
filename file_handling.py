#syntax
# file=open("filename","mode")
#mode=r,w,a,r+,w+,a+
#r=read
#w=write
#a=append
#r+=read and write
#w+=write and read
#a+=append and read
file=open("students.txt","w+")
file.read()
file.write("hello siddhu")
file.write("hello sai")
file.close()
file=open("students.txt","r+")
file.write("\nhello siddhu")
file.write("\nhello sai")
file.close()

#read
f=open('my data2','r')
print(f)
print(f.read())#print wholw data

#print one line or two
print(f.readline(),end="#")
print(f.readline())

#write and print
f1=open('abc','w')
f1.write("something")
f1.write("missing")

#append
f1=open('abc','a')
f1.write("mobile")

#copy
f1=open('abc','w')
for data in f:
    f1.write(data)

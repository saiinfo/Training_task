#1)object and class creation
class banglore:
    name=""
    work=""
    def job(self):
        print("lets work")
    def leave(self):
        print("lets sleep")
        
ramesh=banglore()
suresh=banglore()

ramesh.job()
#ramesh.leave()
suresh.leave()
#print(ramesh.name)
ramesh.name="ramesh"
suresh.name="suresh"

ramesh.work="yes"
suresh.work="no"

print(ramesh.name)
print("work:",ramesh.work)

print(suresh.name)  
print("work:",suresh.work)

ramesh.job()
suresh.leave()
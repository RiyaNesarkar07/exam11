import time
import tracemalloc
class emplooye:
    def __init__(self,name,desig,salary):
        self.name=name
        self.desig=desig
        self.salary=salary
    def read(self):
        self.name=input("enter the name:")
        self.desig=input("enter the desig:")
        self.salary=int(input("enter the salary:"))
    def displayDetails(self):
        print("name=",self.name)
        print("designation",self.desig)
        print("salary",self.salary)
start=time.process_time()
tracemalloc.start()
e1Array=[]
while(True):
    e1=emplooye('','',0)
    e1.read()
    e1Array.append(e1)
    ch=input("add more y/n?")
    if(ch=='n'):break
print("details of all emplooye")
for e1 in e1Array:
    e1.displayDeatails()
end=time.process_time()
print("space required=",tracemalloc.get_traced_memory())
print("time required=",(end-start))
tracemalloc.stop()

hhh

from time import time
from math import sqrt
from threading import Thread
from multiprocessing import Queue, Lock
now_time = time()
def sushu(n):
    flag = True
    for i in range(2,int(sqrt(n))+1):
        if n%i ==0:
            return False
    else:
         return flag
def xiancheng(start,end):
        t = 0
        global q
        lock.acquire()
        for i in range(start,end):
            if sushu(i):
                t +=i
        q.put(t)
        lock.release()
total = 1000000
interval  = total//8

sum = 0
index_1 = 2
processes = []
index_2 = interval+1
q = Queue()
lock = Lock()
count = 0
for i in range(1,8):
    p = Thread(target = xiancheng,args = (index_1,index_2))
    p.start()
    processes.append(p)
    index_1 = index_2
    index_2 = (i+1)*interval +1
p = Thread(target = xiancheng,args = (index_1,total+1))
p.start()
processes.append(p)
for p in processes:
    p.join()
while not q.empty():
    sum += q.get()
    count +=1
print(sum)
print(count)
end_time = time()
print(end_time-now_time)

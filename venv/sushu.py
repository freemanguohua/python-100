from time import time
from math import sqrt
now_time = time()
#num = [x for x in range(2,100001)]
def sushu(n):
    flag = True
    for i in range(2,int(sqrt(n))+1):
        if n%i ==0:
            return False
    return flag
sum = 0
count = 0
for i in range(2,1000001) :
    if sushu(i):
        sum +=i
        count +=1;

print(sum)
print(count)
end_time = time()
print(end_time-now_time)

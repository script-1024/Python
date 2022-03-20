from lib import *
def sort(i=0):
    print(f"第{i+1}次排序: ")
    for back in range(1,len(a)):
        for front in range(back):
            if a[front] > a[back]:
                a[front], a[back] = a[back], a[front]
        printAll(a)
    print("")


n=get("數列長度",min=1,cl=1)

times=get("執行次數",min=1,cl=1)

for i in range(times):
    a = fill(n)
    sort(i)
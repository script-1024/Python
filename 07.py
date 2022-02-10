#判斷質數
import math
while True:
    try: n=int(input())
    except: break
    if n<2: prime = False
    else:
        prime = True
        for i in range(2,int(math.sqrt(n))+1):
            if n%i == 0:
                prime = False
                break
    if prime: print("質數")
    else: print("非質數")
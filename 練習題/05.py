#完成數列
t = int(input())
for i in range(t):
    a,b,c,d = map(int,input().split(' '))
    if b-a == c-b:
        e = d + (b-a)
    else: e = d * int(b/a)
    print(a,b,c,d,e)
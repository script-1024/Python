# 半邊三角形
def half_tri(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print('*',end='')
        print('')

# 全三角形
def full_tri(n):
    k=n
    for i in range(0,n):
        for j in range(1,k):
            print(' ',end='')

        k = k-1

        for j in range(0,i+1):
            print('**',end='')
        print('')

while 1:
    wait = 1
    while wait:
        n = input('> ')
        if n != '': 
            n = int(n)
            wait = 0

        if n == 0:
            exit()
        elif n < 0:
            exit('長度必須為正值')

    '''---------------'''
    #half_tri(n)
    full_tri(n)

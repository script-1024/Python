from random import randint
from os import system,name
from time import sleep

def clear():
    system('cls' if name=="nt" else "clear")

def msg(txt="什麼也沒有..."):
    clear()
    print(txt)
    sleep(len(txt)*0.2)
    clear()

def isSet(value,t=int):
    try: type(value) 
    except: return 0 
    else: 
        if type(value)==t: return 1
        else: return 0

def get(tips="",min=0,max=100,retry=True,cl=False):
    n=''
    while 1:
        print(tips)
        try: n = int(input("> "))  
        except: msg("請輸入數字")
        if isSet(n):
            if n>=min and n<=max: break
            else: msg(f"不在範圍 {min}~{max} 內")
        if not retry: break
    if cl: clear()
    return n

def fill(n=1):
    a = {}
    for i in range(n):
        a[i] = randint(0,n*5)
    return a

def printAll(source):
    for i in range(len(source)-1):
        print(source[i],end=', ')
    print(source[len(source)-1],end="\n")
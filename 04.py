#平、閏年判斷
while True:
    try: y=int(input())
    except: break
    if y%4==0 and y%100!=0 or y%400==0: print("閏年")
    else: print("平年")
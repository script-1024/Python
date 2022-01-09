print("* 輸入「0」可以結束此程式")
while (1):
    
    
    print("* 請輸入一個西元年份")
    year = input("> ")

    if year != "":
        year = int(year)
    else:
        print("! 輸入格式有誤")
    


    if year == 0:
        print("! 程序已被使用者終止\n")
        exit()

    '''
    if "AD" in year:
        print(0)
        '''

    if (year % 4) != 0:
        print(f"* 不是閏年")

    elif (year % 100) != 0:
        print(f"* 是閏年")

    elif (year % 400) != 0:
        print(f"* 不是閏年")

    else:
        print(f"* 是閏年")

    print("\n")
while(True):
    try:
        a = 0
        b = 0

        a,b = map(int, input().split())
        count1 = 1
        count2 = 1
    
        if 0<=a<=20 and 0<=b<=20:
            
            for r in range(1, a+1):
                count1 *= r
            for s in range(1, b+1):
                count2 *= s

            sum = count1 + count2

            print(sum)

    except EOFError:
        break
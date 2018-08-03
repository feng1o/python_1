#-*-coding:utf-8 -*-


def Nseq(s, n):
    if(n == 1 and len(s) < 3):
        if (len(s) == 1):
            return float(s[0])
        elif(len(s) == 2):
            return float(s[0]) * 10 + float(s[1])
        elif(len(s) == 0):
            return -1000000
    elif (s == '100' and n == 1):
        return 100
    elif(n == 1 and len(s) > 2):
        return -1000000
    else:
        s1 = s[1:len(s)]
        x1 = float(s[0]) + Nseq(s1, n - 1)
        s2 = s[2:len(s)]
        x2 = float(s[0]) * 10 + float(s[1]) + Nseq(s2, n - 1)
        result = max(x1, x2)
        return result

if __name__ == '__main__':
    # result = Nseq("123456789987654321123456789012345678901234567890", 24)
    result = Nseq("99199",3)
    #result = Nseq("7277999517556851233678434227888136156861495873988149422724228586", 35)
    print(result)

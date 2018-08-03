
def Nsep(s, c):
    n = len(s)
    res = [[-10000 for j in range(c + 1)] for i in range(n + 1)]
    # print(res)
    res[1][1] = float(s[0])
    res[2][1] = float(s[0]) * 10 + float(s[1])
    res[2][2] = float(s[0]) + float(s[1])
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            if(j < i and i < 3 * j + 1):
                if(j >= 2):
                    x1 = res[i - 1][j - 1] + float(s[i - 1])
                else:
                    x1 = float(s[i - 1])
                if(s[i - 2] == 0):
                    x2 = -100000
                elif(i == 2):
                    x2 = float(s[i - 2]) * 10 + float(s[i - 1])
                else:
                    x2 = res[i - 2][j - 1] + \
                        float(s[i - 2]) * 10 + float(s[i - 1])
                if(i == 3 and s[0:3] == '100'):
                    x3 = 100
                elif(i == 3 and float(s[0:3]) > 100):
                    x3 = -1000000
                elif(i > 3 and s[i - 3:i] == '100'):
                    x3 = res[i - 3][j - 1] + 100
                else:
                    x3 = -100000
                x = max(x1, x2, x3)
                if(x > 0):
                    res[i][j] = x
    return res

if __name__ == '__main__':
    s = '7277999517556851233678434227888136156861495873988149422724228586'
    s2 = '821711602653177166294353276266861667971553521272636560133084248288828255676'
    s3 = '100'
    #s = '9240472250820632676729970691922158180166547841260363853818249554882589434199'
    #s = '12345678909876543211'
    n = 35
    res = Nsep(s, n)
    res2 = Nsep(s2, 40)
    res3 = Nsep(s3, 2)
    print(res[len(s)][n] / n)
    print(res2[len(s2)][40] / 40)
    print(res3[len(s3)][2]/2)
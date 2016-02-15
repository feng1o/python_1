# _*_ coding:utf-8 _*_
# import random
guess = int(temp)
while guess != secret:
    temp = input("重新input..")
    guess = int(temp)

    # guess = input("重新输入") #如果只有这个是错误的，猜个数字3，重新输入4，、\\不会进入if里面
    # guess = int(input("重新输入")) #这个是可以的，，，，
    if guess == secret:              #m冒号的作用哦哦 哦哦
        print("xxxxx")
        print("bbbbbbbbb")      #缩进，，，，
    else:
        if guess < secret:
            print("too small")
        else:
            print("too big")

print("over")


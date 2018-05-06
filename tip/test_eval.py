#_*_conding:utf-8_*_
#!/bin/python

a = "[[1,2], [3,4], [5,6], [7,8], [9,0]]"
b = eval(a)


print(b)
print(type(b))


__import__('os').system('dir')

x = 1
y = 1
num1 = eval("x+y")
print("eva x+y = ", num1)


def g():
    x = 2
    y = 2
    num3 = eval("x+y")
    print(num3)
    num2 = eval("x+y", globals())
    #num2 = eval("x+y",globals(),locals())
    print('num2 = ', num2)
    print (locals()["x"])
    print (globals()["x"])

g()
#locals()对象的值不能修改，globals()对象的值可以修改
z=0
def f():    
    z = 1    
    print (locals())        
    locals()["z"] = 2    
    print (locals())      
f() 
globals()["z"] = 2
print (z)
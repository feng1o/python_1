# coding=utf8
''' 
    复数是由一个实数和一个虚数组合构成，表示为：x+yj 
    一个负数时一对有序浮点数(x,y)，其中x是实数部分，y是虚数部分。 
    Python语言中有关负数的概念： 
    1、虚数不能单独存在，它们总是和一个值为0.0的实数部分一起构成一个复数 
    2、复数由实数部分和虚数部分构成 
    3、表示虚数的语法：real+imagej 
    4、实数部分和虚数部分都是浮点数 
    5、虚数部分必须有后缀j或J 

    复数的内建属性： 
    复数对象拥有数据属性，分别为该复数的实部和虚部。 
    复数还拥有conjugate方法，调用它可以返回该复数的共轭复数对象。 
    复数属性：real(复数的实部)、imag(复数的虚部)、conjugate()（返回复数的共轭复数） 
    '''
class Complex(object):
    '''''创建一个静态属性用来记录类版本号'''
    version = 1.0
    '''''创建个复数类，用于操作和初始化复数'''

    def __init__(self, rel=15, img=15j):
        self.realPart = rel
        self.imagPart = img

     # 创建复数
    def creatComplex(self):
        return self.realPart + self.imagPart
      # 获取输入数字部分的虚部

    def getImg(self):
        # 把虚部转换成字符串
        img = str(self.imagPart)
        print(img)
        # 对字符串进行切片操作获取数字部分
        img = img[:-1]
        return float(img)

def test():
    print ("run test...........")
    com = Complex()
    Cplex = com.creatComplex()
    if Cplex.imag == com.getImg():
        print (com.getImg())
    else:
        pass
    if Cplex.real == com.realPart:
        print (com.realPart)
    else:
        pass
        # 原复数
    print ("the religion complex is :", Cplex)
        # 求取共轭复数
    print ("the conjugate complex is :", Cplex.conjugate())

if __name__ == "__main__":
    test()

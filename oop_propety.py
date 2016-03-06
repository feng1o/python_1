# _*_coding:utf-8_*_
# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143186781871161bc8d6497004764b398401a401d4cce000
# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：
# 比如加入判定

print("\n@property")


class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):  # 此方法判定比较麻烦
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
st1 = Student()
st1.set_score(80)
# 不能st1.score = 20
# st1.set_score(800)  # 报错


class Student2(object):

    # __slots__ = ('name', 'age', 'cla')

    @property
    def name(self):
        return self._name  # 必须有_

    @name.setter
    def name(self, names):
        if not isinstance(names, str):
            raise ValueError('type eeror')
        self._name = names   # 必须有_

st2 = Student2()
st2.name = "lf"  # OK，实际转化为s.set_score(60)
print('st2.name = %s' % st2.name)


class Student(object):

    @property
    def birth(self):
        return self._birth  # birth是可读写属性，

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth 
# 而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。


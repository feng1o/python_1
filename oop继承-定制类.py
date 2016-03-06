# _*_ coding:utf-8 _*_


class animal(object):
    def lives(self):
    	print("has alives")


class dog(animal):
    pass


class fish(object):
    def swiming(self):
    	print("swinming")


class person(animal, fish):
    pass
per1 = person()
per1.swiming()
per1.lives()
# _*_ coding:utf-8 _*_


class magicMethoClass(object):
	def __init__(self, name):
		self.name = name

	def __str__(self):
		#print("name = ", self.name)
		return self

mmc = magicMethoClass("lf")
print(mmc.__str__)
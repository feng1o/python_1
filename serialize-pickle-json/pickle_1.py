#!/bin/python3 
#_*_coding:utf-8 _*_

try:
	import cPickle as pickle
except ImportError:
	import pickle

d1 = dict(name = 'lf', age = 20)
d2 = set(['a', 20, 1, 2]);
print(pickle.dumps(d1))
print(pickle.loads(pickle.dumps(d1)))

with open("data.txt", 'ab+') as f:
	pickle.dump(d1, f)
	pickle.dump(d2, f)
	while True:
		try:
			dd = pickle.load(f)
			print("xx", dd)
		except EOFError:
			print("ok")
			break
		print(dd)

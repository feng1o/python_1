#!/usr/bin/env python
# _*_ coding:utf-8 _*_


try: 
	import simplejson as json
	print('ok..')
except  ImportError  : 
	print("import json...")
	import json

js = json.loads('{"姓名": "lf", "age": 23}', encoding='GB2312')
print(json.dumps(js))

print("what--", json.dumps(js, ensure_ascii=False))

print("json age=%d" % js['age'])


dataJsonStr1 = '{"x" : ["lf", 2, "男"]}'

#dataJsonStr = dataJsonStr1.decode("GB2312")
js2 = json.loads(dataJsonStr1)
print(json.dumps(js2))
print("xx....", json.dumps(js2, ensure_ascii=False))
print(js2['x'])
print(js2['x'][2])

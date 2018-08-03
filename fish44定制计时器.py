# _*_ encoding:utf-8 _*_

import time as t


class Mytimer():

    def __init__(self):
                # self.unit = ['年', '月', 'day', 'hour', 'minit', 'second']
        self.prompt = "未开始"
        self.last = []
        self.begin = 0
        self.end = 0

    def __str__(self):
        return self.prompt
    __repr__ = __str__

    def start(self):
        self.begin = t.localtime()
        print('计时开始')

    def stop(self):
        if not self.begin:
            print("tip: not started!")
        else:
       		self.end = t.localtime()
        	print("stop")

    def _calc(self):
        self.last = []  # liebiaoli
        self.prompt = "总共运行"
        for index in range(5):
            self.last.append(self.end[index] - self.begin[index])
            self.prompt += (str(self.last[index]) + self.unit[index])

        print(self.prompt)

mtime = Mytimer()
mtime.start()
mtime.stop()
mtime.stop()

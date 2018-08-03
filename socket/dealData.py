###########################################################################
# Concurrent server>  dealdata.py                                         #
# author: lf                                                              #
# time: 2016-07-10                                                        #
#                                                                         #
###########################################################################

from time import ctime
import os
import errno


HEADLEN = 4


class recvHeadLen(object):
    """docstring for  recvHeadLen"""

    def __init__(self, len):
        super(recvHeadLen, self).__init__()
        self.len = len

    def getHeadLen(self):
        print("....")


cur_path = os.path.abspath('.')


class tsf_picFile(object):
    """docstring for tsf_picFlie"""

    def __init__(self, path, fname, mode, content):
        super(tsf_picFlie, self).__init__()
        self.path = path
        self.fname = fname
        self.mode = mode
        self.content = content

    def ow_pic(self):
        with open(self.path + self.fname, self.mode) as openflie:
            openflie.write(self.content)
            print("write file over~!")
        openflie.close()

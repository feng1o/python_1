###########################################################################
# Concurrent server>  dealdata.py                                         #
# author: lf                                                              #
# time: 2016-07-10                                                        #
#                                                                         #
###########################################################################

from time import ctime
import datetime
import os
import errno
import struct


HEADLEN = 4
class  recvHeadLen(object):
	"""docstring for  recvHeadLen"""
	def __init__(self, len):
		super( recvHeadLen, self).__init__()
		self.len = len
	def getHeadLen(self):
		print("....")


def rename(pic):
	r_time = str(datetime.datetime.now()).replace(' ', '_')
	r_time = r_time.replace(':','_')
	new_img_name = pic+'-'+r_time+'.jpg'
	return new_img_name

cur_path = os.path.abspath('.')

class tsf_picFile():
	"""docstring for tsf_picFlie"""
	def __init__(self, path,fname, mode, content):
#super(tsf_picFlie, self).__init__()
		self.path = path
		self.fname = fname
		self.mode = mode
		self.content = content
	def ow_pic(self):
		self.fname = rename('img')
#print("open file:%s \n mode =%s \n filecontent = %s" %(self.path + self.fname, self.mode, self.content))
		print("open file:%s \n mode =%s \n " %(self.path + self.fname, self.mode))
		if not os.path.isdir(self.path + "/pic"):
			print("pic dir isnot  exit...")
			os.mkdir(self.path+"/pic")
		else:
			print("pic dir is exit...")
		with open(self.path+"/pic/"+self.fname, self.mode) as openflie:
			openflie.write(self.content)
			print("write file over~!")
		openflie.close()

if __name__=='__main__':
	print("....")
	print("....%s" % rename('img'))

	cur_path = os.path.abspath('.')
	# global pic_nu 
	rdpic = tsf_picFile(cur_path,'' , 'w+','picBody')
	rdpic.ow_pic()
	tsf_picFile.ow_pic(rdpic)

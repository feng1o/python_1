#!/usr/bin/python
# Filename: pickling.py

import pickle

# the name of the file where we will store the object
shoplistfile = 'shoplist.data'
# the list of things to buy
shoplist = ['apple','mango','carrot']
shoplist1= ['name','age','sex']

# Write to the file
f = open(shoplistfile,'wb')
pickle.dump(shoplist, f) #dump the object to a file
pickle.dump(shoplist1,f)
f.close()

del shoplist # detroy the shoplist variable
del shoplist1

# Read back from the storage
with open(shoplistfile,'rb') as f:
	while True:
		try:
			storedlist  = pickle.load(f) # load the object from the file
		except EOFError:
			print("eof---")
			break
		print(storedlist)
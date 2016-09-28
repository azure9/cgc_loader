#!/usr/bin/python

import os 
import sys

obj_list = []
def Test1(rootDir): 
    list_dirs = os.walk(rootDir) 
    for root, dirs, files in list_dirs: 
        for f in files: 
		if ".o" == f[-2:]:
			obj_list.append(os.path.join(root,f))

Test1(sys.argv[1])
for f in obj_list:
	print f
	f = open(f,'rb+')
	f.seek(1,0)
	f.write('ELF')
	f.close()

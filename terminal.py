#!/usr/bin/python2
import os
cmnd=1
import time
while(cmnd!='exit'):
	os.system("clear")
	print('\x1b[6;30;42m' + '\t\tSaurabh Londhe' + '\x1b[0m')
	os.system("pwd")
	cmnd=raw_input()
	os.system(cmnd)
	time.sleep(1)

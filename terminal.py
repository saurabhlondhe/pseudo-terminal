#!/usr/bin/python2
import os
cmnd=1
a=1
import time
while(cmnd!='exit'):
	os.system("clear")
	print('\x1b[6;30;42m' + '\t\tSaurabh Londhe' + '\x1b[0m')
	os.system("pwd")
	cmnd=raw_input()
	if cmnd=="time":
		a=int(input("Enter time to wait= "))
	elif cmnd=="help":
		print ("time\n\tto change the reset time \n\t\tEnter time in seconds")
		time.sleep(3)
	else:
		os.system(cmnd)
		time.sleep(a)

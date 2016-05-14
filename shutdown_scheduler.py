#simple script to shutdown linux system based on time 

import os
import time

TIME = raw_input("Enter your time in minutes to shutdown :")

TIME = int(TIME)

def shutdownner(TIME):
	SECONDS = TIME * 60
	time.sleep(float(SECONDS))
	os.system("sudo shutdown now -h")

shutdownner(TIME)


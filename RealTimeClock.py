import os #clear screen functioning
import time

#variables display time length

seconds = float(0) #want to display decimals of each second 
minutes = int(0) #want min to be dislayed as whole numbers
hours = int(0) #want hours to be displayed as whole numbers

run = input("Press x to run the program. ")

while run.lower() == "x":
	if seconds > 59:
		seconds = 0
		minutes = minutes+1 #when counter hits 60 seconds, counter resets to 0 and adds a minutes
	
	if minutes > 59:
		minutes = 0
		hours = hours+1 #when counter hits 60 minutes, counter resets to 0 and adds 1 hour
		
	os.system('cls') #clears the command prompt, will just show current time
	seconds = (seconds + .1)
	
	print(hours, ":" , minutes, ":", seconds)
	time.sleep(.1) 
	#will suspend execution for approximately .1 seconds	
	#provides an accurate representation of real time
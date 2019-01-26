import time
import webbrowser

num_breaks = 3
breaks_count = 0

print("This program began on " +time.ctime())
while breaks_count < num_breaks:
	time.sleep(10)
	webbrowser.open( "https://www.youtube.com/watch?v=cf3lgs_fFnM")
	breaks_count = breaks_count+1
	
#About every 10 seconds, the counter automatically makes 
#the user "Take a break" and redirects to the given youtube link

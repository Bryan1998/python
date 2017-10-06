import time
import random

while(not time.sleep(0.25)):
	n = str(random.randint(30,38))
	print("\033[1;",n,";40m************************",sep='')
	print("\033[1;",n,";40m**** /\  /\  /\  /\ ****",sep='')
	print("\033[1;",n,";40m****/  \/  \/  \/  \****",sep='')
	print("\033[1;",n,";40m************************",sep='')

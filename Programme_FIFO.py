import os
from MPUnixAsLib import *
from IPython import display
import time

pid = os.fork()
if pid > 0:
	try:
		serverInterface()
	except KeyboardInterrupt:
		display.clear_output()
		print("\nArret du programme ...\n")
else:
	time.sleep(0.5)
	try:
		clientInterfaceInit()
	except KeyboardInterrupt:
		display.clear_output()
		print("\nArret du programme ...\n")

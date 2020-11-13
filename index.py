#!/usr/bin/python3
import time
from pprint import pprint
from ring_doorbell import Ring, Auth
from oauthlib.oauth2 import MissingTokenError
import getpass
import auth
import json
import analyze
import os
import datetime
def main():
	myAuthObj = auth.createAuthObj()
	ring = None
	if myAuthObj is not None:
		print('[' + str(datetime.datetime.now()) + '] ' + 'Successful Login')
		ring = Ring(myAuthObj)
	else:
		print('[' + str(datetime.datetime.now()) + '] ' + 'Unable to establish connection. Check messages above.')
		return 0

	ring.update_data()
	devices = ring.devices()

	frontDoorCam = devices['doorbots'][0]
	frontDoorCam.recording_download(frontDoorCam.history(limit=5)[0]['id']
		, filename='last_event.mp4', override=True)

	if analyze.analyze(frontDoorCam.history(limit=15)[0]['id']) is not None:
		print('[' + str(datetime.datetime.now()) + '] ' + 'Successfully updated conf with new id')
		os.system('rm last_event.mp4')

	# while True:

		



	# 	time.sleep(3)


if __name__ == main():
	main()



# Requirements before publishing:
# - Change sleep time from 3 to 300. 3 is only for testing.
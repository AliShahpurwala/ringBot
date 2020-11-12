#!/usr/bin/python3
import time
from pprint import pprint
from ring_doorbell import Ring, Auth
from oauthlib.oauth2 import MissingTokenError
import getpass
import auth
import json

def main():
	myAuthObj = auth.createAuthObj()
	ring = None
	if myAuthObj is not None:
		print('Successful Login')
		ring = Ring(myAuthObj)
	else:
		print('Unable to establish connection. Check messages above.')
		return 0

	ring.update_data()
	devices = ring.devices()

	frontDoorCam = devices['doorbots'][0]
	for event in frontDoorCam.history(limit=15):
		print('ID:       %s' % event['id'])
		print('When:     %s' % event['created_at'])

	# while True:

		



	# 	time.sleep(3)


if __name__ == main():
	main()



# Requirements before publishing:
# - Change sleep time from 3 to 300. 3 is only for testing.
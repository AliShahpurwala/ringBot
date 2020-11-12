#!/usr/bin/python3
import time
from pprint import pprint
from ring_doorbell import Ring, Auth
from oauthlib.oauth2 import MissingTokenError
import getpass


def main():
	while True:
		
		time.sleep(3)


# if __name__ == main():
# 	main()



# Requirements before publishing:
# - Change sleep time from 3 to 300. 3 is only for testing.
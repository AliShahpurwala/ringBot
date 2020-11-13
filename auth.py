#!/usr/bin/python3

from ring_doorbell import Ring, Auth
from oauthlib.oauth2 import MissingTokenError, AccessDeniedError
import getpass
import requests
from requests import ConnectionError
import datetime
USERNAME = "ali.murtaza.am@gmail.com"

def call2FA():
	code = input("2FA code: ")
	return code


def createAuthObj():
	try:
		requests.get('https://docs.python.org/3/')
	except ConnectionError:
		print('[' + str(datetime.datetime.now()) + '] ' + 'Connection Error Occurred. Check your internet status.')
		return None
	password = getpass.getpass("Password: ")
	auth = Auth("Project01")
	try:
		auth.fetch_token(USERNAME, password)
	except MissingTokenError:
		try:
			auth.fetch_token(USERNAME, password, call2FA())
		except:
			print('[' + str(datetime.datetime.now()) + '] ' + 'Incorrect or expired 2FA code')
			return None
	except AccessDeniedError:
		print('[' + str(datetime.datetime.now()) + '] ' + "Incorrect Password")
		return None
	return auth


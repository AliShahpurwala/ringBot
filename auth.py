#!/usr/bin/python3

from ring_doorbell import Ring, Auth
from oauthlib.oauth2 import MissingTokenError, AccessDeniedError
import getpass

USERNAME = "ali.murtaza.am@gmail.com"

def call2FA():
	code = input("2FA code: ")
	return code


def createAuthObj():
	password = getpass.getpass("Password: ")
	auth = Auth("Project01")
	try:
		auth.fetch_token(USERNAME, password)
	except MissingTokenError:
		auth.fetch_token(USERNAME, password, call2FA())
	except AccessDeniedError:
		return None
	return auth


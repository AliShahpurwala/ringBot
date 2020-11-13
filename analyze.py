#!/usr/bin/python3
import cv2
import json
import os
def runAnalyzeCheck(lastEventId):
	""" This function will basically check whether a new event has occurred or not"""
	""" false -> No new event      true -> New event found"""
	with open('conf.json', 'r') as confFile:
		confJson = confFile.read()
	conf = json.loads(confJson)
	if (conf['lastVideoIdAnalyzed'] == lastEventId):
		confFile.close()
		return False
	else:
		confFile.close()
		return True

def analyze(lastEventId):
	with open('conf.json', 'r') as confFile:
		confJson = confFile.read()
	conf = json.loads(confJson)
	if (runAnalyzeCheck(lastEventId)):
		conf['lastVideoIdAnalyzed'] = lastEventId
		with open('conf.json', 'w') as outFile:
			json.dump(conf, outFile)
		return True
	else:
		os.system('rm last_event.mp4')
		return None

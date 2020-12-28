#!/usr/bin/python3
import cv2
import json
import os
import datetime
import copy
import pprint

frameScanTemplate = {
	"frameNumber": -1,
	"facesFoundNum": -1,
	"facesFound": []
}


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
		detectedFaceFrames = createAnalyzeFrames()
		detectedFaceFrames = sortFramesByDetectedFaces(detectedFaceFrames)
		print(detectedFaceFrames)
		conf['lastVideoIdAnalyzed'] = lastEventId
		with open('conf.json', 'w') as outFile:
			json.dump(conf, outFile)
		os.system('rm frame*')
		os.system('rm last_event.mp4')
		return True
	else:
		os.system('rm last_event.mp4')
		return None


def createAnalyzeFrames():
	vidcap = cv2.VideoCapture('last_event.mp4')
	count = 0
	success, image = vidcap.read()

	while success and count < 100:
		cv2.imwrite("frame%d.jpg" % count, image)
		success, image = vidcap.read()
		print('[' + str(datetime.datetime.now()) + '] Saved frame ' + str(count) + ': ' + str(success))
		count += 1

	result = []

	for i in range(0,100):
		test_img = cv2.imread('./frame%d.jpg' % i)
		gray_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)
		face_haar_cascade = cv2.CascadeClassifier('./assets/haar_cascade.xml')
		faces = face_haar_cascade.detectMultiScale(test_img, scaleFactor=1.32, minNeighbors=5)
		print(f'Found {faces} in frame {i}')
		frameScanTemplate["frameNumber"] = i
		frameScanTemplate["facesFoundNum"] = len(faces)
		frameScanTemplate["facesFound"] = faces
		result.append(copy.deepcopy(frameScanTemplate))

	detectedFaceFrames = []

	for x in range(0, len(result)):
		if result[x]['facesFoundNum'] > 0:
			detectedFaceFrames.append(copy.deepcopy(result[x]))
	
	del(result)

	print('[' + str(datetime.datetime.now()) + '] Completed analysis of video. Sending for verification.')


	return detectedFaceFrames


def sortFramesByDetectedFaces(detectedFaceFrames):
    n = len(detectedFaceFrames) 
  
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
            if detectedFaceFrames[j]['facesFoundNum'] > detectedFaceFrames[j+1]['facesFoundNum'] : 
                detectedFaceFrames[j], detectedFaceFrames[j+1] = detectedFaceFrames[j+1], detectedFaceFrames[j]

    return detectedFaceFrames
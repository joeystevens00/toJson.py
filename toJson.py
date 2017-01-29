#!/usr/bin/python3
# AUTHOR: Joey Stevens
# Description: CLI tool to build json using easy syntax
# Example: echo "key=value | key2=value2 | key3=value3" | toJson.py
# {"key2": "value2", "key": "value", "key3": "value3"}

import json
import sys

class toJson:
	def __init__(self, data):
		self.data = data
	def getData(self):
		return self.data
	def buildData(self, moredata):
		self.data += moredata
	def getJson(self):
		return json.dumps(self.data)
	def parseData(self):
		keys = {}
		for i in self.data.split("|"):
			key=i.rpartition("=")[0].strip()
			value=i.rpartition("=")[2].strip()
			keys.update({key: value})
		self.data=keys


#Testing = toJson("One=1 | Two=2")
#print(Testing.parseData())
#print(Testing.getJson())
if __name__ == '__main__':
	X = toJson("")

	if not sys.stdin.isatty():
		try:
			for line in sys.stdin:
				X.buildData(line)
		except: 
			pass
	else:
		try:
			X.buildData(str(sys.argv[1]))
		except:
			print("Missing data")
	if X.getData():
		X.parseData()
		print(X.getJson())
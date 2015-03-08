#!/usr/bin/python
import sys
import api
from lxml import etree
from api import Data
from subprocess import call
import time
import subprocess
import urllib2
from bs4 import BeautifulSoup


def command(speech_object):
	previous_command = ""
	while(True):
		line = speech_object.readline()
		if(line.startswith("sentence1: ")):
			com = line[15:-6]
			if (previous_command == com):
				continue
			print com
			if (com == "DRAGON FIRE"):
				userin = Data([" "]," ")
				userin.say("Yes sir.")
				previous_command = com
			if (com == "WHAT IS YOUR NAME"):
				userin = Data([" "]," ")
				userin.say("My name is Dragon Fire.")
				previous_command = com
			if (com == "WHAT IS YOUR GENDER"):
                                userin = Data([" "]," ")
                                userin.say("I have a female voice but I don't have a gender identity. I'm a computer program sir.")
                                previous_command = com
        		if (com == "OPEN FILE MANAGER"):
				userin = Data(["pantheon-files"],"File Manager")
				userin.say("File Manager")
				userin.interact(0)
				previous_command = com
			if (com == "OPEN WEB BROWSER"):
				userin= Data(["sensible-browser"],"Web Browser")
				userin.say("Web Browser")
				userin.interact(0)
				previous_command = com
			if (com == "SHUT DOWN THE COMPUTER"):
                                userin= Data(["sudo","poweroff"],"Shutting down")
                                userin.say("Shutting down")
				userin.interact(3)
                                previous_command = com
			if (com.startswith("SEARCH FOR")):
				userin = Data(["sensible-browser","http://en.wikipedia.org/wiki/"+com[11:].lower()],com[11:])
				userin.interact(0)
				wikihtmlcontent = urllib2.urlopen("http://en.wikipedia.org/wiki/"+com[11:].lower().replace(" ","_")).read()
				parsed_html = BeautifulSoup(wikihtmlcontent)
				wikicontent = parsed_html.body.find("p").text
				wikicontent = "".join([i if ord(i) < 128 and i.isalnum() else ' ' for i in wikicontent])
				#wikicontent = "".join([i if i.isalnum() or i==' ' else '' for i in wikicontent])
				print wikicontent
				userin.say(wikicontent)
                                #userin.say(com[11:].lower())
                                previous_command = com
            
			
			

if __name__ == '__main__':
	try:
		command(sys.stdin)
	except KeyboardInterrupt:
		sys.exit(1)

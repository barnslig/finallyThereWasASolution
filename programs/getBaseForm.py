#!/usr/bin/env python
# Copyright 2011 Leonard Techel, licensed under GPL v3
import sqlite3

database = "exceptions"
ends1 = [ "e", "s", "t" ]
ends2 = [ "ez", "es" ]
ends3 = [ "ons", "ent" ]
ends4 = [ "ssez" ]
ends5 = [ "ssons", "ssent" ]

erEnds = ["e", "es", "e", "ons", "ez", "ent"]
irEnds = ["s", "s", "t", "ssons", "ssez", "ssent"]
dreEnds = ["s", "s", ".", "ons", "ez", "ent"]

def makeEnd(possibleEnds, verb):	
	# delete empty entrys
	clean = [ ]
	for i in possibleEnds:
		if len(i) > 1:
			clean.append(i)
			
	# look for the suffix
	for suffixType in clean:
		
		# set the endigs directory
		endings = ""
		if suffixType == "er":
			endings = erEnds
		elif suffixType == "ir":
			endings = irEnds
		elif suffixType == "dre":
			endings = dreEnds
			
		# look for the end and delete it
		for suffix in endings:
				
			if verb[ len(verb)-len(suffix) : len(verb) ] == suffix:				
				# set the ending length
				if verb[len(verb)-len(suffix)-1 : len(verb)-len(suffix)] == suffixType[0:1]:
					suffixLength = len(suffix)+1
				else:
					suffixLength = len(suffix)
				
				cleanverb = verb[0:len(verb)-suffixLength]
				
		# print out the finished verb
		if len(clean) == 1:
			print("Solution: " + cleanverb + suffixType)
		else:
			print("Possible: " + cleanverb + suffixType)
	
def lookupEnd(verb):
	# delete ç
	verb = verb.replace("ç", "c")
	
	# small suffix
	end1 = verb[len(verb)-1:len(verb)]
	end2 = verb[len(verb)-2:len(verb)]
	end3 = verb[len(verb)-3:len(verb)]
	end4 = verb[len(verb)-4:len(verb)]
	end5 = verb[len(verb)-5:len(verb)]
	
	# set the end
	end = ""
	if end5 in ends5:
		end = end5
	elif end4 in ends4:
		end = end4
	elif end3 in ends3:
		end = end3
	elif end2 in ends2:
		end = end2
	elif end1 in ends1:
		end = end1
		
	# look for specific end
	sends = ""
	if end in erEnds:
		sends += "er|"
	if end in irEnds:
		sends += "ir|"
	if end in dreEnds:
		sends += "dre"	
		
	# try to get a specific
	pends = sends.split("|")
	makeEnd(pends, verb)
	
def getVerbFromDatabase(verb):
	cur.execute("SELECT infinitiv FROM exceptions WHERE conjugation ='{0}';".format(verb))
	row = cur.fetchone()
	try:
		print("Solution: {0}".format(row[0]))
	except TypeError:
		return False

if __name__ == "__main__":
	conn = sqlite3.connect(database)
	cur = conn.cursor()
	
	verb = input("Verb: ")
	print("--------------------")
	
	databaseTry = getVerbFromDatabase(verb)
	
	if databaseTry == False:
		lookupEnd(verb)
		
	print("--------------------")

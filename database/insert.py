#!/usr/bin/python3
# Copyright 2011 Leonard Techel, licensed under GPL v3
import sys
import sqlite3

def startInserting():
	for line in f:
		# ignore comments
		if line[0:1] != "#":
			# split
			splitted = line.split("|")
			try:
				# remove \n's
				strlen = len(splitted[2])
				if "\n" in splitted[2]:
					split = splitted[2][0:strlen-1]
				else:
					split = splitted[2]
					
				# database query
				cur.execute("INSERT INTO exceptions (infinitiv, person, conjugation) VALUES ('%s', '%i', '%s');" % (splitted[1], int(splitted[0]), split))
			except IndexError:
				pass
	conn.commit()
				
				
if __name__ == "__main__":
	# exception database connection
	conn = sqlite3.connect(sys.argv[2])
	cur = conn.cursor()
	
	# open file
	f = open(sys.argv[1], "r")
	
	# start
	startInserting()

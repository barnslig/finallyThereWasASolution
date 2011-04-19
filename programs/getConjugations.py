#!/usr/bin/python
# Copyright 2011 Leonard Techel, licensed under GPL v3
import sqlite3

# config
database = "exceptions"
erEnds = ["e", "es", "e", "ons", "ez", "ent"]
irEnds = ["s", "s", "t", "ssons", "ssez", "ssent"]
dreEnds = ["s", "s", "", "ons", "ez", "ent"]
urEnds = ["", "", "", "", "", ""]
vocals = ["a", "e", "i", "o", "u"]

# function for getting the type of the given verb
def getType(verb):
	# get only the ending
	startlen = len(verb)-3
	endlen = len(verb)
	ending = verb[startlen:endlen]
	
	# -er
	if "er" in ending[1:3]:
		endlen = endlen-2
		out = setEnds(verb, 0)
	# -ir
	elif "ir" in ending[1:3]:
		endlen = endlen-1
		out = setEnds(verb, 1)
	# -dre
	elif "dre" in ending[0:3]:
		endlen = endlen-2
		out = setEnds(verb, 2)
	# other
	else:
		out = setEnds(verb, 3)
		
	printOut(out)
		
# set the new ends and look for exceptions
def setEnds(infinitiv, typ):
	# er
	if typ == 0:
		# set the endings-list
		Endings = erEnds
		# get the verb without ending
		endlen = len(verb)-2
		onlyverb = infinitiv[0:endlen]
	# ir
	elif typ == 1:
		# set the endings-list
		Endings = irEnds
		# get the verb without ending
		endlen = len(verb)-1
		onlyverb = infinitiv[0:endlen]
	# dre
	elif typ == 2:
		# set the endings-list
		Endings = dreEnds
		# get the verb without ending
		endlen = len(verb)-2
		onlyverb = infinitiv[0:endlen]
	# unregular
	elif typ == 3:
		Endings = urEnds
		
	i = 0
	outlist = [ ]
	for end in Endings:
		# look for an exception
		cur.execute("SELECT conjugation FROM exceptions WHERE infinitiv ='" + infinitiv + "' AND person = " + str(i) + ";")
		row = cur.fetchone()
		# if there is one
		try:
			outlist.append(row[0])
		# no exception; regular verb
		except TypeError:
			# set the new end
			setExtension = False
			if onlyverb[len(onlyverb)-1:len(onlyverb)] == "g":
				if i == 3:
					setExtension = True
					Extension = onlyverb + "e"
			elif onlyverb[len(onlyverb)-1:len(onlyverb)] == "c":
				if i == 3:
					setExtension = True
					Extension = onlyverb[0:len(onlyverb)-1] + "ç"
					
			if setExtension == True:
				converb = Extension + end
			else:
				converb = onlyverb + end
				
			# set
			outlist.append(converb)
		i = i + 1
	
	# returns the verbs
	return outlist
	
# function for printing out the conjugated verbs
def printOut(verbs):
	# je
	if verbs[0][0:1] in vocals:
		print("J'" + verbs[0])
	else:
		print("Je	" + verbs[0])
	# tu
	print("Tu	" + verbs[1])
	# il
	print("Il	" + verbs[2])
	# nous
	print("Nous	" + verbs[3])
	# vous
	print("Vous	" + verbs[4])
	# ils
	print("Ils	" + verbs[5])

if __name__ == "__main__":
	# exception database connection
	conn = sqlite3.connect(database)
	cur = conn.cursor()
	
	# get the verb
	verb = input("Le verb: ")
	
	# get the type and start conjugation
	getType(verb)

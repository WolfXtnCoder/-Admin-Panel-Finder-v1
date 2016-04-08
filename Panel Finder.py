#!/usr/bin/env python

#  >>>>>>>>> Salam Alaykom <<<<<<<<<<
# Admin Panel Finder v1 Coded by Wolf XTN | W0lfxt12@gmail.com
# This My First Tool :D 
# Greetz to My Team fallaga team | https://www.facebook.com/wolf.xtn



from urllib2 import Request, urlopen, URLError, HTTPError
def Credit():
	Space(9); print "|||||||||||||||||||||||||||||||||||||||||"
	Space(9); print "|   ----| Admin Panel Finder v1  |---   |"
	Space(9); print "|         Author : Wolf XTN             |"
	Space(9); print "|       Tunisian Fallaga Team           |"
	Space(9); print "|     FB : Facebook.com/Wolf.xtn        |"
	Space(9); print "| Gr33TZ To : AnisXTN And Fallagah Team |"
	Space(9); print "|||||||||||||||||||||||||||||||||||||||||"

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("panels.txt","r");
	link = raw_input("Enter Site Name \n(ex : victim.com or www.victim.com ): ")
	print "\n\nAvilable links : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "OK => ",req_link
			

Credit()
findAdmin()

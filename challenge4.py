import urllib.request

nNothing = 12345

for i in range(300):
	response = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + str(nNothing))
	html = response.read()
	print(html)
	lastNothing = nNothing
	nNothing = ("".join([i for i in str(html) if (ord("0") <= ord(i) <= ord("9"))]))
	
	if not nNothing:
		nNothing = str(int(int(lastNothing) / 2))
		print(nNothing)
	
	elif int(nNothing) == 8268363579:
		nNothing = 63579
		print("ok :)")

#http://www.pythonchallenge.com/pc/def/peak.html
	

	

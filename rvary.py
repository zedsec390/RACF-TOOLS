from des import DesCrypt
import sys

h=["5AA70358A9C369E0","8038785CEDE74675"]

wlist=["123","QWERTY1","DOG","PASSWORD"]

for j in h:
	for i in wlist:
		d = DesCrypt(i,i)
		#d.DEBUG=True
		d.crypt()
		t=(d.getHexHash().upper())
		if t == j.upper():
			print("Found: " + i + ":" + t)
			break

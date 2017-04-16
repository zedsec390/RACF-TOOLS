from des import DesCrypt
import sys

# Demonstrates how RACF DES passwords are built and stored

u = "IBMUSER"
p3 = "2222"         

print("User: {0:s}  password: {1:s} ".format(u,p3))
d = DesCrypt(u,p3)
d.DEBUG=True
d.crypt()
print(u + ":" + d.getHexHash().upper())

from smartcard.System import readers

WRITE = [0x00, 0xD6]
STARTMSB = [0x00] 
STARTLSB = [0x00]
MEM_L = [0x01]


f=open("ID.txt",'r')
ID=int(f.read())
ID+=1
f.write(ID)
ID=hex(ID)
DATA=[ID]

cardservice.connection.connect()
apdu = READ + STARTMSB + STARTLSB + MEM_L + DATA
response1, sw1, sw2 = self.cardservice.connection.transmit( apdu )
print(response1)


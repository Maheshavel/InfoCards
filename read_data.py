from smartcard.System import readers
import os

SELECT = [0x00, 0xA4, 0x04, 0x00, 0x0A, 0xA0, 0x00, 0x00, 0x00, 0x62,
    0x03, 0x01, 0x0C, 0x06, 0x01]
COMMAND = [0x00, 0x00, 0x00, 0x00]

r = readers()
reader = r[0]

connection = reader.createConnection()
connection.connect()

data, sw1, sw2 = connection.transmit(SELECT)
print(data)

data, sw1, sw2 = connection.transmit(COMMAND)
print(data)

res=int(data,16)

mypath=os.getcwd()
mypath+='\res'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for files in onlyfiles:
    os.startfile(files)

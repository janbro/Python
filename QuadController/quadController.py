import serial
import io
import bluetooth
import sys

##bluetoothPort = serial.Serial()
##bluetoothPort.baudrate =
bd_addr = "f0:72:8c:7a:f4:7b" #itade address

port = 13
sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))
print 'Connected'
sock.settimeout(1.0)
sock.send("a")
print 'Sent data'

data = sock.recv(1)
print 'received [%s]'%data
while True:
    print sock.recv(1)
sock.close()

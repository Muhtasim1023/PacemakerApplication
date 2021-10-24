import serial
import serial.tools.list_ports



myports = serial.tools.list_ports.comports()

print()

for i in myports:

    print(i.vid)

# print(myports)

print()
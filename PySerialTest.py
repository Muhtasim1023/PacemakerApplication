import serial

import serial.tools.list_ports


def serialConnect():
    notConnected = True
    global pacemaker_serial, hardwareConnected
    port = ["COM1","COM2","COM3","COM4","COM5","COM6","COM7","COM8"] ## set correct COM port!
    i = len(port)
    while notConnected:
        i -= 1
        try:
            pacemaker_serial = serial.Serial(port=port[i], baudrate=115200,timeout=1)
            print(pacemaker_serial)
            notConnected = False
        except:
            notConnected = True
            print(port[i] + " failed")
        if (notConnected == False): 
            hardwareConnected = True
            print(port[i] + " connected")
            pacemaker_serial.flush()
            break

# serialConnect()


myports = serial.tools.list_ports.comports()
print()
for i in myports:
    print(i.description)
# print(myports)
print()

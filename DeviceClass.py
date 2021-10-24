import win32com.client
import json

class Device:
    Name = ""
    Id = ""

    def __init__(self, Name, Id):
        self.Name = Name
        self.Id = Id

    def Set_Name(self, Name):
        self.Name = Name
    
    def Set_Id(self, Id):
        self.Id = Id

    def Get_Device_From_Json_By_Id(self):
        All_Devices = Devices()
        for i in All_Devices.Get_Devices_From_Json():
            if self.Id == i["Id"]:
                self.Name = i["Name"]

    def Save_Device_To_Json(self):
        All_Devices = Devices()
        saved_devices = All_Devices.Get_Devices_From_Json()
        saved_devices.append({"Name": self.Name, "Id": self.Id})
        with open('UserDevices.json', 'w') as w:
            json.dump({"Devices": saved_devices}, w, indent = 2)
            w.close()
        print("New pacemaker saved")

class Devices:
    wmi = None
    DeviceIdList = []

    def __init__(self):
        self.DeviceIdList = []
        self.wmi = win32com.client.GetObject ("winmgmts:")
        for usb in self.wmi.InstancesOf ("Win32_USBHub"):
            if usb.Name == "J-Link driver":# and usb.DeviceID not in self.DeviceIdList:
                self.DeviceIdList.append(usb.DeviceID) # Only add Pacemaker devices
        
    def Get_All_Device_Ids(self):
        return self.DeviceIdList

    def Get_Devices_From_Json(self):
        retLst = []
        with open('UserDevices.json', 'r') as r:
            data = json.loads(r.read())
            for i in data["Devices"]:
                retLst.append(i)
            r.close()
        return retLst

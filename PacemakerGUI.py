from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.config import Config
Config.set('graphics','resizable', False)

from DeviceClass import Devices, Device

import json


class Parameter:
    # Code = None
    Id = None
    Name = None
    Label = None
    Values = None
    Value = None
    # Int_Value = None
    # Min = None
    # Max = None
    # Increment = None
    Unit = None
    UI_Type = None
    Priority = None

    def __init__(self, Id, Name, Label, Values, Value, Unit, UI_Type, Priority):
        # , Values, Value, Int_Value, Min, Max, Increment, Units, UI_Type):
        self.Id = Id
        self.Name = Name
        self.Label = Label
        self.Values = Values
        self.Value = Value
        self.Unit = Unit
        self.UI_Type = UI_Type
        self.Priority = Priority

    def Set_Value(self, val):
        if  val == "-" or val in self.Values:
            self.Value = val
            print("{label} set to {value}".format(label = self.Label, value = val))
            with open('SelectedParameters.json', 'w') as w:
                dump_lst = []
                for i in Param_Lst:
                    dump_lst.append({"Id": i.Id, "Name": i.Name, "Label": i.Label, "Value": i.Value})
                json.dump({"SelectedParameters": dump_lst}, w, indent = 2)
            w.close()
            return True
        else:
            print("Uable to set {label} to {value}".format(label = self.Label, value = val))
            return False



Param_Lst = [] # Holds all parameter objects read from JSON file
# Read JSON file for parameter data (use DB later?)
with open('Parameters.json', 'r') as myfile:
    data=json.loads(myfile.read())
    for i in data["Parameters"]:
        Param_Lst.append(Parameter(**i))
    Param_Lst.sort(key=lambda x: x.Priority)
    myfile.close()







# Define our different screens
class CreateNewAccountWindow(Screen):
    pass

class LoginWindow(Screen):
    pass

class MainWindow(Screen):
    def Get_Params(self):
        return Param_Lst
    def Get_Param_Label(self, id):
        if Param_Lst[id].Unit == "":
            return Param_Lst[id].Label
        else:
            return Param_Lst[id].Label + " (" + Param_Lst[id].Unit + ")"
    def Get_Param_Value(self, id):
        return Param_Lst[id].Value
    def Get_Param_Values(self, id):
        return Param_Lst[id].Values
    def Set_Param_Value(self, id, value):
        Param_Lst[id].Set_Value(value)
    def Clear_Params(self, spinners):
        for i in Param_Lst:
            i.Set_Value("-")
            spinners[i.Id].text = "-"
    pass

class WindowManager(ScreenManager):
    pass

# Welcome page Screen
class MainApp(MDApp):
    
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        Window.size = (1080,720)
        Window.minimum_width = 1080
        Window.minimum_height = 720
        return Builder.load_file("GUIlogin.kv")

    def loginUser(self):
        
        username = self.root.ids.loginWindow.user.text 
        password = self.root.ids.loginWindow.password.text

        try:
            with open('UserInfo.json', 'r') as r:
                data = json.loads(r.read())
                for i in data["UserInfo"]:
                    if i["Username"] == username and i["Password"] == password:
                        self.root.ids.mainWindow.user_label.text = "User: " + i["Name"]
                        self.root.ids.loginWindow.user.text = ""
                        self.root.ids.loginWindow.password.text = ""
                        return "MainWindow"
        except:
            return "LoginWindow"

        

    def logNewUser(self):

        name = self.root.ids.newUser._name.text 
        username = self.root.ids.newUser._user.text 
        password = self.root.ids.newUser._pass.text

        database = []
        newUser = {"Username": username, "Name": name, "Password": password}

        try:
            with open('UserInfo.json', 'r') as r:
                data = json.loads(r.read())
                for i in data["UserInfo"]:
                    database.append(i)
                r.close()
        except:
            pass

        with open('UserInfo.json', 'w') as w:
            if len(database) < 10:
                if not newUser in database:
                    database.append(newUser)
                    self.root.ids.newUser._name.text = "" 
                    self.root.ids.newUser._user.text = ""
                    self.root.ids.newUser._pass.text = ""
                    print("New user added.")
                    json.dump({"UserInfo": database}, w, indent = 2)
                    return "LoginWindow"
                else:
                    print("User already exists.")     
            else:
                #POP UP
                print("Too Many Users FOP!")   
            json.dump({"UserInfo": database}, w, indent = 2)
            return "CreateNewAccountWindow"

    def Connect_To_Device(self):
        All_Devices = Devices()
        if len(All_Devices.Get_All_Device_Ids()) == 0:
            # TO-DO -> Error Message
            self.root.ids.mainWindow.deviceName.text = "No Pacemaker Devices Connected!"
            print("No Pacemaker Devices Connected")
        elif len(All_Devices.Get_All_Device_Ids()) == 1:
            # TO-DO -> Connected Message
            Current_Device = Device("", All_Devices.DeviceIdList[0])
            Current_Device.Get_Device_From_Json_By_Id()
            if Current_Device.Name != "" and Current_Device.Id != "":
                self.root.ids.mainWindow.deviceName.text = Current_Device.Name
                print("Pacemaker recognized")
                print(Current_Device.Name)
                print(Current_Device.Id)
                # TO-DO -> Set this as main pacemaker (connect it)
            else:
                print("Pacemaker unrecognized")
                newName = input(print("Enter New Pacemaker Name:"))
                Current_Device.Name = newName
                Current_Device.Id = All_Devices.DeviceIdList[0]
                Current_Device.Save_Device_To_Json()
                # TO-DO -> Set this as main pacemaker (connect it)
                self.root.ids.mainWindow.deviceName.text = Current_Device.Name
        else:
            # TO-DO -> UI To Pick Which Pacemaker
            # Decide what happens depending on recognizability of Pacemaker's
            print("Multiple pacemakers found, pick the one you would like to use")
            for i in All_Devices.Get_All_Device_Ids():
                print(i)



if __name__ == '__main__':
    MainApp().run()
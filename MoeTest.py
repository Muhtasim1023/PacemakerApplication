from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

import json

from DeviceClass import Devices, Device

# Define our different screens
class CreateNewAccountWindow(Screen):
    pass

class LoginWindow(Screen):
    pass

class MainWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass


# Welcome page Screen
class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        return Builder.load_file("MoeTest.kv")

    def deviceName(self):
        # implement device checking function in here
        print("Device Set")
        self.root.ids.mainWindow.deviceName.text = "Cam's Pacemaker"
        ###############################################

    def loginUser(self):
        
        username = self.root.ids.login.user.text 
        password = self.root.ids.login.password.text

        with open('UserInfo.json', 'r') as r:
            data = json.loads(r.read())
            for i in data["UserInfo"]:
                if i["Username"] == username and i["Password"] == password:
                    self.root.ids.mainWindow.username.text = i["Name"]
                    self.root.ids.login.user.text = ""
                    self.root.ids.login.password.text = ""
                    r.close()
                    return "MainWindow"
            r.close()
        return "LoginWindow"
        

    def logNewUser(self):

        name = self.root.ids.newUser._name.text 
        username = self.root.ids.newUser._user.text 
        password = self.root.ids.newUser._pass.text

        database = []
        newUser = {"Username": username, "Name": name, "Password": password}

        with open('UserInfo.json', 'r') as r:
            data = json.loads(r.read())
            for i in data["UserInfo"]:
                database.append(i)
            r.close()

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
            print("No Pacemaker Devices Connected")
        elif len(All_Devices.Get_All_Device_Ids()) == 1:
            # TO-DO -> Connected Message
            Current_Device = Device("", All_Devices.DeviceIdList[0])
            Current_Device.Get_Device_From_Json_By_Id()
            if Current_Device.Name != "" and Current_Device.Id != "":
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
        else:
            # TO-DO -> UI To Pick Which Pacemaker
            # Decide what happens depending on recognizability of Pacemaker's
            print("Multiple pacemakers found, pick the one you would like to use")
            for i in All_Devices.Get_All_Device_Ids():
                print(i)

            



if __name__ == '__main__':
    MainApp().run()
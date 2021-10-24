from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

import json

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
        return Builder.load_file("GUIlogin.kv")

    def loginUser(self):
        
        username = self.root.ids.loginWindow.user.text 
        password = self.root.ids.loginWindow.password.text

        with open('UserInfo.json', 'r') as r:
            data = json.loads(r.read())
            for i in data["UserInfo"]:
                if i["Username"] == username and i["Password"] == password:
                    self.root.ids.mainWindow.user_label.text = i["Name"]
                    self.root.ids.loginWindow.user.text = ""
                    self.root.ids.loginWindow.password.text = ""
                    return "MainWindow"

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


if __name__ == '__main__':
    MainApp().run()
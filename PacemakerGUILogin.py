from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

import json

sm = ScreenManager()

# Define our different screens
class CreateNewAccountWindow(Screen):
    pass

class LoginWindow(Screen):
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
        
        username = self.root.ids.login.user.text 
        password = self.root.ids.login.password.text

        # Search Username and PassWord in savedUser.txt
        print("Username: ", username)
        print("Password: ", password)

    def logNewUser(self):
        name = self.root.ids.newUser._name.text 
        username = self.root.ids.newUser._user.text 
        password = self.root.ids.newUser._pass.text 
        data = {"Name: ": name, "Username: ": username, "Password: ": password }

        with open('savedUser.txt', 'w') as f:
            json.dump(data, f)


if __name__ == '__main__':
    MainApp().run()
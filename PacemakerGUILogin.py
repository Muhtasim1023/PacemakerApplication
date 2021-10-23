from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


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

    def logData(self):
        username = self.root.ids.user.text 
        password = self.root.ids.password.text

        print("Username: ", username)
        print("Password: ", password)

if __name__ == '__main__':
    MainApp().run()
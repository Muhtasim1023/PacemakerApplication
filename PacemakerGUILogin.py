from kivymd.app import MDApp
from kivy.lang import Builder


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
    
    def createnewUser(self):
        pass
MainApp().run()
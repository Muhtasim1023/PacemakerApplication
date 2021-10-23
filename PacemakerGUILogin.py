from kivymd.app import MDApp
from kivy.lang import Builder


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Pink"
        return Builder.load_file("GUIlogin.kv")
    def logger(self):
        self.root.ids.welcome_label.text = f"Sup {self.root.ids.user.text}!"
    
    def clear(self):
        self.root.ids.welcome_label.text = f"PACEMAKER GUI"
        self.root.ids.user.text = ""
        self.root.ids.user.password.text = ""

MainApp().run()
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp
import json

sm = ScreenManager()

class Parameter:
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
        self.Id = Id
        self.Name = Name
        self.Label = Label
        self.Values = Values
        self.Value = Value
        self.Unit = Unit
        self.UI_Type = UI_Type
        self.Priority = Priority

    def Set_Value(self, val):
        if val in self.Values:
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

Builder.load_file("Kivy.kv")

# Main Section
class MainWindow(Screen):
    def Get_Params(self):
        return Param_Lst
    def Get_Param_Label(self, id):
        return Param_Lst[id].Label + " (" + Param_Lst[id].Unit + ")"
    def Get_Param_Value(self, id):
        return Param_Lst[id].Value
    def Get_Param_Values(self, id):
        return Param_Lst[id].Values
    def Set_Param_Value(self, id, value):
        Param_Lst[id].Set_Value(value)
    pass

# Welcome page Screen
class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"

        # ParamUI = ParameterUI()
        # for i in range(5):
        #     ParamUI.ParameterUI.add_widget(Label(text="HI"))



        return MainWindow()

if __name__ == '__main__':
    MainApp().run()

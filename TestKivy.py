from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp

import json

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

    def Set_Value(self, spinner, val):
        print(spinner)
        if val in self.Values:
            self.Value = val
            print("{label} set to {value}".format(label = self.Label, value = val))
            All_Parameters.Get_All_Parameters()
            return True
        else:
            print("Uable to set {label} to {value}".format(label = self.Label, value = val))
            All_Parameters.Get_All_Parameters()
            return False
        

class Parameters:
    Parameters = None

    def __init__(self, Parameters):
        self.Parameters = Parameters
    
    def Get_All_Parameters(self):
        print("\n")
        for i in self.Parameters:
            print("{label} = {value}".format(label = i.Label, value = i.Value))
        print("\n")
        

All_Parameters = None
Param_Lst = [] # Holds all parameter objects read from JSON file
# Read JSON file for parameter data (use DB later?)
with open('Parameters.json', 'r') as myfile:
    data=json.loads(myfile.read())
    for i in data["Parameters"]:
        Param_Lst.append(Parameter(**i))
    Param_Lst.sort(key=lambda x: x.Priority)
    All_Parameters = Parameters(Param_Lst)
    myfile.close()

All_Parameters.Get_All_Parameters()

layout = GridLayout(cols=2, spacing=10, size_hint_y=None)
# Make sure the height is such that there is something to scroll.
layout.bind(minimum_height=layout.setter('height'))
for i in Param_Lst:
    label = Label(text=i.Label + " (" + i.Unit + ")", size_hint_y=None, height=40, halign='left')
    label.bind(size=label.setter('text_size'))
    spinner = Spinner(text=i.Value, values=i.Values, size_hint=(None, None), size=(200, 40))
    spinner.bind(text=i.Set_Value)
    layout.add_widget(label)
    layout.add_widget(spinner)
root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
root.add_widget(layout)

runTouchApp(root)

All_Parameters.Get_All_Parameters()
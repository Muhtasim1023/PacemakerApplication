from enum import Enum
import json

class UI_Type(Enum):
    Range = 0
    Select = 0

class Pacemaker_Mode(Enum):
    VOO = 0
    VVI = 1
    AOO = 2
    AAI = 3
    # Add other modes

# print(Pacemaker_Mode.AAI.value)

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
        # if self.UI_Type == UI_Type.Select:
        print(val)
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
        # if self.UI_Type == UI_Type.Range:
        #     if self.Min <= val and val <= self.Max:
        #         self.Value = val
        #         return True
        #     else:
        #         return False

# test_param_string = '{"Name": "PMMode", "Label": "Pacemaker Mode"}'

# test_param_dict = json.loads(test_param_string)

# test_param = Parameter(**test_param_dict)

# print(test_param.Code)
# print(test_param.Label)

# print(19//20)



# lst = [30, 50, 90, 175] 
# Min = lst[0]
# Mac = lst[-1]
# inc = [5, 1, 5]

# val = 55

# for i in range(0, len(lst)):
#     if lst[i] <= val and val <= lst[i + 1]:
#         print(inc[i])


# allow_values = [0.05, 0.1, 0.2, 0.3, 1.9]
# a = ["VOO", "VVI", "AOO", "AAI"]

# b = [30]

# Values = ["30-50 (increments of 1)", "50-80 (increments of 5)", ""]
# minmax = [[30, 50], [50, 80]]
# step= [1, 5, 3]

Param_Lst = [] # Holds all parameter objects read from JSON file

# Read JSON file for parameter data (use DB later?)
with open('Parameters.json', 'r') as myfile:
    data=json.loads(myfile.read())
    for i in data["Parameters"]:
        Param_Lst.append(Parameter(**i))
    Param_Lst.sort(key=lambda x: x.Priority)
    myfile.close()

for i in Param_Lst:
    print(i.Id)
    print(i.Name)
    print(i.Label)
    print(i.Values)
    print(i.Value)
    print(i.Unit)
    print(i.UI_Type)
    print(i.Priority)
    print()

# Test setting parameter value
Param_Lst[0].Set_Value(50)
print(Param_Lst[0].Value)

# class UserInfo:
#     def __init__(self):


lst = []
with open('UserInfo.json', 'r') as r: 
    data = json.loads(r.read())
    for i in data["UserInfo"]:
        lst.append(i)
    r.close()

newUser = {"Username": "Cam","Name": "Jam","Password": "Ham"}

with open('UserInfo.json', 'w') as w:
    if not newUser in lst:
        lst.append(newUser)
        print("New user added.")
    else:
        print("User already exists.")        
    json.dump({"UserInfo": lst}, w, indent = 2)













    
    

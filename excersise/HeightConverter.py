import FreeSimpleGUI as sg
from Converter import convert
label_ft = sg.Text("Enter feet")
label_inch = sg.Text("Enter Inches")
label_Text = sg.Text("Result: ")
label_Result = sg.Text("",key="output")

ConvertBtn = sg.Button("Convert")

Input_Feet = sg.Input(key="feet")
Input_Inches = sg.Input(key="inches")




_layout = [[label_ft,Input_Feet],[label_inch,Input_Inches],[ConvertBtn],[label_Text,label_Result]]
window = sg.Window("Height Converter", layout=_layout)

while True:
    event, values = window.read()
    feet = float(values["feet"])

    inches = float(values["inches"])
    result =convert(feet,inches)
    window["output"].update(value=f"{result}")

window.close()




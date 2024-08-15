import functions2

import FreeSimpleGUI as sg

label = sg.Text("Type in a to -do")
input_box = sg.InputText(tooltip="Enter to do")
add_button = sg.Button("Add")
label2 = sg.Text("Hey")
window = sg.Window('MY-to-do App',layout=[[[label], input_box, add_button,label2]])
window.read()
window.close()
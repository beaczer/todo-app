import functions2

import FreeSimpleGUI as sg
import time

sg.theme("DarkPurple4")
clock = sg.Text('', key='clock')
list_box = sg.Listbox(values=functions2.get_todos()
                      , key='todos'
                      ,enable_events=True
                      ,size=[45,10])
edit_button = sg.Button("Edit")

label = sg.Text("Type in a to -do")
input_box = sg.InputText(tooltip="Enter to do", key="todo", text_color='green', font='Verdana')
add_button = sg.Button("Add")
complete_button= sg.Button("Complete")
exit_button =sg.Button("",key="Exit")
layout = [[clock],[[label]
              , input_box
              , add_button]
            ,[list_box,edit_button,complete_button]
          , [exit_button]]
window = sg.Window('MY-to-do App',
                   layout= layout,
                   font=('Helvetica',20))

while True:
    event, values = window.read(timeout=10)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(f"1- {event}-2 {values} --3{values['todos']}")

    match event:
        case "Add":
            todos = functions2.get_todos()
            new_todo = values['todo'] +"\n"

            todos.append(new_todo)
            functions2.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = functions2.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions2.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Select item")
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Complete':
            try:
                todo_to_complete =values['todos'][0]
                todos= functions2.get_todos()
                todos.remove(todo_to_complete)
                functions2.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(values="")
            except IndexError:
                sg.popup("Select item")
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            exit()
            break
print('BYe')



window.close()
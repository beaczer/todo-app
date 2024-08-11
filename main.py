
from functions2 import get_todos, write_todos
import time
now = time.strftime("%b %d, %Y %H:%M")


while True:
    user_action=input("type add or show, edit or exit: ")
    user_action= user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + "\n")

        write_todos(todos, "todos.txt")

    elif user_action.startswith("show"):

        todos= get_todos()


        for index,item in enumerate(todos):
            new_item= item.strip('\n')
            row = f"{index + 1} - {item}"
            print(row)


    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(row)

            number = number - 1

            todos   = get_todos()

            print('Here is todos existing',todos)

            new_todo=input("Enter new to do")
            todos[number] = new_todo + "\n"

            print('Here is how it will be', todos)

            write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number=int(user_action[9:])

            todos = get_todos()
            index = number = 1
            todo_to_removed = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)
            message = f"Todo {todo_to_removed} was remove from the list"
            index = number - 1
            todo_to_removed = todos[index]
            todos.pop(number-1)

            write_todos(todos)
            message = f"To do {todo_to_removed} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue
    elif 'exit' in user_action:
        break
    else:
        break


print('Bye')
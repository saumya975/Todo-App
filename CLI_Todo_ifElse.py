import todoFunctions
import time


current_time=time.strftime("%b %m,%y  %H:%M:%S")
print(f"It is {current_time}")
while True:
    user_action = input("add,show,edit,remove or exit: ")
    user_action=user_action.capitalize().strip()

    if 'Add' in user_action:
        todo=user_action[4:]
        todos=todoFunctions.get_todos()
        todos.append(todo+'\n')

        todoFunctions.write_todos(todos)

    elif 'Show' in user_action:
        with open('todos1.txt','r') as file:
            todos=file.readlines()

        for index,item in enumerate(todos):
            print(f"{index+1}- {item}",end="")

    elif 'Remove' in user_action:
        number=int(user_action[7:])
        todos=todoFunctions.get_todos()
        todos.pop(number-1)
        todoFunctions.write_todos( todos)


    elif 'Edit' in user_action:
        number=int(user_action[5:])
        todos=todoFunctions.get_todos()
        new_todo=input("Enter new todo: ")
        todos[number-1]=new_todo+'\n'
        todoFunctions.write_todos( todos)




    elif 'Exit' in user_action:
        break
    else:
        print("invalid choice")
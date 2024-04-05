def get_todos(filepath='todos1.txt'):
    with open(filepath, 'r') as file:
        todos_1 = file.readlines()

    return todos_1

def write_todos( todos_1,filepath='todos1.txt'):
    with open(filepath, 'w') as file:
        file.writelines(todos_1)
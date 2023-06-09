FILEPATH = "tasks.txt"

def get_todos(filepath=FILEPATH):
    """
    Read a text file and return the list of to-do items.
    :param filepath: text file
    :return: list of to-dos
    """
    with open(filepath, 'r') as local_file:
        todos_local = local_file.readlines()
        return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """
    Write the to-do items list in the text file
    :param todos_arg:
    :param filepath: text file
    :return:
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())
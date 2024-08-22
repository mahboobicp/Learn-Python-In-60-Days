FILEPATH = r"D:\Python\Learn-Python-In-60-Days\Files\todos.txt"
""" import time
now = time.strftime("%b %d, %Y %H : %M : %S")
print("***"*20)
print("It is ",now)
print("***"*20) """
def get_todo(path_local=FILEPATH): 
    """ This function open a file in read moode and then read the file 
    using readlines method and return a List which contain all the file contents """
    with open(path_local , 'r') as file:
        todo_local = file.readlines()
    return todo_local

def write_todos(todo_list, path_local=FILEPATH):
    """ This function take two arguments 
     1. A list which contain all the data which will be written to the file
     2. File path """
    with open(path_local , 'w') as file:
            file.writelines(todo_list)


""" #print(__name__)
if __name__ == "__main__":
     print("Main") """
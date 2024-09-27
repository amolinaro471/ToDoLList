import linkedList as LL


todolist = LL.linkedList()
print("Welcome to ToDoLList")

def menu_printer():
    output = "1: Add To List\n2: Remove From List\n3. Print List\n4: Save List\n5: Load Previous List\n6: Quit"
    print(output)

def inputChecker(input_num):
    x = input_num
    isDone = False
    if x == 1:
        print("Add To List")
        #The tasks are being parsed weird when printed out???
        title = input("Title: ")
        tasks = input("Tasks: ")
        todolist.add_to_list(title, tasks)
    elif x == 2:
        print("Remove Task")
        title = input("Title to Remove: ")
        #This doesnt remove anything even if the Title name is right?
        print(type(title))
        todolist.remove_from_list(title)
    elif x == 3:
        print("Printing To Do List...")
        print(todolist)
    elif x == 4:
        print("Save List")
        todolist.write_to_file("SavedList.txt")
    elif x == 5:
        print("Load Previous List")
        todolist.read_from_file("SavedList.txt")
    elif x == 6:
        print("Quitting...")
        isDone = True
    else:
        print("Not Valid Input. Please try again")   
    return isDone

def main():
    isDone = False
    x = 0
    while not isDone:
        menu_printer()
        x = int(input("Input: "))
        isDone = inputChecker(x)
    print("\nGoodbye!")

main()
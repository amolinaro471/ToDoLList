import linkedList as LL


todolist = LL.linkedList()
print("Welcome to ToDoLList")

def menu_printer():
    output = "1: Add To List\n2: Remove From List\n3. Print List\n4: Save List\n5: Load Previous List\n6: Quit"
    print(output)

def task_inputs():
    isDone = False
    task_list = []
    while not isDone:
        task = input("Task: ")
        if task == "":
            break
        else:
            task_list.append(task)
            done = int(input("Type 1 to be done inputting tasks: "))
            if done == 1:
                isDone = True
    return task_list

def inputChecker(input_num):
    x = input_num
    isDone = False
    if x == 1:
        title = input("Title: ")
        tasks = task_inputs()
        todolist.add_to_list(title, tasks)
    elif x == 2:
        title = input("Title to Remove: ")
        print(title)
        #This doesnt remove anything even if the Title name is right?
        todolist.remove_from_list(title)
    elif x == 3:
        print("Printing To Do List...")
        print(todolist)
    elif x == 4:
        todolist.write_to_file("SavedList.txt")
    elif x == 5:
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
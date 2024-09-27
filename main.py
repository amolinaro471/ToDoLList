import linkedList as LL
LL.linkedList()
print("Welcome to ToDoLList")

def menu_printer():
    output = "1: Add Task\n2: Remove Task\n3. Print List\n4: Save list\n5: Load previous list\n6: Quit"
    print(output)

def inputChecker(input_num):
    x = input_num
    isDone = False
    if x == 1:
        print("Add Task")
    elif x == 2:
        print("Remove Task")
    elif x == 3:
        print("Printing To Do List...")
    elif x == 4:
        print("Save List")
    elif x == 5:
        print("Load Previous List")
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
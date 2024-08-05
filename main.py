import linkedList as LL
LL.linkedList()
print("Welcome to ToDoLList")

def menu_printer():
    output = "1: Add Task\n2: Remove Task\n3. Print List\n4: Save list\n5: Load previous list\n6: Quit"
    print(output)


def input_checker(x):
    if x < 1 or x > 6:
        print("Invalid choice")
    #Maybe also handle what functions get called from here
    return x

def main():
    isDone = False
    x = 0
    while not isDone:
        menu_printer()
        x = int(input())
        if x == 6:
            isDone = True
        input_checker(x)
    print("\nGoodbye!")

main()
class Node:
    def __init__(self,title):
        self.title = title
        self.tasks = None
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        temp = self.head
        out = ""
        while temp is not None:
            if temp is self.head:
                out = "Head --> \n"
            out = out + "Title: " + temp.title + "\n"
            for task in temp.tasks:
                out = out + "\t* " + task + "\n"
            temp = temp.next
        return out
    

    def add_to_list(self,title,tasks):
        new_node = Node(title)
        new_node.tasks = tasks
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def remove_from_list(self,title):
        temp = self.head
        before = temp
        if title is temp.title:
            self.head = temp.next
        else:
            temp = temp.next
            while temp is not None:
                if temp.title is title:
                    before.next = temp.next
                    break
                temp = temp.next
                before = before.next
                
            
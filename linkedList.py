class Node:
    def __init__(self,title):
        self.title = title
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        temp = self.head
        out = ""
        while temp is not None:
            if temp is self.head:
                out = "Head --> "
            out = out + "Title: " + temp.title + "\n"
            temp = temp.next
        return out
    

    def add_to_list(self,title):
        new_node = Node(title)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def remove_from_head(self):
        temp = self.head.next
        self.head = temp
            
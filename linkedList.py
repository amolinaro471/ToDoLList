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

    def remove_from_list(self,title):
        #check the head node
        #if head node, head node pointer goes to next node
        #check rest of node and repeat the same idea
        temp = self.head
        while temp is not None:
            if temp.title == title:
                if temp is self.head:
                    self.head = self.head.next
                # remove non head node now

            temp = temp.next
            


LList = linkedList()
LList.add_to_list("Head Node")
LList.add_to_list("Head Node New")
LList.add_to_list("Head Node Even Newer")
print(LList)

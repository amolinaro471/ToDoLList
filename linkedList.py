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

# LList = linkedList()
# LList.add_to_list("Head Node")
# LList.add_to_list("Head Node New")
# LList.add_to_list("Head Node Even Newer")

# # one_node = Node("TESTING1")
# # LList.head = one_node
# # LList.add_to_list("Testing Add")
# # LList.add_to_list("Testing Add Two")
# print(LList)
import linkedList as LL

testList = LL.linkedList()

testList.add_to_list("test1")
testList.add_to_list("test2")
testList.add_to_list("test3")

print(testList)

testList.remove_from_head()
testList.remove_from_head()

print(testList)
class Node():
    def __init__(self, ndata):
        self.data = ndata
        self.next = None

class LinkList():
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("The list is empty.")
        else:
            p = self.head
            while p is not None:
                print(p.data, " ")
                p = p.next

    def insert_start(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

mylist = LinkList
mylist.insert_start(13)
mylist.print()



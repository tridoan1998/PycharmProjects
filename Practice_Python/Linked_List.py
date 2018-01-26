class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class link_list():
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        p = self.head
        if(p is None):
            temp = Node(data)
            temp.next = self.head
            self.head = temp
        else:
            temp = Node(data)
            temp.next = p.next
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def print(self):
        temp = self.head
        if temp is None:
            print("empty.")
            return
        else:
            while(temp is not None):
                print(temp.data, " ")
                temp = temp.next



linklist = link_list()
linklist.insert_beginning(1)
linklist.print()



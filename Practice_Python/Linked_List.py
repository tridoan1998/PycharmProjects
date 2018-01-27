class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class link_list():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def print_size(self):
        return self.size

    def insert_start(self, data):
        if self.head is None:
            temp = Node(data)
            self.head = temp
            self.tail = temp
        else:
            temp = Node(data)
            temp.next = self.head
            self.head = temp
        self.size += 1

    def insert_end(self, data):
        if self.head is None:
            temp = Node(data)
            self.head = temp
            self.tail = temp
        else:
            temp = Node(data)
            self.tail.next = temp
            self.tail = temp
        self.size += 1

    def print(self):
        temp = self.head
        if temp is None:
            print("empty.")
            return
        else:
            while(temp is not None):
                print(temp.data, " ")
                temp = temp.next

    def remove_start(self):
        if self.size is 0:
            print("The list is already empty!")
            return
        elif self.size is 1:
            del self.head
            self.head = self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            del temp
        self.size -= 1   

    def remove_stop(self):
        if self.size is 0:
            print("the list is empty.")
            return
        elif self.size is 1:
            del self.head
            self.head = self.tail = None
        else:
            temp = self.tail
            self.tail = self.tail.next
            del temp
        self.size -= 1

    def get_size(self):
        return print(self.size)

    def search(self, value):
        temp = self.head
        count = 1
        while value != temp.data:
            temp = temp.next
            count += 1
            if temp.next is None:
                return print("The list has no data with the value ", value)
        return print(count)

linklist = link_list()

linklist.insert_end(13)
linklist.insert_end(20)
linklist.insert_end(100)
linklist.insert_end(40)

print("The size of the list is:", linklist.print_size())
linklist.search(20)


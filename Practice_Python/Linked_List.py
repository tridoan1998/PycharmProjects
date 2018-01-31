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
        return count

    def print_data_at_current_node(self, position):
        if self.size is 0:
            print("The list is already empty!")
            return
        else:
            temp = self.head
            count = 1
            while count < position :
                temp = temp.next
                count += 1
            if self.size is 1:
                del self.head
                self.head = self.tail = None
            else:

                print(temp.data)
    def delete_data_at_current_node(self, position):
        temp = self.head
        print(temp)
        print(temp.next)
        print(temp.next.next)
        print(temp.next.next.next)
        print(" ")

        count = 1
        while count < (position-1):
            temp = temp.next
            count += 1
        print(temp)
        del temp.next
        print(temp)

    def find_value_(self, value):
        temp = self.head
        while temp:
            if temp.data == value:
                return True
            else:
                temp = temp.next
            if temp.next is None:
                return False

    def count(self, value):
        temp = self.head
        count = 0
        if temp is None:
            print("The list is empty.")
            return
        while temp is not None:
            if temp.data == value:
                count += 1
                temp = temp.next
            else:
                temp = temp.next
        if count is 0:
            print("The list has no element ", value)
        else:
            print("The list has the element", value , " which occured: " , count , "times")


    def remove_a_node(self):
        temp = self.head
        temp = temp.next.next
        del temp.next


array = []
print(array.__len__())


keep = True
count = 0
while keep is True:
    x = int(input("Enter data here: "))
    array.append(x)
    count += 1
    y = str(input("Are you still want to input? Y or N"))
    print(y)
    if y is "y":
        continue
    elif y is "n":
        break

print("The array you created are: ", array)

def bubble_sort(array):
    #travel through all array element
    for i in range(0, array.__len__()):
        #
        for j in range(0, array.__len__()):
            if array[j] > array[i]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
            else:
                continue
        print(array)
    return array



print("The new array that sorted: ")
print(bubble_sort(array))




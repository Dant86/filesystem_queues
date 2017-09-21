class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, newVal):
        newVal = Node(newVal)
        if self.head is None or self.tail is None:
            self.head = newVal
            self.tail = newVal
            self.length += 1
            return
        self.tail.next = newVal
        self.tail = newVal
        self.length += 1

    def prepend(self, newVal):
        newVal = Node(newVal)
        if self.head is None or self.tail is None:
            self.head = newVal
            self.tail = newVal
            self.length += 1
            return
        newVal.next = self.head
        self.head = newVal
        self.length += 1

    def add(self, newVal, index):
        newNode = Node(newVal)
        if index < 0:
            raise ValueError("Index < 0")
        elif index == 0:
            self.prepend(newVal)
        elif index > 0 and index < self.length:
            temp = self.head
            for i in range(index - 1):
                temp = temp.next
            newNode.next = temp.next
            temp.next = newNode
            self.length += 1
        elif index == self.length:
            self.append(newVal)
        else:
            for i in range(index - self.length):
                self.append(0)
            self.append(newVal)

    def set(self, newVal, index):
        temp = self.head
        for i in range(index):
            temp = temp.next
        temp.value = newVal

    def remove_from_back(self):
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None
        self.length -= 1

    def remove_from_front(self):
        self.head = self.head.next
        self.length -= 1

    def remove(self, index):
        if index < 0:
            raise ValueError("Index < 0")
        elif index == 0:
            self.remove_from_front()
        elif index > 0 and index < self.length - 1:
            temp = self.head
            for i in range(index - 1):
                temp = temp.next
            temp.next = temp.next.next
            self.length -= 1
        elif index == self.length - 1:
            self.remove_from_back()
        else:
            raise ValueError("Index >= length of list")

    def itemAt(self, index):
        if index < 0:
            raise ValueError("Index < 0")
        elif index >= 0 and index < self.length:
            temp = self.head
            for i in range(index - 1):
                temp = temp.next
            return temp.value
        elif index >= self.length:
            raise ValueError("Index >= length of list")

    def indexOf(self, value):
        temp = self.head
        index = 0
        while temp is not None:
            if temp.value == value:
                return idx
            idx += 1
        return -1

    def length():
        return self.length

    def __str__(self):
        temp = self.head
        strVal = "["
        while temp is not None:
            strVal += str(temp.value)
            if temp.next is not None:
                strVal += ", "
            temp = temp.next
        return strVal + "]"

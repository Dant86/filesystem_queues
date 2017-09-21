import os
import sys
from ll import LinkedList

class Queue():

    def __init__(self):
        self.values = LinkedList()

    def add(self, newVal):
        self.values.append(newVal)

    def remove(self):
        self.values.remove_from_front()

    def length(self):
        return self.values.length()

    def itemAt(self, index):
        return self.values.itemAt(index)

    def indexOf(self, value):
        return self.values.indexOf(value)

    def __str__(self):
        return str(self.values)

def get_files(path, queue):
    for fname in os.listdir(path):
        if "." in fname:
            queue.add(fname)
        else:
            get_files(path + "/" + fname, queue)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("Usage: python filequeue.py [path_name]")
    path = sys.argv[1]
    files = Queue()
    get_files(path, files)
    print(files)
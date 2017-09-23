import os
import sys
import operator
from ll import LinkedList

class Queue():

    def __init__(self):
        self.values = LinkedList()

    def add(self, newVal):
        self.values.append(newVal)

    def remove(self):
        self.values.remove_from_front()

    def itemAt(self, index):
        return self.values.itemAt(index)

    def indexOf(self, value):
        return self.values.indexOf(value)

    def __len__(self):
        return self.values.length

    def __str__(self):
        return str(self.values)

class FileQueue(Queue):

    def __init__(self, initial_path):
        super(FileQueue, self).__init__()
        self.initial_path = initial_path

    def get_slash_counts(self):
        slashes = {}
        for i in range(self.values.length):
            slashes[self.itemAt(i)] = self.itemAt(i).count("/")
        return slashes

    def sort(self):
        slash_counts = self.get_slash_counts()
        sorted_items = sorted(slash_counts.items(), key=lambda x: x[1])
        new_ll = LinkedList()
        for(k, v) in sorted_items:
            new_ll.append(k)
        self.values = new_ll

    def __str__(self):
        retVal = ""
        self.sort()
        folders = [self.values.itemAt(0)[:self.values.itemAt(0).index("/")]]
        non_folders = []
        for i in range(self.values.length):
            item = self.values.itemAt(i)
            if "." not in item[item.index("/"):]:
                folders.append(item)
            else:
                non_folders.append(item)
        slash_counts = [folder.count("/") for folder in folders]
        minimum_slashes = min(slash_counts)
        for folder in folders:
            amt_slashes = folder.count("/")
            amt_indentations = amt_slashes - minimum_slashes
            for i in range(amt_indentations):
                retVal += "\t"
            retVal += folder + "\n"
            folder_length = len(folder)
            for non_folder in non_folders:
                if non_folder.count("/") - 1 == amt_slashes and non_folder[:folder_length] == folder:
                    for i in range(amt_indentations + 1):
                        retVal += "\t"
                    retVal += non_folder + "\n"
        return retVal

def get_files(path, queue):
    for fname in os.listdir(path):
        queue.add(path + "/" + fname)
        if "." not in fname:
            get_files(path + "/" + fname, queue)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("Usage: python filequeue.py [path_name]")
    path = sys.argv[1]
    files = FileQueue(path)
    get_files(path, files)
    print(files)
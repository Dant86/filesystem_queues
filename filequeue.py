import os
import sys

class Node:

	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	def append(self, i):
		if self.head is None or self.tail is None:
			self.head = Node(i)
			self.tail = Node(i)
			self.length += 1
			return
		newNode = Node(i)
		self.tail.next = newNode
		self.tail = newNode
		self.length += 1

	def prepend(self, i):
		newNode = Node(i)
		if self.head == None:
			self.tail = newNode
		newNode.next = self.head
		self.head = newNode
		self.length += 1

	def removeFromFront(self):
		newNode = self.head.next
		self.head = newNode
		self.length -= 1

	def removeFromBack(self):
		newNode = self.head
		while(newNode.next.next is not None):
			newNode = newNode.next
		newNode.next = None
		self.length -= 1

	def itemAt(self, idx):
		if idx > self.length-1 or idx < 0:
			raise ValueError("Index out of bounds")
		newNode = self.head
		for i in range(self.length-1):
			newNode = newNode.next
		return newNode.value

	def indexOf(self, i):
		newNode = self.head
		idx = 0
		while(newNode is not None):
			if newNode.value == i:
				return idx
			idx += 1
		return -1

	def set(self, newItem, idx):
		if idx > self.length-1 or idx < 0:
			raise ValueError("Index out of bounds")
		newNode = self.head
		for i in range(idx):
			newNode = newNode.next
		newNode.value = newItem

	def add(self, newItem, idx):
		newNode= Node(newItem)
		if self.head is None:
			self.head = newNode
			self.tail = newNode
			self.length += 1
			return
		if idx < 0:
			raise ValueError("Index out of bounds")
		if idx > self.length-1:
			for i in range(idx-self.length):
				self.append(0)
		trav = self.head
		for i in range(idx-1):
			trav = trav.next
		newNode.next = trav.next
		trav.next = newNode
		self.length += 1

	def remove(self, idx):
		if self.length == 1 and idx == 0:
			self.head = None
			self.tail = None
			self.length -= 1
			return
		trav = self.head
		for i in range(idx-1):
			trav = trav.next
		trav.next = trav.next.next

	def isEmpty(self):
		return this.head is None or this.tail is None

	def __str__(self):
		temp = self.head
		retVal = "["
		while temp is not None:
			retVal += str(temp.value)
			if temp.next is not None:
				retVal += ", "
			temp = temp.next
		retVal += "]"
		return retVal

foo = LinkedList()
foo.prepend(5)
foo.append(578)
foo.add(222, 1)
foo.add(23468,3)
foo.set(52, 3)
foo.prepend(12)
foo.append(123)
print(foo)


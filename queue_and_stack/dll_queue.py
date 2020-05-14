import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def dequeue(self):
        # print(f'Dequeue {self.size}')
        if self.size != 0:
            self.size -= 1
            return self.storage.remove_from_tail()
        else:
            # print('The list is empty')
            return None

    def len(self):
        # print(f'\n self.size {self.size}')
        return self.size

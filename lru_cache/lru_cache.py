import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class dll(object):
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.head = dll(-1, -1)
        self.tail = self.head
        self.cache = {}
        self.capacity = limit
        self.length = 0
    
    def move_to_end(self, node):
        while node.next:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
        
    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key not in self.cache:
            return None
        node = self.cache[key]
        value = node.value
        #move node to end of linked list
        # self.storage.move_to_end(node)
        self.move_to_end(node)
        return value
            

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        #check if key is in cache

        if key in self.cache:
            node = self.cache[key]
            node.value = value
            #move to end
            # self.storage.move_to_end(node)
            self.move_to_end(node)  
        else:
            #create new node and insert at end
            # print(key)
            # self.storage.add_to_tail(value, key)
            node = dll(key, value)
            self.cache[key] = node
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.length += 1
            #check length
            if self.length > self.capacity:
                #if at capacity remove head
                # self.storage.remove_from_head()
                remove = self.head.next
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
                del self.cache[remove.key]
                self.length -= 1

test = LRUCache(3)
test.set('item1', 'a')
test.set('item2', 'b')
test.set('item3', 'c')
test.set('item4', 'd')
test.set('item3', 'h')
# print(test.storage.get_max())
print(test.get('item3'))
print(test.get('item1'))
print(test.cache['item2'].next)
# print(test.capacity)
# print(test.length)
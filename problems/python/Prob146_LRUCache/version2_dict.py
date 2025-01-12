class DoubleLLNode:
    def __init__(self, key: int):
        self.key = key
        self.prev = None
        self.next = None

class Queue:
    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.count = 0
        self.capacity = capacity

    # Returns true if there was enough space to add node
    def enqueue(self, node: DoubleLLNode) -> bool:
        if self.count >= self.capacity:
            return False

        # Queue is not empty
        if self.tail is not None:
            self.tail.next = node
        else:
            self.head = node
    
        node.prev = self.tail
        node.next = None
        self.tail = node
        self.count += 1
        return True

    # Returns LRU key
    def dequeue(self) -> int:
        if self.count == 0:
            return -1
        
        key = self.head.key
        self.head = self.head.next
        self.count -= 1

        if self.head is None:
            self.tail = None

        return key

    # If key was present in cache already, move it to tail (MRU)
    def update(self, node: DoubleLLNode) -> None:
        if self.tail == node:
            return

        if self.head == node:
            self.head = self.head.next
            if self.head is None:
                self.tail = None

        if node.prev is not None:
            (node.prev).next = node.next
        if node.next is not None:
            (node.next).prev = node.prev

        self.count -= 1
        self.enqueue(node)

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.queue = Queue(capacity)  # Queue where head is LRU and tail is MRU
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            entry = self.cache[key]
            self.queue.update(entry[1])
            return entry[0]
        return -1

    def put(self, key: int, value: int) -> None:
        # New key
        if not key in self.cache:
            node = DoubleLLNode(key)
            self.cache[key] = [value, node]

            if not self.queue.enqueue(node):
                key_to_delete = self.queue.dequeue()
                del self.cache[key_to_delete]  # Delete LRU from cache
                self.queue.enqueue(node)
        # Existing key
        else:
            entry = self.cache[key]
            entry[0] = value
            self.queue.update(entry[1])

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
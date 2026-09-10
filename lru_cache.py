# Tags: design, linked-list, review-priority
class LinkedList:
    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.previous = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.cache= {}

    def get(self, key: int) -> int:
        res = -1
        if key in self.cache:
            res = self.cache[key][0]
            if self.cache[key][1] != self.tail:
                node = self.cache[key][1]
                self.move_node_to_tail(node)
        return res
    
    def move_node_to_tail(self, node: LinkedList):
        next_node = node.next
        if next_node:
            next_node.previous = node.previous
        if node.previous:
            node.previous.next = next_node
        else:
            self.head = next_node
            self.head.previous = None
        node.next = None
        self.tail.next = node
        node.previous = self.tail
        self.tail = node

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:      
            node = LinkedList(key)
            self.cache[key] = [value, node]
            if not self.head:
                self.head = node
                self.tail = node
            else:
                self.tail.next = node
                node.previous = self.tail
                self.tail = node
        else:
            node = self.cache[key][1]
            self.cache[key][0] = value
            if self.tail != node:
                self.move_node_to_tail(node)

        if len(self.cache) > self.capacity:
            old_key = self.head.value
            del self.cache[old_key]
            self.head = self.head.next
            self.head.previous = None
    
if __name__ == "__main__":
    lru = LRUCache(3)
    lru.put(1, 1)
    lru.put(2, 2)
    lru.put(3, 3)
    print(lru.get(1))
    print(lru.get(2))
    print(lru.get(4))
    lru.put(4, 4)
    print(lru.get(1))
    print(lru.get(2))
    print(lru.get(3))
    print(lru.get(4))
    print(lru.get(2))
    lru.put(1, 8)
    lru.put(3, 7)
    print(lru.get(1))

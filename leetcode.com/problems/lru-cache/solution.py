
class DLL: # DoublyLinkedList
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)

        # making circular
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        node.next = self.head.next
        node.prev = self.head

        last_recent = self.head.next
        self.head.next = node
        last_recent.prev = node

    def delete(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    def first(self):
        return self.head.next

    def last(self):
        return self.tail.prev



class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = {}
        self.seq = DLL()


    def get(self, key: int) -> int:
        if key in self.data:
            node = self.data[key]

            self._delete(key)
            self.put(node.key, node.val)

            return node.val
        
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self._delete(key)

        self._check_space()
        self._add(key, value)


    def _check_space(self) -> None:
        if len(self.data) == self.capacity:
            self._delete(self.seq.last().key)
        
    def _add(self, key: int, value: int) -> None:
        self.seq.add(DLL.Node(key, value))
        self.data[key] = self.seq.first()
        

    def _delete(self, key: int) -> None:
        node = self.data[key]
        del self.data[key]
        self.seq.delete(node)
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

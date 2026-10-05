class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.termTable = dict() # key: term, val: key
        self.keyTable = dict() # key: key, val: term
        self.keys = dict()
        self.term = 0
        self.evictTerm = 0

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        
        oldTerm = self.keyTable.pop(key)
        self.termTable.pop(oldTerm)

        self.keyTable[key] = self.term
        self.termTable[self.term] = key
        self.term += 1

        while self.evictTerm not in self.termTable:
            self.evictTerm += 1

        return self.keys[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            oldTerm = self.keyTable.pop(key)
            self.termTable.pop(oldTerm)
        else:
            if self.size == self.capacity:
                evictKey = self.termTable.pop(self.evictTerm)
                self.keyTable.pop(evictKey)
                self.keys.pop(evictKey)
                self.size -= 1
            self.size += 1

        self.keys[key] = value
        self.keyTable[key] = self.term
        self.termTable[self.term] = key
        self.term += 1

        while self.evictTerm not in self.termTable:
            self.evictTerm += 1

            
            
        
        
        


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
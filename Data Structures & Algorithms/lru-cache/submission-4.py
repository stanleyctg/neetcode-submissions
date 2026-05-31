from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.recent_accesses = deque()

    def get(self, key: int) -> int:
        # update recent_accesses
        if key in self.cache:
            if key in self.recent_accesses:
                self.recent_accesses.remove(key)
            self.recent_accesses.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        # check capacity
        if key not in self.cache and len(self.cache) == self.capacity:
            del self.cache[self.recent_accesses.popleft()]
        if key in self.recent_accesses:
            self.recent_accesses.remove(key)
        self.recent_accesses.append(key)
        self.cache[key] = value


        

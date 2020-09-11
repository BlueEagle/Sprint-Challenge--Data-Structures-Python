class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.last_modified = 0
        self.storage = []

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            self.storage[self.last_modified] = item
            self.last_modified += 1
            if self.last_modified == self.capacity:
                self.last_modified = 0

    def get(self):
        return self.storage

from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data: list):
        self.data = data
        self.index = 0

    def __next__(self):
        try:
            result = self.data[self.index]
            self.index += 1
            return result
        except Exception:
            raise StopIteration

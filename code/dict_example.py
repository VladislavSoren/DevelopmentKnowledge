numbers = [1, 22, 33, 44]

class NumberStorage:
    def __init__(self):
        self.buckets = [[] for _ in range(10)]

    def get_bucket(self, x):
        return abs(x) % len(self.buckets)

    def store_numbers(self, numbers):
        for number in numbers:
            self.buckets[self.get_bucket(number)].append(number)

    def has_number(self, x):
        return x in self.buckets[self.get_bucket(x)]
    
ns = NumberStorage()
ns.store_numbers(numbers)
print(ns.has_number(1))
print(ns.has_number(6))
class EvenOddSumTracker:
    def __init__(self):
        self.num = []

    def add_number(self, n):
        self.num.append(n)

    def even_sum(self):
        return sum([x if x % 2 == 0 else 0 for x in self.num ])

    def odd_sum(self):
        return sum([x if x % 2 != 0 else 0 for x in self.num ])
tracker = EvenOddSumTracker()
tracker.add_number(2)
tracker.add_number(3)
tracker.add_number(4)
tracker.add_number(5)
print(tracker.even_sum())
print(tracker.odd_sum())

class MinMaxNumberFinder:
    def __init__(self):
        self.numbers = []

    def add_number(self, n):
        self.numbers.append(n)

    def min_numbers(self):
        if not self.numbers:
            return []
        min_val = min(self.numbers)
        return [x for x in self.numbers if x == min_val]

    def max_numbers(self):
        if not self.numbers:
            return []
        max_val = max(self.numbers)
        return sorted(set(x for x in self.numbers if x == max_val))
finder = MinMaxNumberFinder()
finder.add_number(5)
finder.add_number(1)
finder.add_number(9)
finder.add_number(1)
finder.add_number(7)
print(finder.min_numbers())
print(finder.max_numbers())

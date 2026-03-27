class NumberDivider:
    def __init__(self):
        self.divisible_list = []
        self.not_divisible_list = []

    def add_number(self, n):
        if n % 3 == 0:
            self.divisible_list.append(n)
        else:
            self.not_divisible_list.append(n)

    def divisible(self):
        return self.divisible_list

    def not_divisible(self):
        return self.not_divisible_list

divider = NumberDivider()
divider.add_number(1)
divider.add_number(3)
divider.add_number(4)
divider.add_number(6)
divider.add_number(7)
print(divider.divisible())
print(divider.not_divisible())

class LimitedCounter:
    def __init__(self, limit):
        self.__value = 0
        self.__limit = limit

    def increment(self):
        if self.__value < self.__limit:
            self.__value += 1

    def decrement(self):
        if self.__value > 0:
            self.__value -= 1

    def get_value(self):
        return self.__value

counter = LimitedCounter(3)
counter.increment()
counter.increment()
counter.increment()
counter.increment()
print(counter.get_value())
counter.decrement()
print(counter.get_value())

class FlipFlopBell:
    def __init__(self):
        self.next = "flip"

    def ring(self):
        print(self.next)
        self.next = "flop" if self.next == "flip" else "flip"
bell = FlipFlopBell()
bell.ring()
bell.ring()
bell.ring()

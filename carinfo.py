class CarInfo:

    def __init__(self, orig, index, upper):
        self.orig = orig
        self.index = index
        self.upper = upper

    def __repr__(self) -> str:
        return f"CarInfo({self.orig}, {self.index}, {self.upper})"







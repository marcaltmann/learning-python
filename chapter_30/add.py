class Commuter1:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other

    def __radd__(self, other):
        print('radd', self.val, other)
        return other + self.val


class Commuter2:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other

    def __radd__(self, other):
        return self.__add__(other)


class Commuter3:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other

    def __radd__(self, other):
        return self + other


class Commuter4:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other

    __radd__ = __add__


class Commuter5:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        if isinstance(other, Commuter5):
            other = other.val
        return Commuter5(self.val + other)

    def __radd__(self, other):
        print('radd', self.val, other)
        return Commuter5(other + self.val)

    def __iadd__(self, other):
        print('iadd', self.val, other)
        self.val += other
        return self

    def __repr__(self):
        return '<Commuter5: %s>' % self.val

class Truth:
    def __bool__(self):
        return True

class Truth2:
    def __bool__(self):
        return False

class Something:
    def __len__(self):
        return 5

class Something2:
    def __len__(self):
        return 0

class Something3:
    def __len__(self):
        return -2

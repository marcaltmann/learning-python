class UpsideDown:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, i):
        return self.data[i]

    def __contains__(self, i):
        return not (i in self.data)

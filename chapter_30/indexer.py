class Indexer:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        print(index)
        return index

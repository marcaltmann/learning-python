class Empty:
    def __getattr__(self, attrname):
        if attrname == 'age':
            return 40
        else:
            raise AttributeError(attrname)

    def __getattribute__(self, attrname):
        return 'spam'

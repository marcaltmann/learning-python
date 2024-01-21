class Super:
    def delegate(self):
        self.action()

    def action(self):
        #assert False, 'action must be defined!'
        raise NotImplementedError('action must be defined!')

X = Super()
X.delegate()

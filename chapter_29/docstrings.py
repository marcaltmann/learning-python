"I am: docstrings.__doc__"

def func(args):
    "I am: docstrings.func.__doc__"
    pass

class spam:
    "I am: spam.__doc__ or docstrings.spam.__doc__ or self.__doc__"
    def method(self):
        "I am: spam.method.__doc__ or self.method.__doc__"
        print(self.__doc__)
        print(self.method.__doc__)

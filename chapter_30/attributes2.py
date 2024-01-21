from typing import Any

class Crazy:
    def __setattr__(self, name: str, value: Any) -> None:
        self.__dict__[name] = value + 10

    def __delattr__(self, name: str) -> None:
        print('deleting')
        del self.__dict__[name]

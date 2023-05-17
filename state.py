class State:
    def __init__(self, name : str, is_accept : bool = False) -> None:
        self.name = name
        self.is_accept = is_accept
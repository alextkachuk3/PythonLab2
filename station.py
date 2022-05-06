class Station:

    def __init__(self, id: str, name: str, open: str, close: str):
        if type(id) != str:
            raise ValueError("id value should be string")
        if type(name) != str:
            raise ValueError("name value should be string")
        if type(open) != str:
            raise ValueError("open value should be string")
        if type(close) != str:
            raise ValueError("close value should be string")
        self.id = id
        self.name = name
        self.open = open
        self.close = close

    def update_name(self, name: str):
        if type(name) != str:
            raise ValueError("name value should be string")
        self.name = name

    def update_open_time(self, open: str):
        if type(open) != str:
            raise ValueError("open value should be string")
        self.open = open

    def update_close_time(self, close: str):
        if type(close) != str:
            raise ValueError("close value should be string")
        self.close = close

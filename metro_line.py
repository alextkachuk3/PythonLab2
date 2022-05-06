from station import Station


class MetroLine:

    def __init__(self, id: str, color: str):
        if type(id) != str:
            raise ValueError("id value should be string")
        if type(color) != str:
            raise ValueError("color value should be string")
        self.stations = []
        self.id = id
        self.color = color

    def add_station(self, name: str, open: str, close: str, id=None, index=None):

        if id is None:
            if len(self.stations) == 0:
                id = 's-' + self.id[1:] + '-1'
            else:
                id = 's' + self.id[1:] + '-' + str(get_last_number(self.stations[len(self.stations) - 1].id) + 1)

        if index is None:
            self.stations.append(Station(id, name, open, close))
        else:
            self.stations.insert(index, Station(id, name, open, close))

    def remove_station(self, id: str):
        self.stations = list(filter(lambda x: x.id != id, self.stations))

    def update_color(self, color):
        if type(color) != str:
            raise ValueError("color value should be string")
        self.color = color


def get_last_number(text: str) -> int:
    prev_is_not_digit = False
    last_num_pos = 0
    for i in range(0, len(text)):
        if not text[i].isnumeric():
            prev_is_not_digit = True
        else:
            if prev_is_not_digit:
                prev_is_not_digit = False
                last_num_pos = i
    return int(text[last_num_pos:])

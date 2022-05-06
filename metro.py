from metro_line import MetroLine


class Metro:
    def __init__(self):
        self.lines = []

    def add_line(self, color: str, id=None):
        if id is None:
            if len(self.lines) == 0:
                id = 'l-0'
            else:
                id = 'l-' + str(int(self.lines[len(self.lines) - 1].id[2:]) + 1)
        self.lines.append(MetroLine(id, color))

    def delete_line(self, id: str):
        self.lines = list(filter(lambda x: x.id != id, self.lines))

    def update_color(self, id: str, color: str):
        list(filter(lambda x: x.id == id, self.lines))[0].update_color(color)

    def add_station_to_line(self, line_id: str, name: str, open: str, close: str, id=None):
        list(filter(lambda x: x.id == line_id, self.lines))[0].add_station(name, open, close, id)

    def delete_station(self, station_id):
        ind = self.find_index_of_station(station_id)
        if ind is None:
            raise ValueError("Station with id " + station_id + " not exist")
        self.lines[ind[0]].stations.pop(ind[1])

    def find_station(self, station_id):
        ind = self.find_index_of_station(station_id)
        return self.lines[ind[0]].stations[ind[1]]

    def find_index_of_station(self, station_id):
        result = None
        for i, line in enumerate(self.lines):
            for j, station in enumerate(line.stations):
                if station.id == station_id:
                    result = [i, j]
        return result

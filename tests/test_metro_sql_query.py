import unittest

from metro import Metro
from test_config import host, port, user, password, db_name


class TestMetroSQL(unittest.TestCase):
    def drop_tables(self):
        self.metro.connection.cursor().execute("DROP TABLE metro_lines, metro_stations")

    def test_adding_lines(self):
        self.metro = Metro(host, port, user, password, db_name)
        self.metro.add_line('green')
        self.metro.add_line('red')
        self.metro.add_line('blue')
        result = self.metro.lines_list()
        self.drop_tables()
        self.assertEqual(result, [(1, 'green'), (2, 'red'), (3, 'blue')])

    def test_deleting_lines(self):
        self.metro = Metro(host, port, user, password, db_name)
        self.metro.add_line('green')
        self.metro.add_line('red')
        self.metro.add_line('blue')
        self.metro.delete_line(2)
        result = self.metro.lines_list()
        self.drop_tables()
        self.assertEqual(result, [(1, 'green'), (3, 'blue')])

    def test_adding_stations(self):
        self.metro = Metro(host, port, user, password, db_name)
        self.metro.add_line('green')
        self.metro.add_line('red')
        self.metro.add_line('blue')
        self.metro.add_station('Teremky', 3, '6:00:00', '23:45:00')
        self.metro.add_station('Vystavkovyi Tsentr', 3, '6:00:00', '23:45:00')
        self.metro.add_station('Vasylkivska', 3, '6:00:00', '23:45:00')
        self.metro.add_station('Syrets', 1, '6:00:00', '23:40:00')
        self.metro.add_station('Akademmistechko', 2, '6:00:00', '23:45:00')
        self.metro.add_station('Holosiivska', 3, '6:30:00', '23:45:00')
        self.metro.add_station('Dorohozhychi', 1, '6:00:00', '23:40:00')
        self.metro.add_station('Lukianivska', 1, '6:00:00', '23:40:00')
        self.metro.add_station('Sviatoshyn', 2, '6:00:00', '23:30:00')
        self.metro.add_station('Nykvy', 2, '6:00:00', '23:45:00')
        self.metro.add_station('Zoloti Vorota', 1, '6:00:00', '23:40:00')
        self.metro.add_station('Demiivska', 3, '6:00:00', '23:45:00')
        result_stations = self.metro.stations_list()
        print(result_stations)
        self.drop_tables()
        self.assertEqual(result_stations, [(1, 'Teremky', '6:00:00', '23:45:00', 3), (2, 'Vystavkovyi Tsentr', '6:00:00', '23:45:00', 3), (3, 'Vasylkivska', '6:00:00', '23:45:00', 3), (4, 'Syrets', '6:00:00', '23:40:00', 1), (5, 'Akademmistechko', '6:00:00', '23:45:00', 2), (6, 'Holosiivska', '6:30:00', '23:45:00', 3), (7, 'Dorohozhychi', '6:00:00', '23:40:00', 1), (8, 'Lukianivska', '6:00:00', '23:40:00', 1), (9, 'Sviatoshyn', '6:00:00', '23:30:00', 2), (10, 'Nykvy', '6:00:00', '23:45:00', 2), (11, 'Zoloti Vorota', '6:00:00', '23:40:00', 1), (12, 'Demiivska', '6:00:00', '23:45:00', 3)])

    def test_deleting_stations(self):
        self.metro = Metro(host, port, user, password, db_name)
        self.metro.add_line('green')
        self.metro.add_line('red')
        self.metro.add_line('blue')
        self.metro.add_station('Teremky', 3, '6:00:00', '23:45:00')
        self.metro.add_station('Vystavkovyi Tsentr', 3, '6:00:00', '23:45:00')
        self.metro.add_station('Vasylkivska', 3, '6:00:00', '23:45:00')
        self.metro.add_station('Syrets', 1, '6:00:00', '23:40:00')
        self.metro.add_station('Akademmistechko', 2, '6:00:00', '23:45:00')
        self.metro.add_station('Holosiivska', 3, '6:30:00', '23:45:00')
        self.metro.add_station('Dorohozhychi', 1, '6:00:00', '23:40:00')
        self.metro.add_station('Lukianivska', 1, '6:00:00', '23:40:00')
        self.metro.add_station('Sviatoshyn', 2, '6:00:00', '23:30:00')
        self.metro.add_station('Nykvy', 2, '6:00:00', '23:45:00')
        self.metro.add_station('Zoloti Vorota', 1, '6:00:00', '23:40:00')
        self.metro.add_station('Demiivska', 3, '6:00:00', '23:45:00')

        self.metro.delete_station(3)
        self.metro.delete_station(5)
        self.metro.delete_station(9)
        self.metro.delete_station(4)
        result_stations = self.metro.stations_list()
        print(result_stations)
        self.drop_tables()
        self.assertEqual(result_stations, [(1, 'Teremky', '6:00:00', '23:45:00', 3), (2, 'Vystavkovyi Tsentr', '6:00:00', '23:45:00', 3), (6, 'Holosiivska', '6:30:00', '23:45:00', 3), (7, 'Dorohozhychi', '6:00:00', '23:40:00', 1), (8, 'Lukianivska', '6:00:00', '23:40:00', 1), (10, 'Nykvy', '6:00:00', '23:45:00', 2), (11, 'Zoloti Vorota', '6:00:00', '23:40:00', 1), (12, 'Demiivska', '6:00:00', '23:45:00', 3)])

    def test_deleting_station_after_deleting_line(self):
        self.metro = Metro(host, port, user, password, db_name)
        self.metro.add_line('green')
        self.metro.add_line('red')
        self.metro.add_line('blue')
        self.metro.add_station('Teremky', 3, '6:00:00', '23:45:00')
        self.metro.add_station('Vystavkovyi Tsentr', 3, '6:00:00', '23:45:00')
        self.metro.add_station('Vasylkivska', 3, '6:00:00', '23:45:00')
        self.metro.add_station('Syrets', 1, '6:00:00', '23:40:00')
        self.metro.add_station('Akademmistechko', 2, '6:00:00', '23:45:00')
        self.metro.add_station('Holosiivska', 3, '6:30:00', '23:45:00')
        self.metro.add_station('Dorohozhychi', 1, '6:00:00', '23:40:00')
        self.metro.add_station('Lukianivska', 1, '6:00:00', '23:40:00')
        self.metro.add_station('Sviatoshyn', 2, '6:00:00', '23:30:00')
        self.metro.add_station('Nykvy', 2, '6:00:00', '23:45:00')
        self.metro.add_station('Zoloti Vorota', 1, '6:00:00', '23:40:00')
        self.metro.add_station('Demiivska', 3, '6:00:00', '23:45:00')

        self.metro.delete_line(1)
        self.metro.delete_line(3)
        result_stations = self.metro.stations_list()
        print(result_stations)
        self.drop_tables()
        self.assertEqual(result_stations, [(5, 'Akademmistechko', '6:00:00', '23:45:00', 2), (9, 'Sviatoshyn', '6:00:00', '23:30:00', 2), (10, 'Nykvy', '6:00:00', '23:45:00', 2)])

    def test_search_station_by_name(self):
        self.metro = Metro(host, port, user, password, db_name)
        self.metro.add_line('green')
        self.metro.add_line('red')
        self.metro.add_line('blue')
        self.metro.add_station('Teremky', 3, '6:00:00', '23:45:00')
        self.metro.add_station('Vystavkovyi Tsentr', 3, '6:00:00', '23:45:00')
        self.metro.add_station('Vasylkivska', 3, '6:00:00', '23:45:00')
        self.metro.add_station('Syrets', 1, '6:00:00', '23:40:00')
        self.metro.add_station('Akademmistechko', 2, '6:00:00', '23:45:00')
        self.metro.add_station('Holosiivska', 3, '6:30:00', '23:45:00')
        self.metro.add_station('Dorohozhychi', 1, '6:00:00', '23:40:00')
        self.metro.add_station('Lukianivska', 1, '6:00:00', '23:40:00')
        self.metro.add_station('Sviatoshyn', 2, '6:00:00', '23:30:00')
        self.metro.add_station('Nykvy', 2, '6:00:00', '23:45:00')
        self.metro.add_station('Zoloti Vorota', 1, '6:00:00', '23:40:00')
        self.metro.add_station('Demiivska', 3, '6:00:00', '23:45:00')

        result = self.metro.find_station('Sviatoshyn')
        print(result)
        self.drop_tables()
        self.assertEqual(result, (9, 'Sviatoshyn', '6:00:00', '23:30:00', 2))

    def test_count_of_stations_on_line(self):
        self.metro = Metro(host, port, user, password, db_name)
        self.metro.add_line('green')
        self.metro.add_line('red')
        self.metro.add_line('blue')
        self.metro.add_station('Teremky', 3, '6:00:00', '23:45:00')
        self.metro.add_station('Vystavkovyi Tsentr', 3, '6:00:00', '23:45:00')
        self.metro.add_station('Vasylkivska', 3, '6:00:00', '23:45:00')
        self.metro.add_station('Syrets', 1, '6:00:00', '23:40:00')
        self.metro.add_station('Akademmistechko', 2, '6:00:00', '23:45:00')
        self.metro.add_station('Holosiivska', 3, '6:30:00', '23:45:00')
        self.metro.add_station('Dorohozhychi', 1, '6:00:00', '23:40:00')
        self.metro.add_station('Lukianivska', 1, '6:00:00', '23:40:00')
        self.metro.add_station('Sviatoshyn', 2, '6:00:00', '23:30:00')
        self.metro.add_station('Nykvy', 2, '6:00:00', '23:45:00')
        self.metro.add_station('Zoloti Vorota', 1, '6:00:00', '23:40:00')
        self.metro.add_station('Demiivska', 3, '6:00:00', '23:45:00')

        result = self.metro.count_of_stations_on_line(3)
        print(result)
        self.drop_tables()
        self.assertEqual(result, 5)

    def test_update_station_name(self):
        self.metro = Metro(host, port, user, password, db_name)
        self.metro.add_line('green')
        self.metro.add_line('red')
        self.metro.add_line('blue')
        self.metro.add_station('Teremky', 3, '6:00:00', '23:45:00')
        self.metro.add_station('Vystavkovyi Tsentr', 3, '6:00:00', '23:45:00')
        self.metro.add_station('Vasylkovska', 3, '6:00:00', '23:45:00')
        self.metro.add_station('Syrets', 1, '6:00:00', '23:40:00')
        self.metro.add_station('Akademmistechko', 2, '6:00:00', '23:45:00')
        self.metro.add_station('Holosivska', 3, '6:30:00', '23:45:00')
        self.metro.add_station('Dorohozhychi', 1, '6:00:00', '23:40:00')

        self.metro.update_station_name(3, 'Vasylkivska')
        self.metro.update_station_name(6, 'Holosiivska')

        result = self.metro.stations_list()

        print(result)
        self.drop_tables()
        self.assertEqual(result, [(1, 'Teremky', '6:00:00', '23:45:00', 3), (2, 'Vystavkovyi Tsentr', '6:00:00', '23:45:00', 3), (3, 'Vasylkivska', '6:00:00', '23:45:00', 3), (4, 'Syrets', '6:00:00', '23:40:00', 1), (5, 'Akademmistechko', '6:00:00', '23:45:00', 2), (6, 'Holosiivska', '6:30:00', '23:45:00', 3), (7, 'Dorohozhychi', '6:00:00', '23:40:00', 1)])


if __name__ == '__main__':
    unittest.main()

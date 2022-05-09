from metro import Metro

from config import host, port, user, password, db_name


if __name__ == '__main__':
    q = Metro(host, port, user, password, db_name)
    # q.add_station("Nivki", 5, "06:00:00", "23:00:00")
    # print(q.stations_list(), sep='\t')
    # print(q.lines_list())
    # print(q.find_station(5))
    # print(q.find_line(4))

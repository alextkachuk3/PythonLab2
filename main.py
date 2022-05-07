from metro import Metro

if __name__ == '__main__':
    q = Metro()
    #q.add_station("Nivki", 5, "06:00:00", "23:00:00")
    print(q.stations_list(), sep='\t')
    print(q.lines_list())
    print(q.find_station(5))
    print(q.find_line(4))

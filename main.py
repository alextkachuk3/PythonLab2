from metro import Metro

if __name__ == '__main__':
    q = Metro()
    #q.add_station("Nivki", 5, "06:00:00", "23:00:00")
    print(q.stations_list(), sep='\t')
    print(q.lines_list())

    # try:
    #     connection = pymysql.connect(
    #         host=host,
    #         port=3306,
    #         user=user,
    #         password=password,
    #         database=db_name
    #     )
    #     print('Successfully connected...')
    #
    #     try:
    #         with connection.cursor() as cursor:
    #             cursor.execute('SHOW TABLES')
    #
    #             for x in cursor:
    #                 print(x)
    #
    #             create_metro_lines_table_query = "CREATE TABLE metro_lines(" \
    #                                              "id INT AUTO_INCREMENT PRIMARY KEY, " \
    #                                              "color VARCHAR(50));"
    #
    #             cursor.execute(create_metro_lines_table_query)
    #             print("Metro lines table created successfully")
    #
    #             create_metro_stations_table_query = "CREATE TABLE metro_stations(" \
    #                                                 "id INT AUTO_INCREMENT PRIMARY KEY, " \
    #                                                 "name VARCHAR(100), " \
    #                                                 "open TIME, " \
    #                                                 "close TIME, " \
    #                                                 "metro_line_id INT, " \
    #                                                 "FOREIGN KEY (metro_line_id) " \
    #                                                 "REFERENCES metro_lines(id) " \
    #                                                 "ON UPDATE CASCADE ON DELETE RESTRICT);"
    #
    #             cursor.execute(create_metro_stations_table_query)
    #             print("Metro stations table created successfully")
    #
    #     finally:
    #         connection.close()
    #
    # except Exception as ex:
    #     print('Connection refused...')
    #     print(ex)



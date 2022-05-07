import pymysql as pymysql

from config import host, user, password, db_name


class Metro:
    def __init__(self):
        self.connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name
        )
        print('Successfully connected...')

        with self.connection.cursor() as cursor:
            cursor.execute('SHOW TABLES')

            table_list = self.get_table_list()

            if 'metro_lines' not in table_list:
                create_metro_lines_table_query = "CREATE TABLE metro_lines(" \
                                                 "id INT AUTO_INCREMENT PRIMARY KEY, " \
                                                 "color VARCHAR(50));"
                cursor.execute(create_metro_lines_table_query)
                print("Metro lines table created successfully")

            if 'metro_stations' not in table_list:
                create_metro_stations_table_query = "CREATE TABLE metro_stations(" \
                                                    "id INT AUTO_INCREMENT PRIMARY KEY, " \
                                                    "name VARCHAR(100), " \
                                                    "open TIME, " \
                                                    "close TIME, " \
                                                    "metro_line_id INT, " \
                                                    "FOREIGN KEY (metro_line_id) " \
                                                    "REFERENCES metro_lines(id) " \
                                                    "ON UPDATE CASCADE ON DELETE RESTRICT);"
                cursor.execute(create_metro_stations_table_query)
                print("Metro stations table created successfully")

    def __del__(self):
        self.connection.close()
        print('Connection closed...')

    def get_table_list(self):
        table_name_list = []
        with self.connection.cursor() as cursor:
            cursor.execute('SHOW TABLES')
            for x in cursor:
                table_name_list.append(x[0])
        return table_name_list

    # def add_line(self, color: str, id=None):
    #

    # def delete_line(self, id: str):
    #
    #
    # def update_color(self, id: str, color: str):
    #
    #
    # def add_station_to_line(self, line_id: str, name: str, open: str, close: str, id=None):
    #
    #
    # def delete_station(self, station_id):
    #
    #
    # def find_station(self, station_id):
    #
    #
    # def find_index_of_station(self, station_id):

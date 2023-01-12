class DateTime:
    def __init__(self, time: str, date: str):
        self.__time = time
        self.__date = date

    def create_date_time_by_tuple(self, deadline: tuple):
        self.__date = deadline[4]
        self.__time = deadline[5]

    def get_time(self):
        return self.__time

    def get_date(self):
        return self.__date

    def __str__(self):
        return f'{self.__date} {self.__time}'

    time = property(get_time)
    date = property(get_date)
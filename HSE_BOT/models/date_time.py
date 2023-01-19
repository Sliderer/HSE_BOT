class DateTime:
    def __init__(self, time: str, date: str):
        self.__time = str(time)
        self.__date = str(date)
        self.__deadline_gap = 360

    def compare_by_time(self, compare_time: str):
        hours, minutes = list(map(int, self.__time.split(':')[:-1]))
        compare_hours, compare_minutes = list(map(int, compare_time.split(':')))
        difference = hours * 60 + minutes - compare_hours * 60 - compare_minutes
        return 0 <= difference <= self.__deadline_gap

    def get_time(self):
        return self.__time

    def get_date(self):
        return self.__date

    def __str__(self):
        return f'{self.__date} {self.__time}'

    time = property(get_time)
    date = property(get_date)

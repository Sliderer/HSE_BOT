import typing


class Deadline:
    def __init__(self, data: typing.Dict, user_id: int):
        self.__title: str = str(data['title'])
        self.__description: str = str(data['description'])
        self.__date: str = str(data['date'])
        self.__time: str = str(data['time'])
        self.__user_id: int = int(user_id)

    def __str__(self):
        return f'Title: {self.__title} \n' \
               f'Description: {self.__description} \n' \
               f'Date: {self.__date} \n' \
               f'Time: {self.__time}'

    def get_user_id(self):
        return self.__user_id

    def get_title(self):
        return self.__title

    def get_description(self):
        return self.__description

    def get_date(self):
        return self.__date

    def get_time(self):
        return self.__time

    user_id = property(get_user_id)
    title = property(get_title)
    description = property(get_description)
    date = property(get_date)
    time = property(get_time)

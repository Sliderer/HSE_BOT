class User:
    def __init__(self, user_id: int, first_name: str, second_name: str):
        self.__user_id = user_id
        self.__first_name = first_name
        self.__second_name = second_name

    def get_user_id(self):
        return self.__user_id

    def get_first_name(self):
        return self.__first_name

    def get_second_name(self):
        return self.__second_name

    user_id = property(get_user_id)
    first_name = property(get_first_name)
    second_name = property(get_second_name)
import requests
from bs4 import BeautifulSoup
from models import DateTime


class DateTimeParser:
    website_url = 'https://time100.ru/index.php'

    def __init__(self):
        self.__current_date_time = self.parse_date_time()
        self.__last_daily_deadlines_part_update = self.__current_date_time

    def parse_date_time(self) -> DateTime:
        print('Start parsing')
        result = ' '
        try:
            result = requests.get(self.website_url)
        except:
            print('Error with parsing time')

        content = BeautifulSoup(result.content, 'lxml')
        time = self.parse_time(content)
        date = self.parse_date(content)
        result = DateTime(time=time, date=date)
        self.__current_date_time = result
        print(self.__current_date_time)
        return result

    def parse_time(self, content: BeautifulSoup):
        content = content.find('h3', class_='display-time monospace')
        content = content.find('span', class_='time').text
        return content

    def parse_date(self, content: BeautifulSoup):
        content = content.find('h3', class_='display-date monospace')
        content = content.find('span', class_='time').text
        content = content.split(':')[1]
        content = FormatConverter.convert_date_format(content)
        return content

    def get_current_date_time(self):
        return self.__current_date_time

    def get_current_date_time_update(self):
        self.__last_daily_deadlines_part_update = self.__current_date_time
        return self.__current_date_time

    def get_last_daily_deadlines_part_update(self):
        return self.__last_daily_deadlines_part_update

    current_date_time = property(get_current_date_time)
    current_date_time_update = property(get_current_date_time_update)
    last_daily_deadlines_part_update = property(get_last_daily_deadlines_part_update)


class FormatConverter:
    months_str_to_num = {
        'января': '01',
        'февраля': '02',
        'марта': '03',
        'апреля': '04',
        'мая': '05',
        'июня': '06',
        'июля': '07',
        'августа': '08',
        'сентября': '09',
        'октября': '10',
        'ноября': '11',
        'декабря': '12',
    }

    @staticmethod
    def convert_date_format(date: str) -> str:
        date = date.strip()
        parts = date.split()
        day = parts[0]
        month = FormatConverter.months_str_to_num[parts[1]]
        year = parts[2]
        return '-'.join([year, month, day])

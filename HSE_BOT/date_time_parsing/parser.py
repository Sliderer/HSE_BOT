import requests
from bs4 import BeautifulSoup


class DateTime:
    def __init__(self, time: str, date: str):
        self.__time = time
        self.__date = date

    def get_time(self):
        return self.__time

    def get_date(self):
        return self.__date

    def __str__(self):
        return f'{self.__date} {self.__time}'

    time = property(get_time)
    date = property(get_date)


class DateTimeParser:
    website_url = 'https://time100.ru/index.php'
    date_time = DateTime(' ', ' ')

    def parse_date_time(self) -> DateTime:
        result = ' '
        try:
            result = requests.get(self.website_url)
        except:
            print('Error with parsing time')

        content = BeautifulSoup(result.content, 'lxml')
        time = self.parse_time(content)
        date = self.parse_date(content)
        result = DateTime(time=time, date=date)
        self.date_time = result
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

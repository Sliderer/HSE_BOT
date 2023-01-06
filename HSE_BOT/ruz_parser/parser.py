from selenium import webdriver
import datetime
from selenium.webdriver.common.by import By
from time import sleep


class Parser:
    web_url = "https://ruz.hse.ru/ruz/main"

    def __init__(self):
        pass

    @staticmethod
    def __get_good_form(lessons):
        ans = ""
        # max_len = 0
        # for lesson in lessons:
        #     max_len = max(max_len, len(max(lesson.values(), key=len)))
        # max_len += 2
        # ans += "+" + "-"*(max_len-2) + "+\n"
        for lesson in lessons:
            name = lesson['name']
            type = lesson['type']
            address = lesson['address']
            professor = lesson['professor']
            time = lesson['time']
            date = lesson['date']
            ans += f'{name}|\n|{time}|\n|{type}|\n|{address}|\n|{professor}|\n|{date}|\n\n'
            ans = ans.replace('|', ' ')
            # ans += "+" + "-" * (max_len - 2) + "+\n"
        return ans

    @staticmethod
    def __month_to_number(month: str):
        if month == 'январь':
            return "01"
        elif month == 'февраль':
            return "02"
        elif month == 'март':
            return "03"
        elif month == 'апрель':
            return "04"
        elif month == 'май':
            return "05"
        elif month == 'июнь':
            return "06"
        elif month == 'июль':
            return "07"
        elif month == 'август':
            return "08"
        elif month == 'сентябрь':
            return "09"
        elif month == 'октябрь':
            return "10"
        elif month == 'ноябрь':
            return "11"
        elif month == 'декабрь':
            return "12"

    def get_lessons(self, full_name: str):

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        browser = webdriver.Chrome(options=options)
        browser.get(self.web_url)

        sleep(1)

        button = browser.find_element(By.XPATH, "//button[@class='btn btn-outline-secondary ng-star-inserted']")
        button.click()

        # sleep(1)

        input = browser.find_element(By.XPATH, "//input[@placeholder='Студент']")
        input.clear()
        input.send_keys(full_name)

        sleep(1)

        get = browser.find_elements(By.XPATH, "//li[@role='option']")[0]
        print(get.text)
        get.click()

        next = browser.find_elements(By.XPATH, "//button[@title='Следующая неделя']")[0]
        next.click()

        sleep(1)

        list = browser.find_elements(By.XPATH, "//div[@class='media item']")
        result = []

        days = browser.find_elements(By.XPATH, "//div[@class='day']")
        months = browser.find_elements(By.XPATH, "//div[@class='month']")
        cur_date_ind = 0
        prev_time = "00:00-00:00"

        for ind, cur in enumerate(list):
            full_name = cur.find_elements(By.XPATH, "//span[@class='ng-star-inserted']")[ind].text
            type = cur.find_elements(By.XPATH, "//div[@class='text-muted kind ng-star-inserted']")[ind].text
            address = cur.find_elements(By.XPATH, "//td")[3 * ind].text
            professor = cur.find_elements(By.XPATH, "//td")[3 * ind + 2].text
            time = str(browser.find_elements(By.XPATH, "//div[@class='time']")[ind].get_attribute("innerHTML"))
            time = time[1:6] + time[12] + time[19:-1]

            if time <= prev_time:
                cur_date_ind += 1
            prev_time = time

            day = days[cur_date_ind].get_attribute("innerHTML")
            if len(day) == 1:
                day = "0" + day
            month = self.__month_to_number(months[cur_date_ind].get_attribute("innerHTML"))
            year = datetime.datetime.now().year
            date = f'{day}.{month}.{year}'

            lesson = {
                'name': full_name,
                'type': type,
                'address': address,
                'professor': professor,
                'time': time,
                'date': date
            }
            result.append(lesson)

        browser.quit()
        return self.__get_good_form(result)

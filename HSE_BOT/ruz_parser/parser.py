from selenium import webdriver
import datetime
from selenium.webdriver.common.by import By
from time import sleep


class Parser:
    web_url = "https://ruz.hse.ru/ruz/main"
    browser = None

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.browser = webdriver.Chrome(options=options)

    def __del__(self):
        self.browser.quit()

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

    month_to_number = {
        'январь': "01",
        'февраль': "02",
        'март': "03",
        'апрель': "04",
        'май': "05",
        'июнь': "06",
        'июль': "07",
        'август': "08",
        'сентябрь': "09",
        'октябрь': "10",
        'ноябрь': "11",
        'декабрь': "12"
    }

    def get_lessons(self, full_name: str):

        self.browser.get(self.web_url)

        while len(self.browser.find_elements(By.XPATH,
                                             "//button[@class='btn btn-outline-secondary ng-star-inserted']")) == 0:
            sleep(0.05)

        button = self.browser.find_element(By.XPATH, "//button[@class='btn btn-outline-secondary ng-star-inserted']")
        button.click()

        input = self.browser.find_element(By.XPATH, "//input[@placeholder='Студент']")
        input.clear()
        input.send_keys(full_name)

        while len(self.browser.find_elements(By.XPATH, "//li[@role='option']")) == 0:
            sleep(0.05)

        get = self.browser.find_element(By.XPATH, "//li[@role='option']")
        print(get.text)
        get.click()

        delta = 0
        while len(self.browser.find_elements(By.XPATH, "//div[@class='media item']")) == 0:
            sleep(0.05)
            delta += 0.01
            if delta >= 3:
                return []

        cnt = len(self.browser.find_elements(By.XPATH, "//div[@class='media item']"))
        result = []

        days = self.browser.find_elements(By.XPATH, "//div[@class='day']")
        months = self.browser.find_elements(By.XPATH, "//div[@class='month']")
        cur_date_ind = 0
        prev_time = "00:00-00:00"

        for ind in range(cnt):
            full_name = self.browser.find_elements(By.XPATH, "//span[@class='ng-star-inserted']")[ind].text
            type = self.browser.find_elements(By.XPATH, "//div[@class='text-muted kind ng-star-inserted']")[ind].text
            address = self.browser.find_elements(By.XPATH, "//td")[3 * ind].text
            professor = self.browser.find_elements(By.XPATH, "//td")[3 * ind + 2].text
            time = str(self.browser.find_elements(By.XPATH, "//div[@class='time']")[ind].get_attribute("innerHTML"))
            time = time[1:6] + time[12] + time[19:-1]

            if time <= prev_time:
                cur_date_ind += 1
            prev_time = time

            day = days[cur_date_ind].get_attribute("innerHTML")
            if len(day) == 1:
                day = "0" + day
            month = self.month_to_number[months[cur_date_ind].get_attribute("innerHTML")]
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

        return self.__get_good_form(result)

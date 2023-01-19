class ScheduleFormatter:

    @staticmethod
    def get_good_form(lessons):
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

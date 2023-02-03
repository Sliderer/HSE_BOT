class DeadlineFormatter:
    @staticmethod
    def get_deadline_text(deadline) -> str:
        return f'{deadline[2]} \n{deadline[3]}'

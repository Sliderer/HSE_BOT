class DeadlineFormatter:
    @staticmethod
    def get_deadline_text(deadline) -> str:
        return f'⚡️You have a deadline!⚡️\n{deadline[2]} \n{deadline[3]}'

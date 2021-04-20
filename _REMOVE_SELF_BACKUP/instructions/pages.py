from datetime import time

from ._builtin import Page


class Instructions(Page):
    pass


class Understanding(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3']

    def q1_error_message(self, value):
        if not value == 50:
            return "Ihre Antwort war nicht korrekt. Überdenken Sie Ihre Antwort erneut."

    def q2_error_message(self, value):
        if not value == 100:
            return "Ihre Antwort war nicht korrekt. Überdenken Sie Ihre Antwort erneut."

    def q3_error_message(self, value):
        if not value == 0:
            return "Ihre Antwort war nicht korrekt. Überdenken Sie Ihre Antwort erneut."

    def before_next_page(self):
        import time
        self.participant.wait_page_arrival = time.time()


page_sequence = [
    Instructions,
    Understanding
]

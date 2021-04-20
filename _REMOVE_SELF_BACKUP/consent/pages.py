from ._builtin import Page


class Introduction(Page):
    pass


class Consent(Page):
    form_model = 'player'
    form_fields = ['consent']

    def consent_error_message(self, value):
        if not value:
            return "Um an der Studie teilzunehmen müssen Sie der Einverständniserklärung zustimmen. " \
                   "Andernfalls schließen Sie das Fenster um die Studie an dieser Stelle zu beenden. " \
                   "Ihre Entlohnung entfällt hierbei jedoch."


page_sequence = [
    Introduction,
    Consent
]

from string import digits
from ._builtin import Page


class IDPage(Page):
    form_model = 'player'
    form_fields = ['DecisionLabId']

    def DecisionLabId_error_message(self, value):
        # Exactly 7 digits
        if len(value) < 7:
            return "Eingabe zu kurz! Die Decision Lab Id sollte genau sieben Stellen haben!"

        # Only digits
        if any([c not in digits for c in value]):
            return "Bitte nur Ziffern eingeben!"

        # Last two digits are the sum of all other digits
        sm = sum([int(c) * (i + 1) for i, c in enumerate(value[0:5])]) % 100
        if not sm == int(value[5:]):
            return "Falsche Decision Lab ID!"

        if value == "0000000":
            return "Fehlerhafe Decision Lab ID!"

    def before_next_page(self):
        self.player.participant.vars["DecisionLabId"] = self.player.DecisionLabId
        self.player.participant.label = self.player.DecisionLabId


page_sequence = [
    IDPage
]

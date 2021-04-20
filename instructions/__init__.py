from otree.api import *

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'EnvyInstructions'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q1 = models.IntegerField(
        choices=[[0, '0 Cent'], [50, '50 Cent'], [100, '100 Cent']], widget=widgets.RadioSelect
    )
    q2 = models.IntegerField(
        choices=[[0, '0 Cent'], [50, '50 Cent'], [100, '100 Cent']], widget=widgets.RadioSelect
    )
    q3 = models.IntegerField(
        choices=[[0, '0 Cent'], [50, '50 Cent'], [100, '100 Cent']], widget=widgets.RadioSelect
    )


# FUNCTIONS
# PAGES
class Instructions(Page):
    pass


class Understanding(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3']

    @staticmethod
    def q1_error_message(player: Player, value):
        if not value == 50:
            return "Ihre Antwort war nicht korrekt. Überdenken Sie Ihre Antwort erneut."

    @staticmethod
    def q2_error_message(player: Player, value):
        if not value == 100:
            return "Ihre Antwort war nicht korrekt. Überdenken Sie Ihre Antwort erneut."

    @staticmethod
    def q3_error_message(player: Player, value):
        if not value == 0:
            return "Ihre Antwort war nicht korrekt. Überdenken Sie Ihre Antwort erneut."

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.participant.wait_page_arrival = time.time()


page_sequence = [Instructions, Understanding]

from otree.api import *
from otree.models import player

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'showup_fee'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class Showup_Fee(Page):

    def vars_for_template(player: Player):
        return dict(role=player.participant.role)


class Hypothetical_Ambivalence(Page):
    form_model = 'player'
    form_fields = [
        'ambivalence1',
        'ambivalence2',
        'ambivalence3',
        'ambivalence4',
        'ambivalence5',
        'ambivalence6',
        'ambivalence7',
        'ambivalence8',
        'ambivalence9',
        'ambivalence10',
    ]


class Debriefing(Page):
    pass


page_sequence = [Showup_Fee, Hypothetical_Ambivalence, Debriefing]

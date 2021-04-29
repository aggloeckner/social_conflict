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


def make_likert_7(label):
    return models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label=label,
        widget=widgets.RadioSelectHorizontal,
    )


class Group(BaseGroup):
    pass


class Player(BasePlayer):
        ambivalence1 = make_likert_7("")
        ambivalence2 = make_likert_7("")
        ambivalence3 = make_likert_7("")
        ambivalence4 = make_likert_7("")
        ambivalence5 = make_likert_7("")
        ambivalence6 = make_likert_7("")
        ambivalence7 = make_likert_7("")
        ambivalence8 = make_likert_7("")
        ambivalence9 = make_likert_7("")
        ambivalence10 = make_likert_7("")


# PAGES
class Showup_Fee(Page):

    def vars_for_template(player: Player):
        return dict(role=player.participant.role)


class TAS(Page):
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


page_sequence = [
    Showup_Fee,
    TAS,
    Debriefing,
]

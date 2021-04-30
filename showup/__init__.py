from otree.api import *
from otree.models import player

c = Currency

doc = """
Your app description
"""

class Constants(BaseConstants):
    name_in_url = 'showup'
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
        amb1 = make_likert_7("")
        amb2 = make_likert_7("")
        amb3 = make_likert_7("")
        amb4 = make_likert_7("")
        amb5 = make_likert_7("")
        amb6 = make_likert_7("")
        amb7 = make_likert_7("")
        amb8 = make_likert_7("")
        amb9 = make_likert_7("")
        amb10 = make_likert_7("")


# PAGES
class Showup(Page):

    def vars_for_template(player: Player):
        return dict(role=player.participant.role)


class TAS(Page):
    form_model = 'player'
    form_fields = [
        'amb1',
        'amb2',
        'amb3',
        'amb4',
        'amb5',
        'amb6',
        'amb7',
        'amb8',
        'amb9',
        'amb10',
    ]


class Debriefing(Page):
    @staticmethod
    def vars_for_template(player: Player):
        p1 = player.group.get_player_by_id(1)
        p2 = player.group.get_player_by_id(2)
        return dict(
            total_earnings=player.participant.payoff_plus_participation_fee()
        )

page_sequence = [
    Showup,
    TAS,
    Debriefing,
]

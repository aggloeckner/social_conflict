from otree.api import *

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'hypothetical'
    players_per_group = None
    num_rounds = 1
    endowment = Currency(100)


class Subsession(BaseSubsession):
    pass


def make_likert(label):
    return models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        label=label,
        widget=widgets.RadioSelectHorizontal,
    )


def make_likert_7(label):
    return models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label=label,
        widget=widgets.RadioSelectHorizontal,
    )


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    offer = models.CurrencyField(min=0, max=Constants.endowment, label="")
    conflicted = make_likert("")
    bad = make_likert("")
    good = make_likert("")
    satisfied = make_likert("")
    regret = make_likert("")
    play_again = make_likert("")
    play_again_other = make_likert("")
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


# FUNCTIONS
def set_payoffs(group: Group):
    p1 = group.get_player_by_id(1)
    p1.payoff = Constants.endowment - p1.offer


# PAGES
class DictatorConflict(Page):
    form_model = 'player'
    form_fields = ['offer', 'conflicted', 'bad', 'good']


class DictatorRegret(Page):
    form_model = 'player'
    form_fields = ['satisfied', 'regret', 'play_again', 'play_again_other']


class Ambivalence(Page):
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
    after_all_players_arrive = 'set_payoffs'

    @staticmethod
    def vars_for_template(player: Player):
        p1 = player.group.get_player_by_id(1)
        p2 = player.group.get_player_by_id(2)
        return dict(
            kept=p1.payoff.to_real_world_currency(player.session),
            total_p1=(200 + p1.payoff).to_real_world_currency(player.session),
        )


page_sequence = [
    DictatorConflict,
    DictatorRegret,
    Ambivalence,
    Debriefing,
]

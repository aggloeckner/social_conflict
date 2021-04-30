from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c
)

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'SoCo'
    players_per_group = 2
    num_rounds = 1
    endowment = c(100)
    dictator_role = 'Dictator'
    recipient_role = 'Recipient'


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


def waiting_too_long(player):
    participant = player.participant

    import time
    # assumes you set wait_page_arrival in PARTICIPANT_FIELDS.
    return time.time() - participant.wait_page_arrival > 5 * 60


class Group(BaseGroup):
    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p1.payoff = Constants.endowment - p1.offer
        p2.payoff = p1.offer


class Player(BasePlayer):
    offer = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label=""
    )
    conflicted = make_likert("")
    bad = make_likert("")
    good = make_likert("")
    satisfied = make_likert("")
    regret = make_likert("")
    play_again = make_likert("")
    play_again_other = make_likert("")
    conflicted_0 = make_likert("")
    conflicted_25 = make_likert("")
    conflicted_50 = make_likert("")
    bad_0 = make_likert("")
    bad_25 = make_likert("")
    bad_50 = make_likert("")
    good_0 = make_likert("")
    good_25 = make_likert("")
    good_50 = make_likert("")
    play_again_0 = make_likert("")
    play_again_25 = make_likert("")
    play_again_50 = make_likert("")
    play_again_other_0 = make_likert("")
    play_again_other_25 = make_likert("")
    play_again_other_50 = make_likert("")
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



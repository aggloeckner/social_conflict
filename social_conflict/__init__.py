from otree.api import *

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'social_conflict'
    players_per_group = 2
    num_rounds = 1
    endowment = Currency(100)
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


# FUNCTIONS
def set_payoffs(group: Group):
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)
    if p1.offer is not None:
        p1.payoff = Constants.endowment - p1.offer
        p2.payoff = p1.offer
    else:
        p1.payoff = -200
        p2.payoff = 200


def waiting_too_long(player):
    participant = player.participant
    import time
    return time.time() - participant.wait_page_arrival > 300


def group_by_arrival_time_method(subsession, waiting_players):
    if len(waiting_players) >= 2:
        p1 = waiting_players[0]
        p2 = waiting_players[1]
        p1.participant.role = 1
        p2.participant.role = 2
        return waiting_players[:2]
    for player in waiting_players:
        if waiting_too_long(player):
            # make a single-player group.
            return [player]


# PAGES
class GroupingWaitPage(WaitPage):
    group_by_arrival_time = True

    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        group = player.group
        if len(group.get_players()) == 1:
            return upcoming_apps[0]

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'body_text': "Sobald die nächste Person eintrifft, geht es los.",
            'title_text': "Bitte warten Sie.",
        }


class DictatorOffer(Page):
    form_model = 'player'
    form_fields = ['offer']

    timeout_seconds = 300

    @staticmethod
    def is_displayed(player: Player):
        return player.role == Constants.dictator_role


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'

    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        if waiting_too_long(player):
            return upcoming_apps[-1]


class DictatorConflict(Page):
    form_model = 'player'
    form_fields = ['conflicted', 'bad', 'good']

    @staticmethod
    def is_displayed(player: Player):
        return player.role == Constants.dictator_role


class DictatorRegret(Page):
    form_model = 'player'
    form_fields = ['satisfied', 'regret', 'play_again', 'play_again_other']

    @staticmethod
    def is_displayed(player: Player):
        return player.role == Constants.dictator_role


class RecipientConflict(Page):
    form_model = 'player'
    form_fields = ['conflicted', 'bad', 'good', 'play_again', 'play_again_other']

    @staticmethod
    def is_displayed(player: Player):
        return player.role == Constants.recipient_role

    @staticmethod
    def vars_for_template(player: Player):
        return dict(kept=Constants.endowment - player.payoff, offer=player.payoff)


class RecipientAlternative0(Page):
    form_model = 'player'
    form_fields = ['conflicted_0', 'bad_0', 'good_0', 'play_again_0', 'play_again_other_0']

    @staticmethod
    def is_displayed(player: Player):
        return player.role == Constants.recipient_role


class RecipientAlternative25(Page):
    form_model = 'player'
    form_fields = ['conflicted_25', 'bad_25', 'good_25', 'play_again_25', 'play_again_other_25']

    @staticmethod
    def is_displayed(player: Player):
        return player.role == Constants.recipient_role


class RecipientAlternative50(Page):
    form_model = 'player'
    form_fields = ['conflicted_50', 'bad_50', 'good_50', 'play_again_50', 'play_again_other_50']

    @staticmethod
    def is_displayed(player: Player):
        return player.role == Constants.recipient_role


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
    @staticmethod
    def vars_for_template(player: Player):
        p1 = player.group.get_player_by_id(1)
        p2 = player.group.get_player_by_id(2)
        return dict(
            kept=p1.payoff.to_real_world_currency(player.session),
            offer=p2.payoff.to_real_world_currency(player.session),
            total_p1=(200 + p1.payoff).to_real_world_currency(player.session),
            total_p2=(200 + p2.payoff).to_real_world_currency(player.session),
        )


page_sequence = [
    GroupingWaitPage,
    DictatorOffer,
    ResultsWaitPage,
    DictatorConflict,
    DictatorRegret,
    RecipientConflict,
    RecipientAlternative0,
    RecipientAlternative25,
    RecipientAlternative50,
    Ambivalence,
    Debriefing,
]

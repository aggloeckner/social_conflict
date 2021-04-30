from otree.api import *

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'SoCO'
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
    confl = make_likert("")
    bad = make_likert("")
    good = make_likert("")
    satisfied = make_likert("")
    regret = make_likert("")
    p_a = make_likert("")
    p_a_o = make_likert("")
    confl_0 = make_likert("")
    confl_25 = make_likert("")
    confl_50 = make_likert("")
    bad_0 = make_likert("")
    bad_25 = make_likert("")
    bad_50 = make_likert("")
    good_0 = make_likert("")
    good_25 = make_likert("")
    good_50 = make_likert("")
    p_a_0 = make_likert("")
    p_a_25 = make_likert("")
    p_a_50 = make_likert("")
    p_a_o_0 = make_likert("")
    p_a_o_25 = make_likert("")
    p_a_o_50 = make_likert("")
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


class PlayerA_Offer(Page):
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


class PlayerA_CBG(Page):
    form_model = 'player'
    form_fields = ['confl', 'bad', 'good']

    @staticmethod
    def is_displayed(player: Player):
        return player.role == Constants.dictator_role


class PlayerA_SRPP(Page):
    form_model = 'player'
    form_fields = ['satisfied', 'regret', 'p_a', 'p_a_o']

    @staticmethod
    def is_displayed(player: Player):
        return player.role == Constants.dictator_role


class PlayerB_CBGPP(Page):
    form_model = 'player'
    form_fields = ['confl', 'bad', 'good', 'p_a', 'p_a_o']

    @staticmethod
    def is_displayed(player: Player):
        return player.role == Constants.recipient_role

    @staticmethod
    def vars_for_template(player: Player):
        return dict(kept=Constants.endowment - player.payoff, offer=player.payoff)


class PlayerB_Alt0(Page):
    form_model = 'player'
    form_fields = ['confl_0', 'bad_0', 'good_0', 'p_a_0', 'p_a_o_0']

    @staticmethod
    def is_displayed(player: Player):
        return player.role == Constants.recipient_role


class PlayerB_Alt25(Page):
    form_model = 'player'
    form_fields = ['confl_25', 'bad_25', 'good_25', 'p_a_25', 'p_a_o_25']

    @staticmethod
    def is_displayed(player: Player):
        return player.role == Constants.recipient_role


class PlayerB_Alt50(Page):
    form_model = 'player'
    form_fields = ['confl_50', 'bad_50', 'good_50', 'p_a_50', 'p_a_o_50']

    @staticmethod
    def is_displayed(player: Player):
        return player.role == Constants.recipient_role


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
        kept=p1.payoff.to_real_world_currency(player.session),
        offer=p2.payoff.to_real_world_currency(player.session),
        total_earnings=player.participant.payoff_plus_participation_fee()
        )


page_sequence = [
    GroupingWaitPage,
    PlayerA_Offer,
    ResultsWaitPage,
    PlayerA_CBG,
    PlayerA_SRPP,
    PlayerB_CBGPP,
    PlayerB_Alt0,
    PlayerB_Alt25,
    PlayerB_Alt50,
    TAS,
    Debriefing,
]

from ._builtin import Page, WaitPage
from .models import Constants


class DictatorConflict(Page):
    form_model = 'player'
    form_fields = ['offer', 'conflicted', 'bad', 'good']

    def is_displayed(self):
        return self.player.role == Constants.dictator_role


class GroupingWaitPage(WaitPage):
    group_by_arrival_time = True

    def vars_for_template(self):
        return {'body_text': "Sobald die nächste Person eintrifft, geht es los.",
                'title_text': "Bitte warten Sie."}


class DictatorRegret(Page):
    form_model = 'player'
    form_fields = ['satisfied', 'regret', 'play_again', 'play_again_other']

    def is_displayed(self):
        return self.player.role == Constants.dictator_role


class RecipientConflict(Page):
    form_model = 'player'
    form_fields = ['conflicted', 'bad', 'good', 'play_again', 'play_again_other']

    def is_displayed(self):
        return self.player.role == Constants.recipient_role

    def vars_for_template(self):
        return dict(kept=Constants.endowment - self.player.payoff,
                    offer=self.player.payoff)


class RecipientAlternative0(Page):

    form_model = 'player'
    form_fields = ['conflicted_0', 'bad_0', 'good_0', 'play_again_0', 'play_again_other_0']

    def is_displayed(self):
        return self.player.role == Constants.recipient_role


class RecipientAlternative25(Page):

    form_model = 'player'
    form_fields = ['conflicted_25', 'bad_25', 'good_25', 'play_again_25', 'play_again_other_25']

    def is_displayed(self):
        return self.player.role == Constants.recipient_role


class RecipientAlternative50(Page):

    form_model = 'player'
    form_fields = ['conflicted_50', 'bad_50', 'good_50', 'play_again_50', 'play_again_other_50']

    def is_displayed(self):
        return self.player.role == Constants.recipient_role


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'

    def is_displayed(self):
        return self.player.role == Constants.recipient_role


class Ambivalence(Page):
    form_model = 'player'
    form_fields = ['ambivalence1', 'ambivalence2', 'ambivalence3', 'ambivalence4', 'ambivalence5', 'ambivalence6',
                   'ambivalence7', 'ambivalence8', 'ambivalence9', 'ambivalence10']


class Debriefing(Page):

    def vars_for_template(self):
        p1 = self.group.get_player_by_id(1)
        p2 = self.group.get_player_by_id(2)
        return dict(kept=p1.payoff.to_real_world_currency(self.session),
                    offer=p2.payoff.to_real_world_currency(self.session),
                    total_p1=(200+p1.payoff).to_real_world_currency(self.session),
                    total_p2=(200+p2.payoff).to_real_world_currency(self.session))


page_sequence = [
    DictatorConflict,
    GroupingWaitPage,
    ResultsWaitPage,
    DictatorRegret,
    RecipientConflict,
    RecipientAlternative0,
    RecipientAlternative25,
    RecipientAlternative50,
    Ambivalence,
    Debriefing
]

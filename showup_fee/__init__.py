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
        p1 = player.group.get_player_by_id(1)
        p2 = player.group.get_player_by_id(2)
        return dict(
            total_p1=0,
            total_p2=200,
        )

page_sequence = [Showup_Fee]

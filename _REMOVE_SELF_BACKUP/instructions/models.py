from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer
)

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
        choices=[
            [0, '0 Cent'],
            [50, '50 Cent'],
            [100, '100 Cent']
        ],
        widget=widgets.RadioSelect
    )
    q2 = models.IntegerField(
        choices=[
            [0, '0 Cent'],
            [50, '50 Cent'],
            [100, '100 Cent']
        ],
        widget=widgets.RadioSelect
    )
    q3 = models.IntegerField(
        choices=[
            [0, '0 Cent'],
            [50, '50 Cent'],
            [100, '100 Cent']
        ],
        widget=widgets.RadioSelect
    )

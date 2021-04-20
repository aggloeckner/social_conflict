from otree.api import (
    models,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer
)

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'LabIDs'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    DecisionLabId = models.CharField(max_length=7)

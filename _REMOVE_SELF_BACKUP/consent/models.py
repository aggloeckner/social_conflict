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
    name_in_url = 'consent'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.BooleanField(
        choices=[
            [True, 'Ja, ich bin damit einverstanden.'],
            [False, 'Nein, ich bin damit nicht einverstanden.']
        ],
        widget=widgets.RadioSelect,
        label=""
    )

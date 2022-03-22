from patterns.template_method.human.daniel import Daniel
from patterns.template_method.human.sylwia import Sylwia
from patterns.template_method.types.environment import Environment
from patterns.template_method.types.health import Health
from patterns.template_method.types.little_shits import LittleShits


def test_sylwia_is_doing_great_when_little_shits_are_quiet():
    human = Sylwia(environment=Environment(little_shits=LittleShits.QUIET))
    human.live_for(weeks=10)
    assert human.mental_health == Health(100)


def test_daniel_is_doing_great_when_little_shits_are_quiet():
    human = Daniel(environment=Environment(little_shits=LittleShits.QUIET))
    human.live_for(weeks=10)
    assert human.mental_health == Health(100)

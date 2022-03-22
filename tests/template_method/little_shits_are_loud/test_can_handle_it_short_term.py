from patterns.template_method.daniel import Daniel
from patterns.template_method.environment import Environment
from patterns.template_method.health import Health
from patterns.template_method.little_shits import LittleShits
from patterns.template_method.sylwia import Sylwia


def test_daniel_does_not_care_when_little_shits_are_loud():
    human = Daniel(environment=Environment(little_shits=LittleShits.LOUD))
    human.live_for(weeks=2)
    assert human.mental_health == Health(100)


def test_sylwia_is_dying_inside_when_little_shits_are_loud():
    human = Sylwia(environment=Environment(little_shits=LittleShits.LOUD))
    human.live_for(weeks=2)
    assert human.mental_health > Health(0)
    assert human.mental_health < Health(100)

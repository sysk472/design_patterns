from patterns.template_method.human.sylwia import Sylwia
from patterns.template_method.types.environment import Environment
from patterns.template_method.types.health import Health
from patterns.template_method.types.little_shits import LittleShits


def test_sylwia_poisons_little_shits_and_life_is_good_again():
    human = Sylwia(environment=Environment(little_shits=LittleShits.LOUD))
    human.live_for(weeks=10)
    assert human.mental_health == Health(100)
    assert human.environment.little_shits == LittleShits.DEAD

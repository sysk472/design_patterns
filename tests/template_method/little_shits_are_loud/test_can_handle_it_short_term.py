from patterns.template_method.human.daniel import Daniel
from patterns.template_method.human.sylwia import Sylwia
from patterns.template_method.types.environment import Environment
from patterns.template_method.types.health import Health


def test_daniel_does_not_care_when_little_shits_are_loud_he_just_sleeps_it_off(
    loud_environment: Environment,
):
    human = Daniel(environment=loud_environment)
    human.live_for(weeks=2)
    assert human.mental_health == Health(100)


def test_sylwia_is_dying_inside_when_little_shits_are_loud(
    loud_environment: Environment,
):
    human = Sylwia(environment=loud_environment)
    human.live_for(weeks=2)
    assert human.mental_health > Health(0)
    assert human.mental_health < Health(100)

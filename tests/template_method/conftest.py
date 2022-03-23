import pytest

from patterns.template_method.types.environment import Environment
from patterns.template_method.types.little_shits import LittleShits


@pytest.fixture()
def quiet_environment() -> Environment:
    return Environment(little_shits=LittleShits.QUIET)


@pytest.fixture()
def loud_environment() -> Environment:
    return Environment(little_shits=LittleShits.LOUD)

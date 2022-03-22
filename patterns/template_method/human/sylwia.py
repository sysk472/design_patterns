from typing import Dict

from patterns.template_method.human.human import Human
from patterns.template_method.types.little_shits import LittleShits


class Sylwia(Human):
    @property
    def fatigue_modifiers(self) -> Dict[LittleShits, int]:
        return {
            LittleShits.QUIET: 1,
            LittleShits.LOUD: 2,
            LittleShits.DEAD: 0,
        }

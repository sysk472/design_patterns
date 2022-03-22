from patterns.template_method.human import Human
from patterns.template_method.little_shits import LittleShits


class Sylwia(Human):
    def work(self, hours: int = 8) -> None:
        fatigue_modifiers = {
            LittleShits.QUIET: 1,
            LittleShits.LOUD: 2,
            LittleShits.DEAD: 0,
        }
        fatigue_modifier = fatigue_modifiers[self.environment.little_shits]
        self.mental_health.decrement(fatigue_modifier * hours)

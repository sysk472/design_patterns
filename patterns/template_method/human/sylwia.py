from patterns.template_method.human.human import Human
from patterns.template_method.types.little_shits import LittleShits


class Sylwia(Human):
    def _sleep(self, hours: int = 8) -> None:
        self.mental_health.get_better(hours)

    def _work(self, hours: int = 8) -> None:
        fatigue_modifiers = {
            LittleShits.QUIET: 1,
            LittleShits.LOUD: 2,
            LittleShits.DEAD: 0,
        }
        fatigue_modifier = fatigue_modifiers[self.environment.little_shits]
        self.mental_health.get_worse(hours * (1 + fatigue_modifier))

    def _rest(self, hours: int = 8) -> None:
        self.mental_health.get_better(hours // 5)

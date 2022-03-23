from typing import Dict

from patterns.template_method.types.environment import Environment
from patterns.template_method.types.health import Health
from patterns.template_method.types.little_shits import LittleShits


class Human:
    def __init__(
        self,
        environment: Environment,
        health: Health = None,
        insanity_threshold: Health = None,
    ) -> None:
        self.environment = environment
        self.mental_health = health if health is not None else Health(100)
        self.insanity_threshold = (
            insanity_threshold if insanity_threshold is not None else Health(30)
        )

    def live_for(self, weeks: int) -> None:
        for _ in range(weeks):
            for _ in range(5):
                self._weekday()
                self._consider_poisoning_those_fucking_little_shits()
            for _ in range(2):
                self._weekend()
                self._consider_poisoning_those_fucking_little_shits()

    @property
    def fatigue_modifiers(self) -> Dict[LittleShits, int]:
        return {
            LittleShits.QUIET: 0,
            LittleShits.LOUD: 1,
            LittleShits.DEAD: 0,
        }

    def sleep(self, hours: int = 8) -> None:
        self.mental_health.get_better(hours)

    def work(self, hours: int = 8) -> None:
        self.mental_health.get_worse(
            hours * (1 + self.fatigue_modifiers[self.environment.little_shits])
        )

    def rest(self, hours: int = 8) -> None:
        self.mental_health.get_better(hours // 5)

    def _weekday(self) -> None:
        self.work()
        self.rest()
        self.sleep()

    def _weekend(self) -> None:
        self.rest(hours=16)
        self.sleep()

    def _consider_poisoning_those_fucking_little_shits(self) -> None:
        if self.mental_health < self.insanity_threshold:
            self.environment.little_shits = LittleShits.DEAD

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

    def sleep(self, hours: int = 8) -> None:
        self.mental_health.increment(hours)

    def work(self, hours: int = 8) -> None:
        self.mental_health.decrement(
            hours * (1 + self.fatigue_modifiers[self.environment.little_shits])
        )

    @property
    def fatigue_modifiers(self) -> Dict[LittleShits, int]:
        return {
            LittleShits.QUIET: 0,
            LittleShits.LOUD: 1,
            LittleShits.DEAD: 0,
        }

    def leisure(self, hours: int = 8) -> None:
        self.mental_health.increment(hours // 5)

    def weekday(self) -> None:
        self.work()
        self.leisure()
        self.sleep()
        if self.mental_health < self.insanity_threshold:
            self.poison_those_fucking_little_shits()

    def weekend(self) -> None:
        self.leisure(hours=16)
        self.sleep()
        if self.mental_health < self.insanity_threshold:
            self.poison_those_fucking_little_shits()

    def live_for(self, weeks: int) -> None:
        for _ in range(weeks):
            for _ in range(5):
                self.weekday()
            for _ in range(2):
                self.weekend()

    def poison_those_fucking_little_shits(self) -> None:
        self.environment.little_shits = LittleShits.DEAD

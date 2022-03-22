from patterns.template_method.environment import Environment
from patterns.template_method.health import Health
from patterns.template_method.little_shits import LittleShits


class Human:
    def __init__(
        self,
        environment: Environment,
        health: Health = None,
        insanity_threshold: Health = None,
    ) -> None:
        self.environment = environment
        if health is None:
            health = Health(100)
        self.mental_health = health
        if insanity_threshold is None:
            insanity_threshold = Health(30)
        self.insanity_threshold = insanity_threshold

    def sleep(self, hours: int = 8) -> None:
        self.mental_health.increment(hours)

    def work(self, hours: int = 8) -> None:
        self.mental_health.decrement(hours)

    def leisure(self, hours: int = 8) -> None:
        pass

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

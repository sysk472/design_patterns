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
                self.__weekday()
                self.__consider_poisoning_those_fucking_little_shits()
            for _ in range(2):
                self.__weekend()
                self.__consider_poisoning_those_fucking_little_shits()

    def _sleep(self, hours: int = 8) -> None:
        raise NotImplementedError

    def _work(self, hours: int = 8) -> None:
        raise NotImplementedError

    def _rest(self, hours: int = 8) -> None:
        raise NotImplementedError

    def __weekday(self) -> None:
        self._work()
        self._rest()
        self._sleep()

    def __weekend(self) -> None:
        self._rest(hours=16)
        self._sleep()

    def __consider_poisoning_those_fucking_little_shits(self) -> None:
        if self.mental_health < self.insanity_threshold:
            self.environment.little_shits = LittleShits.DEAD

from patterns.template_method.human.human import Human


class Daniel(Human):
    def _sleep(self, hours: int = 10) -> None:
        self.mental_health.get_better(hours)

    def _rest(self, hours: int = 8) -> None:
        self.mental_health.get_better(hours // 5)
        self.__go_to_toilet(minutes=30)

    def __go_to_toilet(self, minutes: int):
        self.mental_health.get_better(minutes // 30)

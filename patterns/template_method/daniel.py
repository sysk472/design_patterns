from patterns.template_method.human import Human


class Daniel(Human):
    def sleep(self, hours: int = 10) -> None:
        self.mental_health.increment(hours)

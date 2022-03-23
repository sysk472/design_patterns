class Health:
    def __init__(self, percentage: int) -> None:
        self.percentage = percentage

    def get_better(self, percentage: int) -> None:
        self.percentage = min([self.percentage + percentage, 100])

    def get_worse(self, percentage: int) -> None:
        self.percentage = max([self.percentage - percentage, 0])

    def __eq__(self, other) -> bool:
        return self.percentage == other.percentage

    def __gt__(self, other):
        return self.percentage > other.percentage

    def __lt__(self, other):
        return self.percentage < other.percentage

    def __repr__(self):
        return f"Health({self.percentage})"

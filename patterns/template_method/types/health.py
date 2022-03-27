class Health:
    def __init__(self, percentage: int) -> None:
        self._percentage = percentage

    def get_better(self, percentage: int) -> None:
        self._percentage = min([self._percentage + percentage, 100])

    def get_worse(self, percentage: int) -> None:
        self._percentage = max([self._percentage - percentage, 0])

    def __eq__(self, other: "Health") -> bool:
        return self._percentage == other._percentage

    def __gt__(self, other: "Health"):
        return self._percentage > other._percentage

    def __lt__(self, other: "Health"):
        return self._percentage < other._percentage

    def __repr__(self):
        return f"Health({self._percentage})"

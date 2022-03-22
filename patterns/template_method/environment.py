from patterns.template_method.little_shits import LittleShits


class Environment:
    def __init__(self, little_shits: LittleShits) -> None:
        self.little_shits = little_shits

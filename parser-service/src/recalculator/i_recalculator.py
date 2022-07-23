class IRecalculator:
    def get(self) -> dict[str: list[tuple]]:
        raise NotImplementedError()

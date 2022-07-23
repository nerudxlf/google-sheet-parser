from src.recalculator.a_recalculator import ARecalculator
from src.recalculator.i_recalculator import IRecalculator


class Recalculator(IRecalculator, ARecalculator):
    def get(self) -> dict[str: list[tuple]]:
        return {'data': self.calculator()}

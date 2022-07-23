class ARecalculator:
    def __init__(self, data: dict, value: str):
        self.values: list[list] = data.get('values')
        self.value: int = int(value.replace(',', ''))

    def calculator(self) -> list[tuple]:
        rows = [('№', 'заказ №', 'стоимость,$', 'стоимость, Р' 'срок поставки')]
        for row in self.values[1:]:
            rub = str(int(row[2]) * self.value / 10000)
            rows.append((row[0], row[1], row[2], rub, row[3]))
        return rows

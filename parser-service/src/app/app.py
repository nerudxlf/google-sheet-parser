import logging
from time import sleep

import requests

from src.app.iapp import IApp
from src.currency.currency import Currency
from src.currency.i_currency import ICurrency
from src.parser.i_parser import IParser
from src.parser.parser import Parser
from src.recalculator.i_recalculator import IRecalculator
from src.recalculator.recalculator import Recalculator


class App(IApp):
    def __init__(self, id: str, scopes: list[str], secret: str = "secret.json"):
        self.id = id
        self.scopes = scopes
        self.secret = secret

    def run(self, table_range: str, money: str, api_path: str, service: str):
        gs: IParser = Parser(spreadsheet_id=self.id, scopes=self.scopes, secret=self.secret)
        currency: ICurrency = Currency(api_path)
        logging.basicConfig(filename="sample.log", level=logging.INFO)
        while True:
            sleep(5)
            data = gs.get(table_range)
            value = currency.read(money)
            re_calc: IRecalculator = Recalculator(data, value)
            new_data = re_calc.get()
            try:
                send_msg = requests.post(  # Send JSON-RPC request with data
                    service,
                    json={"jsonrpc": "2.0", "method": "data", "params": [new_data], "id": 1},
                    headers={'Content-Type': 'application/json;charset=UTF-8'}
                )
                if send_msg.status_code == 404:
                    logging.error(f"{service} Not Found")
            except requests.exceptions.ConnectionError:
                logging.error(f"{service} Connection Error")

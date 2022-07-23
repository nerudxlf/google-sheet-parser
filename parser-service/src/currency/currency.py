import requests
import xml.etree.ElementTree as ET

from src.currency.a_currency import ACurrency
from src.currency.i_currency import ICurrency


class Currency(ICurrency, ACurrency):
    """
    Class to get currency value
    """
    def read(self, valute_id: str) -> str:
        """

        :param valute_id: currency id from the central bank website
        :return: currency value
        """
        req = requests.get(self.url)
        if req.status_code == 200:
            data = req.content
        else:
            raise Exception()
        xml = ET.fromstring(data)
        for item in xml:
            if item.attrib.get('ID') == valute_id:
                value = item.find('Value').text
                break
        else:
            raise Exception()
        return value

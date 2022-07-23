from src.parser.a_parser import AParser
from src.parser.i_parser import IParser


class Parser(IParser, AParser):
    """
    Class for parsing datasheet
    """
    def get(self, list_range: str):
        """

        :param list_range: Range to get data
        :return: data from google sheet
        """
        sheet = self.service.spreadsheets()
        result = sheet.values().get(spreadsheetId=self.spreadsheet_id, range=list_range)
        return result.execute()
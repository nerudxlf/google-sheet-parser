from src.database.repositories.i_repo import IRepo
from src.database.repositories.postgres import PostgreSQL


class DB:
    """
    Factory method
    """
    @staticmethod
    def postgres(root: str, password: str, host: str, port: str, name: str) -> IRepo:
        """

        :param root: db root
        :param password: db password
        :param host: db host
        :param port: db port
        :param name: db name
        :return: Interface for working with DB
        """
        return PostgreSQL(root, password, host, port, name)

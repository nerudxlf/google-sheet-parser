from src.database.repositories.i_repo import IRepo
from src.database.repositories.postgres import PostgreSQL


class DB:
    @staticmethod
    def postgres(root: str, password: str, host: str, port: str, name: str) -> IRepo:
        return PostgreSQL(root, password, host, port, name)

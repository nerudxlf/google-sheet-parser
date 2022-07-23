from typing import Generator

import sqlalchemy as _sql
import sqlalchemy.orm as _orm

from src.database.repositories.i_repo import IRepo


class PostgreSQL(IRepo):
    def __init__(self, root: str, password: str, host: str, port: str, name: str):
        self.root: str = root
        self.password: str = password
        self.host: str = host
        self.port: str = port
        self.name: str = name

    def connect(self) -> Generator:
        url: str = f"postgresql+psycopg2://{self.root}:{self.password}@{self.host}:{self.port}/{self.name}"
        engine = _sql.create_engine(url)
        session = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)
        try:
            yield session()
        finally:
            session().close()

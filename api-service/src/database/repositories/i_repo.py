from typing import Generator


class IRepo:
    def connect(self) -> Generator:
        raise NotImplementedError()
from dataclasses import dataclass


@dataclass
class Data:
    def __init__(self, data: str, ip: int) -> None:
        self.data = data
        self.ip = ip

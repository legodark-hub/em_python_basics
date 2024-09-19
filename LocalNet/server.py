from typing import List

from data import Data


class Server:

    _id_counter = 0

    def __init__(self) -> None:
        from router import Router

        self.buffer: List[Data] = []
        __class__._id_counter += 1
        self.ip: int = __class__._id_counter
        self.linked_router: Router = Router()

    def send_data(self, data) -> None:
        self.linked_router.buffer.append(data)

    def get_data(self) -> list:
        res = self.buffer.copy()
        self.buffer = []
        return res

    def get_ip(self) -> int:
        return self.ip

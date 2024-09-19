from server import Server
from typing import Dict, List

from data import Data


class Router:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            self = super().__new__(cls)
            self.buffer: List[Data] = []
            self.links: Dict[int, Server] = {}
            cls._instance = self
        return cls._instance
    
    # def __init__(self) -> None:
    #     self.buffer: List[Data] = []
    #     self.links: Dict[int, Server] = {}

    def link(self, server: Server) -> None:
        self.links[server.get_ip()] = server

    def unlink(self, server: Server) -> None:
        if server.get_ip() in self.links:
            del self.links[server.get_ip()]

    def send_data(self) -> None:
        for data in self.buffer:
            if data.ip in self.links:
                self.links[data.ip].buffer.append(data)
        self.buffer = []            

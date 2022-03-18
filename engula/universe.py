from engula.v1 import universe_pb2
from engula.client import Client
from engula.database import Database


class Universe:
    def __init__(self, url):
        self.client = Client(url)

    def create_database(self, name):
        create_database = universe_pb2.CreateDatabaseRequest(name=name)
        req = universe_pb2.UniverseRequest(
            create_database=create_database)
        self.client.universe(req)
        return Database(name, self.client)

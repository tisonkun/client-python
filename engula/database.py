from engula.v1 import universe_pb2
from engula.collection import Collection


class Database:
    def __init__(self, name, client):
        self.name = name
        self.client = client

    def desc(self):
        describe_database = universe_pb2.DescribeDatabaseRequest(
            name=self.name)
        req = universe_pb2.UniverseRequest(
            describe_database=describe_database)
        res = self.client.universe(req)
        return res.describe_database.desc

    def create_collection(self, name):
        create_collection = universe_pb2.CreateCollectionRequest(
            name=name, dbname=self.name)
        req = universe_pb2.UniverseRequest(
            create_collection=create_collection)
        self.client.universe(req)
        return Collection(name, self.name, self.client)

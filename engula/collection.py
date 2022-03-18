from engula.v1 import universe_pb2


class Collection:
    def __init__(self, name, dbname, client):
        self.name = name
        self.dbname = dbname
        self.client = client

    def desc(self):
        describe_collection = universe_pb2.DescribeCollectionRequest(
            name=self.name, dbname=self.dbname)
        req = universe_pb2.UniverseRequest(
            describe_collection=describe_collection)
        res = self.client.universe(req)
        return res.describe_collection.desc

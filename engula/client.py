import grpc
from engula.v1 import engula_pb2
from engula.v1 import engula_pb2_grpc


class Client:
    def __init__(self, url):
        chan = grpc.insecure_channel(url)
        self.stub = engula_pb2_grpc.EngulaStub(chan)

    def universe(self, universe):
        req = engula_pb2.BatchRequest()
        req.universes.append(universe)
        res = self.stub.Batch(req)
        return res.universes[0]

    def database(self, database):
        req = engula_pb2.BatchRequest()
        req.databases.append(database)
        res = self.stub.Batch(req)
        return res.databases[0]

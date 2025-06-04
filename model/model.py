import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._stores = []
        self._grafo = nx.DiGraph()
        pass


    def getStores(self):
        self._stores = DAO.getStores()
        return self._stores

    def addNodes(self, store_id):
        self._nodes = DAO.getOrders(store_id)
        self._grafo.add_nodes_from(self._nodes)
        print(f"{len(self._nodes)} nodi aggiunti")


    def addEdges(self, k):

        pass
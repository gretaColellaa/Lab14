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


    def addEdges(self, k, store_id):
        print("addEdges chiamata")
        print(store_id)

        listaEdgesId = DAO.getEdges(k, store_id)

        listaEdges = []

        for c in listaEdgesId:

            o1 = self.getOrder_from_id(c[0])
            o2 = self.getOrder_from_id(c[1])
            weight = c[2]

            listaEdges.append((o1,o2, weight))

        self._grafo.add_edges_from(listaEdges)

        print(f"{self._grafo.number_of_edges()} archi aggiunti")



    def getOrder_from_id(self, id):

        for o in self._nodes:
            if o.order_id == id:
                return o

    def get_num_of_nodes(self):
        return self._grafo.number_of_nodes()

    def get_num_of_edges(self):
        return self._grafo.number_of_edges()

    def get_nodes(self):
        return self._nodes



    def cammino_piu_lungo(self, s):

        source = self.getOrder_from_id(s)
        # Ordinamento topologico - L'ordinamento topologico è una sequenza dei nodi
        # che rispetta le dipendenze tra di essi.
        topo = list(nx.topological_sort(self._grafo))

        # Inizializza: lunghezza 1 (solo il nodo di partenza)
        dist = {n: 1 if n == source else float('-inf') for n in self._grafo.nodes()}
        pred = {n: None for n in self._grafo.nodes()}

        for u in topo:
           # print(f"Esamino nodo: {u.order_id}, dist[u]={dist[u]}")
            for v in self._grafo.successors(u):
                #print(f" → Successore: {v.order_id}, dist[v]={dist[v]}")
                if dist[v] < dist[u] + 1:
                    #print(f"   ✅ Aggiorno dist[{v.order_id}] = {dist[u] + 1}, pred[{v.order_id}] = {u.order_id}")
                    dist[v] = dist[u] + 1
                    pred[v] = u

                    # in pratica aggiorno il predeccessore ogni volta che la distanza
                    #è maggiore di quella che avevo slavato dai predecessori visti prima

        # Nodo più distante in termini di nodi
        end_node = max(dist, key=dist.get) #nodo con dist massima
        max_len = dist[end_node]

        #cammino
        path = []
        current = end_node

        #creo una lista partendo dall'ultimo nodo (current = end_node)
        while current is not None:
            path.append(current)
            current = pred[current] #aggiorno il corrente con il predecessore
            print(current)
        path.reverse() #rigiro la lista per averla dal primo all'ultimo

        print(len(path))
        return path


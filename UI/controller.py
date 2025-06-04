import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._listStores = []



    def handleCreaGrafo(self, e):
        k_giorni = self._view._txtIntK.value
        store_name = self._view._ddStore.value
        try:
            int(k_giorni)
        except:
            self._view.create_alert("Inserire un valore valido")


        store_id = 0
        for s in self._listStores:
            if s.store_name == store_name:
                store_id = s.store_id

        self._model.addNodes(store_id)
        self._model.addEdges(k_giorni, store_id)

        self._view.txt_result.clean()
        self._view.txt_result.controls.append(ft.Text(f" il grafo ha {self._model.get_num_of_nodes()} nodi"
                                                      f" e {self._model.get_num_of_edges()} archi"))

        self.fillDDnodi()

        self._view.update_page()


    def handleCerca(self, e):
        source = self._view._ddNode.value
        path = self._model.cammino_piu_lungo(source)
        self._view.txt_result.controls.append(ft.Text(f"Nodo di partenza: {source}"))
        for n in path:
            self._view.txt_result.controls.append(ft.Text(f"{n.order_id}"))

        self._view.update_page()

    def handleRicorsione(self, e):
        pass


    def fillDD(self):
        for s in self._model.getStores():
            self._listStores.append(s)
            self._view._ddStore.options.append(ft.dropdown.Option(s.store_name))

        self._view.update_page()

    def fillDDnodi(self):
        for o in self._model.get_nodes():

            self._view._ddNode.options.append(ft.dropdown.Option(o.order_id))








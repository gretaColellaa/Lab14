import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._listStores = []



    def handleCreaGrafo(self, e):
        store_name = self._view._ddStore.value
        store_id = 0
        for s in self._listStores:
            if s.store_name == store_name:
                store_id = s.store_id

        self._model.addNodes(store_id)


        k_giorni = self._view._txtIntK.value
        self._model.addEdges(k_giorni)


    def handleCerca(self, e):
        pass

    def handleRicorsione(self, e):
        pass


    def fillDD(self):
        for s in self._model.getStores():
            self._listStores.append(s)
            self._view._ddStore.options.append(ft.dropdown.Option(s.store_name))

        self._view.update_page()






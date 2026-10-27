import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    def mostra(self, e):
        strumenti = self._model.get_strumenti() # Recupero tutti gli strumenti.
        if strumenti is None: # Controllo se il recupero è fallito.
            self._view.show_alert("Errore nel recupero degli strumenti")
            return
        self._view.lista_strumenti.controls.clear() # Svuoto la lista per evitare duplicati.
        for strumento in strumenti: # Aggiungo gli strumenti alla lista.
            self._view.lista_strumenti.controls.append(ft.Text(str(strumento)))
        self._view.update()

    def cerca(self, e):
        tipo = self._view.input_tipo_strumento.value # Leggo ciò che viene scritto nel campo di ricerca.
        if not tipo: # Controllo sull'inserimento.
            self._view.show_alert("Inserisci il tipo di strumento da cercare")
            return
        strumenti = self._model.cerca_strumenti_per_tipo(tipo) # Interrogo il database usando il tipo inserito.
        if strumenti is None:
            self._view.show_alert("Errore nel recupero degli strumenti")
            return
        self._view.lista_strumenti_ricerca.controls.clear()  # Svuoto la lista per evitare duplicati.
        for strumento in strumenti:  # Aggiungo gli strumenti alla lista.
            self._view.lista_strumenti_ricerca.controls.append(ft.Text(str(strumento)))
        self._view.update()

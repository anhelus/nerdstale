from abc import ABC


class Equipaggiamento(ABC):

    def __init__(self, nome):
        self.nome = nome


class Oggetto(Equipaggiamento):

    def __init__(self, nome, descrizione):
        super().__init__(nome)
        self.descrizione = descrizione


class Pozione(Oggetto):

    def __init__(self, nome, descrizione, salute_curata):
        super().__init__(nome, descrizione)
        self.salute_curata = salute_curata


class Armatura(Equipaggiamento):

    def __init__(self, nome, danno_assorbito):
        super().__init__(nome)
        self.danno_assorbito = danno_assorbito


class Arma(Equipaggiamento):

    def __init__(self, nome, danno_inflitto):
        super().__init__(nome)
        self.danno_inflitto = danno_inflitto


class Inventario():

    def __init__(self, oggetti):
        self.oggetti = oggetti
    
    def aggiungi_oggetto(self, oggetto, quantita):
        for _ in range(quantita):
            self.oggetti.append(oggetto)
    
    def rimuovi_oggetto(self, oggetto, quantita):
        for _ in range(quantita):
            self.oggetti.rimuovi(oggetto)
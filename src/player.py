from abc import ABC
from .equipment import Inventario


class Statistiche():

    def __init__(self, forza, difesa, agilita):
        self.forza = forza
        self.difesa = difesa
        self.agilita = agilita


class Personaggio(ABC):

    def __init__(
            self,
            nome: str,
            salute_massima: int,
            statistiche: Statistiche):
        self.nome = nome
        self.salute_massima = salute_massima
        self.salute_attuale = salute_massima
        self.statistiche = statistiche
    
    def controlla_salute(self):
        if self.salute_attuale <= 0:
            print(f'{self.nome} muore!')
            return False
        elif self.salute_attuale > self.salute_massima:
            self.salute_attuale = self.salute_massima
        return True

    def fai_danno(self,
            quantita_danno: int,
            nemico: 'PersonaggioNemico'):
        print(f'{self.nome} colpisce {nemico.nome}!')
        nemico.salute_attuale = nemico.salute_attuale - quantita_danno
        return nemico.controlla_salute()

    def subisci_danno(self, quantita_danno):
        self.salute_attuale = self.salute_attuale - quantita_danno
        return self.controlla_salute()

    def cura(self, quantita_salute):
        print(f'{self.nome} si cura di {quantita_salute}!')
        self.salute_attuale = self.salute_attuale + quantita_salute
    
    def __str__(self):
        return f'{self.nome} - HP: {self.salute_attuale}/{self.salute_massima}'


class PersonaggioNemico(Personaggio):
    pass


class PersonaggioGiocatore(Personaggio):
    def __init__(
            self,
            nome,
            salute_massima,
            statistiche,
            inventario: Inventario):
        super().__init__(nome, salute_massima, statistiche)
        self.inventario = inventario
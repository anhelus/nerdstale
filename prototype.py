from src.player import PersonaggioGiocatore, PersonaggioNemico


print('Simulazione di un combattimento tra giocatore e nemico...')
print('Creo personaggio giocatore')
print('Creo personaggio nemico')
giocatore = PersonaggioGiocatore('ciccio', 120, 120, 120)
nemico = PersonaggioNemico('stronzo', 120, 120)
print(giocatore)
print(nemico)

cond = True
counter = 1
while cond:
    print(f'Turno {counter}')
    cond = giocatore.fai_danno(10, nemico)
    print(giocatore)
    print(nemico)

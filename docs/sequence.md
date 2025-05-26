## Diagramma di sequenza per il caso d'uso "Gestione combattimento"

1. Si determinano i partecipanti al diagramma di sequenza.
2. Si stabiliscono la prima parte del flusso. In particolare:
    a. Il client rileva la collisione tra sprite del personaggio e del nemico.
    b. Se ciò avviene, si scatena il combattimento, ed il controllo passa al gestore del combattimento. Contestualmente, viene mostrata l'interfaccia di combattimento.
3. Si entra nel loop di combattimento, che dura finché questo è attivo.
4. Viene controllato il turno.
    a. Se è il turno del giocatore, il giocatore sceglie l'azione dall'UI, il sistema calcola il risultato, l'UI viene aggiornata, ed il turno termina.
    b. Se è il turno del nemico, l'IA sceglie l'azione, il sistema calcola il risultato, l'UI viene aggiornata, ed il turno termina.
5. Viene controllato il termine del combattimento.
    a. Il combattimento è terminato con esito vittoria.
    b. Il combattimento è terminato con esito sconfitta.
    c. Il combattimento prosegue.

```mermaid
sequenceDiagram
    participant UI as Giocatore (Interfaccia)
    participant Client as Client di Gioco
    participant CM as Gestore Combattimento
    participant PC as Personaggio Giocatore
    participant EC as Personaggio Nemico

    Note over UI, Client: Giocatore si muove sulla mappa

    Client->>Client: Rileva Collisione(PC, EC)
    activate Client
    Client->>CM: IniziaCombattimento(PC, EC)
    activate CM
    Note right of CM: Prepara stato battaglia, UI, ordine turni
    Client->>UI: Mostra Schermata Combattimento()
    deactivate Client

    loop Finchè Combattimento Attivo
        CM->>CM: Determina Prossimo Turno()

        alt Turno Giocatore
            CM->>UI: Mostra Menu Azioni()
            UI->>CM: SelezionaAzione(azione, bersaglioID)
            CM->>PC: EseguiAzione(azione, bersaglioID)
            activate PC
            Note right of PC: Calcola danno/effetti
            PC-->>CM: RisultatoAzione(danno, status)
            deactivate PC
            CM->>UI: AggiornaUI(danno, status, animazioni)

        else Turno Nemico
            CM->>EC: Richiedi Azione IA()
            activate EC
            Note right of EC: IA sceglie azione e bersaglio
            EC-->>CM: AzioneScelta(azione, bersaglioID)
            deactivate EC
            CM->>PC: ApplicaEffettoAzioneNemica(azione)
            activate PC
            PC-->>CM: RisultatoAzione(danno, status)
            deactivate PC
            CM->>UI: AggiornaUI(danno, status, animazioni)
        end

        CM->>CM: Controlla Fine Combattimento()
        Note right of CM: Verifica HP di tutti i partecipanti
        alt Condizione Fine Raggiunta
                CM->>Client: TerminaCombattimento(esito, ricompense?)
                activate Client
                alt Esito Vittoria
                    Client->>Client: AssegnaRicompense(XP, Oro, Oggetti)
                    Client->>UI: Mostra Schermata Vittoria()
                else Esito Sconfitta
                    Client->>UI: Mostra Schermata Sconfitta()
                    Client->>Client: Gestisci Sconfitta() // Es. Carica ultimo save
                end
                deactivate Client
                deactivate CM
        end
    end

    Client->>UI: Torna alla Mappa Mondo()
```


QUI HO SCRITTO LA DOCUMENTAZIONE
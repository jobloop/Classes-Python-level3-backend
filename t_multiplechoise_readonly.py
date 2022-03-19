# Oppgave a)
class Sporsmaal:
    neste_id = 1        # Oppgave g), klasse-variabel

    # Oppgave a) og b)
    def __init__(self, sporsmaal, svaralternativene, korrekt_svar=0):
        self.__sporsmaal = sporsmaal
        self.__svaralternativene = svaralternativene
        self.__korrekt_svar = korrekt_svar
        self.__id = Sporsmaal.neste_id      # Oppgave g)
        Sporsmaal.neste_id += 1             # Oppgave g)

    # Oppgave h)
    @property
    def sporsmaal(self):
        return self.__sporsmaal

    # Oppgave h)
    @property
    def svaralternativene(self):
        return self.__svaralternativene

    # Oppgave h)
    @property
    def korrekt_svar(self):
        return self.__korrekt_svar

    # Oppgave g)
    @property
    def id(self):
        return self.__id

    # Oppgave c)
    def sjekk_riktig_svar(self, svaret):
        if svaret == self.korrekt_svar:
            return True
        else:
            return False

    # Oppgave d)
    def __str__(self):
        resultat = "Spørsmål:\n"
        resultat += self.__sporsmaal + "\n"
        for nummer, svar in enumerate(self.svaralternativene):
            resultat += f"{nummer}: {svar}\n"
        return resultat


# Oppgave e)
def lag_sporsmaal():
    sporsmaalene = []
    sporsmaalene.append(Sporsmaal("Hvilken løkkestruktur bruker man for å kjøre en blokk et oppgitt antall ganger?",
                                  ["for", "while", "if", "try"]))
    sporsmaalene.append(Sporsmaal("Hvilken logisk operator er bare sann hvis begge argumentene er sanne?",
                                  ["or", "not", "and", "xor"], 2))
    sporsmaalene.append(Sporsmaal("Hvilken logisk operator er sann hvis minst ett av argumentene er sanne?",
                                  ["or", "not", "and", "xor"]))
    sporsmaalene.append(Sporsmaal("Hva er 2+2?",
                                  ["2", "4", "6"], 1))
    sporsmaalene.append(Sporsmaal("Hva blir resultatet av Python formelen 2**3?",
                                  ["5", "6", "8", "16"], 2))
    return sporsmaalene


# Oppgave f)
if __name__ == "__main__":
    sporsmaalene = lag_sporsmaal()
    korrekte_svar = 0
    for sporsmaal in sporsmaalene:
        print(sporsmaal)
        svar = input("Hva er riktig svar? Skriv tallet foran korrekt svaralternativ: ")
        svar = int(svar)
        if sporsmaal.sjekk_riktig_svar(svar):
            print("Korrekt!")
            korrekte_svar += 1
        else:
            print("Feil!")
    print(f"Ferdig. Du fikk {korrekte_svar} riktige av {len(sporsmaalene)} mulige.")

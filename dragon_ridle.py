import random
import time

def displayIntro():
    print('''Du er i et land fullt av drager. Foran deg,
du ser to huler. I den ene hulen er dragen vennlig
og vil dele skatten sin med deg, hvis du svarer riktig på en gåte. Den andre dragen
er grådig og sulten, og vil spise deg så snart han ser deg.
Hvilken hule vil du gå inn i? (1 eller 2).''')
    print()

def velgHule():
    hule = ''# Tom string - variabelen må defineres før den kan brukes
    while hule != '1' and hule != '2': #løkken kjører så lenge varibaelen hule IKKE er nr 1 eller 2
        print('Hvilken hule vil du gå inn i? (1 or 2)')
        hule = input()
    return hule #legg merke til at return har samme innrykk som "while"

def sjekkHule(valgtHule):
    print('Du har kommet fram til hulen...')
    time.sleep(2)
    print('Det er mørkt og nifst...')
    time.sleep(2)
    print('En svær drage hopper fram foran deg! Han åpner sin store kjeft og...')
    print()
    time.sleep(2)
    vennligHule = random.randint(1, 2)#"=" betyr "skal være" et tilfeldig tall mellom 1 og 2
    if valgtHule == str(vennligHule):# "==" betyr "sammenlign" disse to variablene/parametrer
        svar = input('...ber deg om svaret på en gåte. Hva er det som går og går men aldri kommer til døra? Svar: ' )
        svar = svar.lower()
        if svar == 'klokka' or svar == 'klokken':
            print('...riktig svar - du får skatten i belønning!')
        else:
            print('...svaret er feil,og du får ingen skatt - og er fattig som en kirkerotte')
    else:
        print('...sluker deg hel!')

playAgain = 'ja'
while playAgain == 'ja' or playAgain == 'j':# Her er "==" sammenlign om det ene eller det andre input er riktig
    displayIntro()#Her kalles displayIntro() funksjonen
    hullNr = velgHule()#Her kalles velgHule() funksjonen
    sjekkHule(hullNr)#Her kalles sjekkHule(hullNr) funksjonen og den skal ta inn hullNr variablen inn i funksjonen.
    print('Vil du spille en gang til? (ja/nei)')
    playAgain = input()

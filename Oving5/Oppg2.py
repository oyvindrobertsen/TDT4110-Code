def kjonnPrompt():
    prompt = input('Er du (m)ann eller (k)vinne? ')
    if prompt == 'hade' or prompt == 'm' or prompt == 'k':
        return prompt
    else:
        kjonnPrompt()


def alderPrompt():
    prompt = input('Hvor gammel er du? ')

    if prompt == 'hade':
        return prompt
    else:
        try:
            tempvar1 = int(prompt)
        except ValueError:
            alderPrompt()
        else:
            if 16 <= int(prompt) <= 25:
                return int(prompt)
            else:
                print('Du er desverre ikke en del av denne undersøkelsens målgruppe. Værsegod neste!')
                lokke()



def aktivSosMedPrompt():
    prompt = input('Benytter du deg av et eller flere aktive sosiale medier (Ja/Nei)? ')
    if prompt == 'Ja' or prompt == 'ja' or prompt == 'Nei' or prompt == 'nei' or prompt == 'hade':
        return prompt
    else:
        aktivSosMedPrompt()

def facebookPrompt():
    if kjonn == 'm':
        prompt = input('Mellom 40-45% av Facebook sine brukere er menn. Er du en av disse (Ja/Nei)? ')
    else:
        prompt = input('Mellom 55-60% av Facebook sine brukere er menn. Er du en av disse (Ja/Nei)? ')

    if prompt == 'Ja' or prompt == 'ja' or prompt == 'Nei' or prompt == 'nei' or prompt == 'hade':
        return prompt
    else:
        facebookPrompt()

def timerSosMedierPrompt():
    prompt = input('Hvor mange timer i snitt bruker du daglig på sosiale medier? ')

    if prompt == 'hade':
        return prompt
    else:
        pass

    try:
        tempvar1 = float(prompt)
    except ValueError:
        timerSosMedierPrompt()
    else:
        return float(prompt)

def lokke():
    do = True
    global aktiv_sosmedier
    global kjonn
    global alder


    while do == True:
        print('Husk at du kan avslutte undersøkelsen til enhver tid ved å skrive hade.')

        kjonnVar = kjonnPrompt()

        if kjonnVar == 'hade':
            break
        else:
            kjonn = kjonnVar

        alderVar = alderPrompt()

        if alderVar == 'hade':
            break
        else:
            alder = alderVar

        aktivSosMedVar = aktivSosMedPrompt()

        if aktivSosMedVar == 'hade':
            break
        else:
            aktiv_sosmedier = aktivSosMedVar

        if aktiv_sosmedier == 'Ja' or aktiv_sosmedier == 'ja':
            facebookVar = facebookPrompt()

            if facebookVar == 'hade':
                break
            else:
                medlem_facebook = facebookVar

            timerSosMedierVar = timerSosMedierPrompt()

            if timerSosMedierVar == 'hade':
                break
            else:
                timer_sosmedier = timerSosMedierVar
        else:
            continue

    print('test')










def main():
    antall_kvinner = 0
    antall_menn = 0
    antall_sosmedier = 0
    antall_facebook = 0
    antall_timer_sosmedier = 0
    lokke()

main()

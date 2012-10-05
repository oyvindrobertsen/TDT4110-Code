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
        prompt = input('Mellom 55-60% av Facebook sine brukere er kvinner. Er du en av disse (Ja/Nei)? ')

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
    global kjonn

    antall_kvinner = 0
    antall_menn = 0
    antall_sosmedier = 0
    antall_menn_facebook = 0
    antall_kvinner_facebook = 0
    antall_facebook = 0
    antall_timer_sosmedier = 0


    while do == True:
        print('Husk at du kan avslutte undersøkelsen til enhver tid ved å skrive hade.')

        kjonn = kjonnPrompt()

        if kjonn == 'hade':
            break
        elif kjonn == 'm':
            antall_menn = antall_menn + 1
        else:
            antall_kvinner = antall_kvinner + 1


        alder = alderPrompt()

        if alder == 'hade':
            break
        else:
            pass

        aktiv_sosmedier = aktivSosMedPrompt()

        if aktiv_sosmedier == 'hade':
            break
        elif aktiv_sosmedier == 'Ja' or aktiv_sosmedier == 'ja':
            antall_sosmedier = antall_sosmedier + 1


        if aktiv_sosmedier == 'Ja' or aktiv_sosmedier == 'ja':
            medlem_facebook = facebookPrompt()

            if medlem_facebook == 'hade':
                break
            elif (medlem_facebook == 'Ja' or medlem_facebook == 'ja') and kjonn == 'm':
                antall_menn_facebook = antall_menn_facebook + 1
            elif (medlem_facebook == 'Ja' or medlem_facebook == 'ja') and kjonn == 'k':
                antall_kvinner_facebook = antall_kvinner_facebook + 1

            antall_facebook = antall_menn_facebook + antall_kvinner_facebook


            timer_sosmedier = timerSosMedierPrompt()

            if timer_sosmedier == 'hade':
                break
            else:
                antall_timer_sosmedier = antall_timer_sosmedier + timer_sosmedier
        else:
            continue

    print('Antall menn:', antall_menn)
    print('Antall kvinner:', antall_kvinner)
    print('Antall aktive på sosiale medier:', antall_sosmedier)
    print('Antall menn på facebook:', antall_menn_facebook)
    print('Antall kvinner på facebook:', antall_kvinner_facebook)
    print('Antall på facebook totalt:', antall_facebook)
    print('Totalt antall timer på sosiale medier:', antall_timer_sosmedier)


def main():
    lokke()

main()

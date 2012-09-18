def main():
    print('Et program for å beregne nettopris paa bil')
    navn = input('Navnet på bilen: ')
    bpris = int(input('Bruttoprisen på bilen [kr]: '))
    vekt = int(input('Vekt på bilen [kg]: '))
    bhp = int(input('Antall hestekrefter på bilen [hk]: '))
    utslipp = int(input('Antall gram Co2-utslipp på bilen [gram]: '))
    volum = int(input('Motorvolum på bilen [liter]: '))
    beregn_avgift(navn, bpris, vekt, bhp, utslipp, volum)

def beregn_avgift(navn, bpris, vekt, bhp, utslipp, volum):
    volump = bpris * volum * 0.00055
    CO2p = bpris * utslipp * 0.004
    hkp = bpris * bhp * 0.00015
    vektp = bpris * vekt * 0.00034
    netto = bpris + vektp + hkp + CO2p + volump
    print('Utsalgspris på', navn ,' vil bli', netto,'kr')
main()

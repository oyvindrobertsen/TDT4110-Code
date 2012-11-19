from skumleskogen2 import *
hukommelse = {}
steg = 0

def solver():
    global steg
    global hukommelse
    n = nummer()
    print(n)

    if er_nokkel():
        plukk_opp()
        hukommelse = {}
    elif er_laas():
        laas_opp()
    elif er_utgang():
        gaa_ut()
        print(steg)
        return

    if n not in hukommelse:
        hukommelse[n] = {"venstre": False, "hoyre": False}


    if er_stank():
        hukommelse[n]["venstre"] = True
        hukommelse[n]["hoyre"] = True
        steg += 1
        gaa_tilbake()
        solver()
    elif hukommelse[n]["hoyre"] == False:
        hukommelse[n]["hoyre"] = True
        if gaa_hoyre == False:
            solver()
        else:
            steg += 1
            gaa_hoyre()
            solver()
    elif hukommelse[n]["venstre"] == False:
        hukommelse[n]["venstre"] = True
        if gaa_venstre == False:
            solver()
        else:
            steg += 1
            gaa_venstre()
            solver()
    else:
        steg += 1
        gaa_tilbake()
        solver()



def main():
    solver()

main()

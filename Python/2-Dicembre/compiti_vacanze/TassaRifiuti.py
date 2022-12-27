while True:
    try:
        categoria = int(input("categoria:"))
        n_famiglia = int(
            input("numero componenti di famiglia per box inserire 0:"))
        mq = float(input("metri quadrati:"))
        break
    except:
        print("errore")
tari = 0
abitazioni = {
    1: "1.23764 49.92488",
    2: "1.45422 134.17313",
    3: "1.62440 160.38370"
}
alloggi = {
    1: "1.23764 39.93990",
    2: "1.45422 107.33850",
    3: "1.62440 128.30696"
}


def cinquepercento(n):
    return n+(n*0.05)


def calcolaTARI(categoria, n_famiglia, mq):
    match categoria:
        case 1:
            abitazioni.keys()
            try:
                # tmq=['1.23764', '49.92488']
                tmq = abitazioni[n_famiglia].split()
            except:
                print("errore non presente nel registro")
            # print(tmq)
            tari = float(tmq[0])*mq
            tari = tari+float(tmq[1])
        case 2:
            alloggi.keys()
            try:
                # tmq=['1.23764', '49.92488']
                tmq = alloggi[n_famiglia].split()
            except:
                print("errore non presente nel registro")
            # print(tmq)
            tari = float(tmq[0])*mq
            tari = tari+float(tmq[1])
        case 3:
            pass
        case 4:
            tari = 0.34758*mq+0.35771
        case _:
            print("errore")
    cinquepercento(tari)
    return tari


tari = calcolaTARI(categoria, n_famiglia, mq)
print("i dati inseriti sono:", categoria,
      n_famiglia, mq, "per un totale di tari di:")
print(tari)

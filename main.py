import random


def addToList(curPool, taking, points):
    onnistunut = 0
    while onnistunut < points:
        luku = random.randint(0, len(taking) - 1)
        if not taking[luku] in curPool:
            curPool.append(taking[luku])
            onnistunut += 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    currentPool = []

    urheilullisuus = 0
    taiteellisuus = 0
    muusisuus = 0
    pelaaja = 0
    ulkoilu = 0
    kokkaus = 0
    matkailija = 0
    yksilolajit = 0

    file = open("kysymys.txt", "r")
    rivi = 0
    for line in file:
        if rivi == 0:
            splitted = line.split(",")
            if splitted[0] == "Kaksi kertaa kuussa":
                urheilullisuus += 1
            elif splitted[0] == "Kerran viikossa":
                urheilullisuus += 2
            urheilullisuus += int(splitted[1])
            taiteellisuus += int(splitted[2])
            muusisuus += int(splitted[3])
            pelaaja += int(splitted[4])
            ulkoilu += int(splitted[5])
            kokkaus += int(splitted[6])
            matkailija += int(splitted[7])
            yksilolajit += int(splitted[8])
            rivi += 1
        elif rivi == 1:
            line = line.rstrip()
            line = line.split(",")
            for x in line:
                x = x.strip()
                if x == "Yleisen kunnon parantaminen tai fyysinen terveys":
                    urheilullisuus += 1
                elif x == "Uusien taitojen oppiminen":
                    urheilullisuus += 1
                elif x == "Luova itseilmaisu":
                    taiteellisuus += 1
                    muusisuus += 1
    file.close()


    urheilulajit = ["juoksu", "uinti", "jalkapallo", "koripallo", "tennis", "sulkapallo", "koripallo",
                    "kuntosaliharjoittelu", "judo", "futsal", "salibandy", "nyrkkeily", "padel", "squash"]
    taide = ["maalaaminen", "kuvanveisto", "keramiikka teko", "ompelu", "neuolominen", "korujen tekeminen"]
    musiikki = ["soittaminen", "laulaminen", "tanssiminen", "bändissä soittaminen", "DJ soittaminen"]
    pelaaminen = ["tietokonepelaaminen", "konsolipelaaminen", "lautapelailu", "korttipelaaminen", "Dungeons and Dragons"]
    luonto = ["retkeily", "kalastus", "metsästys", "puutarhanhoito", "patikointi"]
    ruoka = ["kokkaaminen", "leipominen", "viininvalmistus", "oluenpano", "viljely"]
    matkailu = ["vaellus", "maastopyöräily", "sukellus", "surffaus", "maantipyöräily", "laskettelu"]
    yksin = ["Lukeminen", "Kirjoittaminen", "Piirtäminen", "maalaaminen", "Valokuvaus", "soittaminen", "juokseminen",
             "jooga", "Puutarhanhoito", "neulominen", "virkkaus", "Retkeily", "ompelu"]

    addToList(currentPool, urheilulajit, urheilullisuus)
    addToList(currentPool, taide, taiteellisuus)
    addToList(currentPool, musiikki, muusisuus)
    addToList(currentPool, pelaaminen, pelaaja)
    addToList(currentPool, luonto, ulkoilu)
    addToList(currentPool, ruoka, kokkaus)
    addToList(currentPool, matkailu, matkailija)
    addToList(currentPool, yksin, yksilolajit)
    print("Lajisi olisi:", currentPool[random.randint(0, len(currentPool) - 1)])

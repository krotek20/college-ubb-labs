def creeaza_tranzactie(tid, zi, suma, tip):
    return {
        "id": tid,
        "zi": zi,
        "suma": suma,
        "tip": tip
    }


def get_id(tranzactie):
    return tranzactie["id"]


def set_id(tranzactie, tid):
    tranzactie["id"] = tid


def get_zi(tranzactie):
    return tranzactie["zi"]


def set_zi(tranzactie, zi):
    tranzactie["zi"] = zi


def get_suma(tranzactie):
    return tranzactie["suma"]


def set_suma(tranzactie, suma):
    tranzactie["suma"] = suma


def get_tip(tranzactie):
    return tranzactie["tip"]


def set_tip(tranzactie, tip):
    tranzactie["tip"] = tip

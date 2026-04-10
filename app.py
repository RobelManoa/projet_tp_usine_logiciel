# fonction calcule TVA
def calculer_tva(prix, taux=0.20):
    tva = prix * (taux / 100)
    return tva
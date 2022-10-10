
#futures

def long(K, S_t, taille):
    print("La position est long sur le Futures")
    print("Le strike est", K," le prix spot est", S_t, "et la taille est", taille)
    position = (S_t-K)*taille
    return print("le payoff de la position est", position)

def short(K,S_t, taille):
    print("La position est short sur le Futures")
    print("Le strike est", K," le prix spot est", S_t, "et la taille est", taille)
    position = (K-S_t)*taille
    return print("le payoff de la position est", position)

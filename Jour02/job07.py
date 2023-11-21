def pyramide(n):
    chaine = "abcdefghijklmnopqrstuvwxyz" * n
    indice = 0
    niveau = 1

    while indice + niveau <= len(chaine):
        print(chaine[indice:indice + niveau])
        indice += niveau
        niveau += 1
pyramide(10)

def job_13():
    liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
    unique_liste = []
    for x in liste:
        if x not in unique_liste:
            unique_liste.append(x)
    return unique_liste
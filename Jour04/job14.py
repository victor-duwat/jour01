def job_14(n, text):
    mots = text.split()
    longs_mots = [mot for mot in mots if len(mot) > n]
    return ' '.join(longs_mots)
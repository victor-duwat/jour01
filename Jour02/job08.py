def triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Pas un triangle"
    if a == b == c:
        return "Équilatéral"
    if a == b or b == c or a == c:
        isocèle = "Isocèle"
        if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
            return isocèle + " et Rectangle"
        return isocèle
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
        return "Rectangle"
    return "Quelconque"
#pas sure de celui là mais il était dure

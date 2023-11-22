def verifier_pair_impair(nombre):
    if nombre % 2 == 0:
        return f"{nombre} est pair."
    else:
        return f"{nombre} est impair."

print(verifier_pair_impair(10))
print(verifier_pair_impair(15))
print(verifier_pair_impair(-5))


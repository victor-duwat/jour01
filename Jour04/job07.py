def job_07():
    L = [8, 24, 48, 2, 16]
    compte = sum(1 for x in L if x % 3 == 0)

    return compte
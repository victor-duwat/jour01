def investissement(montant_initial,rendement):

    gain_annuel=montant_initial*rendement

    print("le gain annuel de l'investisseur est de: ",gain_annuel)

    capital=(montant_initial+5000)*1.2

    print("le capitale de l'investisseur est de:",capital)

    montant_final=capital*0.9

    rendement_final=rendement*0.99

    gain_final=montant_final*rendement_final

    print("le montant final de l'investisseur est de :",montant_final,"son rendement final est de:",rendement_final,"et son gain_final est de :",gain_final)

    
investissement(500,0.2)
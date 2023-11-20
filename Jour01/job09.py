def inventaire(prix_pomme,stock_pomme):
    utilisateur=int(input("Combien de pomme voulez vous ?"))
    prix_pomme=prix_pomme*0.9
    stock_pomme=stock_pomme-utilisateur
    print('Nos pommes sont aux prix de:',prix_pomme,"Є","et il nous en reste : ",stock_pomme)
inventaire(10,100)
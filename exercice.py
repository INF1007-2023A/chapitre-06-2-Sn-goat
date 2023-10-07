#!/usr/bin/env python
# -*- coding: utf-8 -*-


def list_to_dict(some_list):
    dictlist = {}
    for index,cle in enumerate(some_list):
        dictlist[cle] = index

    return dictlist



def color_name_to_hex(colors: list) -> list:
    listcolors = []
    for couleur in colors:
        valeur = 0
        for lettre in couleur:
            valeur += ord(lettre)
        OxValeur = hex(valeur)
        listcolors.append((couleur,OxValeur))
  
    return listcolors



def create_list() -> list:
    intListe = [i for i in range(10000) if (i > 0)  and i == int(i) ]
    trueIntListe = [i for i in intListe if not(15 <= i <= 350) ]

    return trueIntListe



def compute_mse(model_dict: dict) -> dict:
    TotalDiffErreurquad = 0
    for module in model_dict:
        for erreurTuple in model_dict[module]:
            diffErreurquad = (erreurTuple[1] - erreurTuple[0]) **2
            TotalDiffErreurquad += diffErreurquad
        MSE = TotalDiffErreurquad / len(model_dict[module])
        model_dict[module] = MSE
    return model_dict


def main() -> None:
    some_list = ["a", "b", "z", "patate"]
    print(f"La liste suivante {some_list} est transformée en dictionnaire: {list_to_dict(some_list)}")

    colors = ["blue", "red", "green", "yellow", "black", "white"]
    print(f"La valeur hex associée aux couleurs est: {color_name_to_hex(colors)}")

    print(f"La liste des 10000 entiers est: {create_list()}")

    model_dict = {"LR": [(90, 92), (96, 100), (20, 25), (21, -2), (3, -20)],
                  "DNN": [(100, 101), (50, 50), (1,2), (-10, -12), (-1, 7)],
                  "RF": [(10, 19), (56, 70), (1, 9), (-100, -12), (-11, 7)]}
    print(f"Le mse des différents modèles est: {compute_mse(model_dict)}")


if __name__ == '__main__':
    main()

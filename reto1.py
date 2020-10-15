# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 12:14:07 2020

@author: roberthdel87
"""
def nota_quices(codigo: str, nota1: int, nota2: int, nota3: int, nota4: int, nota5: int):
    quitar_nota = min(nota1,nota2,nota3,nota4,nota5)
    promedio = ((nota1 + nota2 + nota3 + nota4 + nota5 - quitar_nota)/20)/4
    return "El promedio ajustado del estudiante "+codigo+" es: "+str(round(promedio,2))

print(nota_quices("BIO2201810", 45,46,33,74,22))

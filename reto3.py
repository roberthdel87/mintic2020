# -*- coding: utf-8 -*-
"""
=============================
Wed Oct  7 15:24:49 2020
@author: roberthdel87
Ejercicio: reto3
=============================
"""
distancias = {('H', 'H'): 0, ('H', 'A'): 21, ('H', 'B'): 57, ('H', 'C'): 58, ('H', 'D'): 195, ('H', 'E'): 245,
              ('H', 'F'): 241, ('A', 'H'): 127, ('A', 'A'): 0, ('A', 'B'): 231, ('A', 'C'): 113, ('A', 'D'): 254,
              ('A', 'E'): 179, ('A', 'F'): 41, ('B', 'H'): 153, ('B', 'A'): 252, ('B', 'B'): 0, ('B', 'C'): 56,
              ('B', 'D'): 126, ('B', 'E'): 160, ('B', 'F'): 269, ('C', 'H'): 196, ('C', 'A'): 128, ('C', 'B'): 80,
              ('C', 'C'): 0, ('C', 'D'): 136, ('C', 'E'): 37, ('C', 'F'): 180, ('D', 'H'): 30, ('D', 'A'): 40,
              ('D', 'B'): 256, ('D', 'C'): 121, ('D', 'D'): 0, ('D', 'E'): 194, ('D', 'F'): 109, ('E', 'H'): 33,
              ('E', 'A'): 144, ('E', 'B'): 179, ('E', 'C'): 114, ('E', 'D'): 237, ('E', 'E'): 0, ('E', 'F'): 119,
              ('F', 'H'): 267, ('F', 'A'): 61, ('F', 'B'): 79, ('F', 'C'): 39, ('F', 'D'): 135, ('F', 'E'): 55,
              ('F', 'F'): 0}
#ruta_inicial = ['H', 'B', 'E', 'A', 'C', 'D', 'H']
ruta_inicial = ['H', 'A', 'B', 'C', 'D', 'E', 'F', 'H']

def ruteo(distancias: dict, ruta_inicial: list)-> dict:
    #Ciclo valida diccionario sea correcto k es la llave y v es el valor
    for k, v in distancias.items():
        """
        Si valor es menos de 0 retorna “Por favor revisarlos datos de entrada.”
        Si valor es 0 pero llaves diferentes retorna “Por favor revisarlos datos de entrada.”
        Si valor es diferente de 0 y llaves iguales retorna “Por favor revisarlos datos de entrada.”
        """
        if v < 0 or (v ==0 and k[0]!=k[1]) or (v !=0 and k[0]==k[1]):
            return "Por favor revisar los datos de entrada."
    
    calcular_distancia = calculo_ruta(ruta_inicial, distancias)
    lista_nueva = ruta_inicial.copy()
    nueva_lista = ruta_inicial.copy()
    i = 1
    control_parada = True
    mejor_lista = ruta_inicial.copy()
    while control_parada:
        control_parada = False
        i = 1
        lista_nueva = mejor_lista.copy()
        while i < len(ruta_inicial)-1:
            j = i + 1
            while j < len(ruta_inicial)-1:
                nueva_lista = lista_nueva.copy()
                auxiliar = nueva_lista[i]
                nueva_lista[i] = nueva_lista[j]
                nueva_lista[j] = auxiliar
                calculo_nueva_lista = calculo_ruta(nueva_lista,distancias)
                #aquí condicional de nueva ruta
                if calcular_distancia > calculo_nueva_lista:
                    mejor_lista = nueva_lista.copy()
                    calcular_distancia = calculo_nueva_lista
                    control_parada = True
                j = j + 1
            i = i +1
    return {'ruta': '-'.join(mejor_lista), 'distancia':calcular_distancia}
def calculo_ruta(ruta: list, distancias:dict):
    #Con esta variable sumo la distancia
    distancia_total=0
    lista_tuplas = []
    i = 0
    while i < len(ruta)-1:
        #Aquí añadí hasta i+1 para colocar en la última tupla H
        tupla = (ruta[i],ruta[i+1])
        lista_tuplas.append(tupla)
        distancia_total = distancia_total + distancias[tupla]
        i = i + 1  
    return distancia_total
        
def cambio_lista(tupla, lista_nueva):
    a = tupla[0]
    b = tupla[1]
    lista_nueva = lista_nueva.copy()
    indice_a = lista_nueva.index(a)
    indice_b = lista_nueva.index(b)
    
    lista_nueva[indice_a] = b
    lista_nueva[indice_b] = a    
    
    return lista_nueva

print(ruteo(distancias, ruta_inicial))

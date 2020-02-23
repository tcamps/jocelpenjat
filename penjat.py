import random
import os


# VARIABLES GLOBALS
# Utilizarem una llista per les paraules, cada element és una nova llista de dos elements
# https://thomas-cokelaer.info/tutorials/python/data_structures.html
llista_paraules = [['CIUTAT', 'BARCELONA'], ['CIUTAT', 'MADRID'], ['CIUTAT', 'VALENCIA'], ['CIUTAT', 'LONDRES'], ['CIUTAT', 'ROMA'], ['CIUTAT', 'PARIS'],
                    ['ANIMAL', 'GAT'], ['ANIMAL', 'GOS'], ['ANIMAL', 'SERP']]

# Paraula amb la qual es juga
paraula_actual = ''
# Tipus de paraula amb la qual es juga
tipus_paraula = ''
# Utilizarem un 'set' per les lletres introduides. Els 'set' no permeten duplicats.
lletres_escrites = set()
paraules_encertades = 0
errors = 0
max_errors = 6


def neteja_terminal():
    os.system('clear')


# Funció que escull una paraula aleatoriament
# La treu de la llista per evitar duplicats
# Retorna una llista de dos elements: tipus i paraula
def retorna_paraula():
    pass


# Elegeix nova paraula i inicalitza lletres_escrites
# Aquesta funció es cridarà a l'inici i cada cop que s'encerti una paraula
def inicialitza_paraula():
    pass


# Funció que dibuixa el text descriptiu de la paraula i els caracters en blanc
# Retorna true si ja s'ha encertat la paraula i false en cas negatiu
def dibuixa_paraula():
    pass


# Funció que dibuixa el penjat, depenent del nombre d'errors
def dibuixa_penjat():
    pass


# Funció que introdueix nova lletra a llista_lletres i comprova si és un error
def nova_lletra(lletra):
    pass


# CODI PRINCIPAL DEL JOC
inicialitza_paraula()

# Bucle principal del joc
# Finalitzarà en arribar al nombre màxim d'errors o encertar totes les paraules
joc = True
while joc:
    pass

# S'ha finalitzat el joc
# Informem en quin cas ens trobem
# Demanem nom i guardem puntuació

# Llegim i mostrem puntuacions ordenades de major a menor

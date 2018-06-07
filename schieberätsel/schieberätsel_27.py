# -*- coding: utf-8 -*-
"""
Programm zur Lösung des SPON Rätsels:
"Meistern Sie das Schiebepuzzle"

Autor: JackNyx

"""

import random

def verschieben(kacheln):
    
    """Verschiebt eine zufällig gewählte Kachel, die sich in Nachbarschaft des 
       leeren Feldes befindet.
       Die Positionen der Kacheln sind durch die Listenindeces 0 (links oben) 
       bis 5 (rechts unten) gegeben.   """
    
    index_leer = kacheln.index("leer")
    # index_liste gibt für die Positionen 0 bis 5 den Index der benachbarten Kacheln an"
    index_liste = [[1,3], [0,2,4], [1, 5], [0, 4], [1, 3, 5], [2, 4]] 
    # index_nachbarn: dem leeren Feld benachbarte Kacheln
    index_nachbarn = index_liste[index_leer]
    #zufällige Auswahl einer Kachel
    index_feld = random.choice(index_nachbarn)
    # ausgewählte Kachel und leeres Feld tauschen Positionen
    kacheln[index_feld], kacheln[index_leer] = kacheln[index_leer], kacheln[index_feld]
    
    return kacheln



loesung = []
versuche_alt = 1000      # beliebiger (großer) Startwert


for n in range(1000):    # minimiert Anzahl an Schritten
    
    # initiale Konfiguration
    kacheln = ["zwei", "leer", "blank_a", "eins", "blank_b", "blank_c"]
    prozedur = []
    prozedur.append(kacheln[:])
    
    # Erster Schritt
    kacheln = verschieben(kacheln)
    prozedur.append(kacheln[:])
    i = 1
    
    # Schiebt Kacheln so lange herum, bis sich Kachel eins und Kachel 2 an der
    # richtigen Position befinden
    while ((kacheln.index("eins") != 0) or (kacheln.index("zwei") != 3)):
        
        kacheln = verschieben(kacheln)
        
        # Verhindert, dass eine Kachel in zwei aufeinanderfolgenden Zügen hin-
        # und wieder zurückgeschoben wird.
        if (kacheln != prozedur[-2]):                
            prozedur.append(kacheln[:])
            i +=1 
        else:
           kacheln = list(prozedur[-1])         
        
    versuche = i
    if versuche < versuche_alt:
        loesung = prozedur[:]
        versuche_alt = versuche
    else:
        pass


for index, value in enumerate(loesung, 0):
    print index, value
print "\n" + "Es waren %i Schritte nötig." % versuche_alt   
        
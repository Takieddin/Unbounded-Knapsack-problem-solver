




import csv
from time import sleep
import numpy as np



from time import time
class Product(object):

    def __init__(self, idd, v, w):
        self.idd = idd
        self.w = w
        self.v = v


def agalgo( capacity,array,t0param,alphaparam,maxitparam):

    i=1
    pt=[]
    for row in array :
        p=Product('x'+str(i+1),int(row[1]),int(row[0]))
        pt.append(p)
        i+=1

        


    t1=time()
    pt.sort(key=lambda x:-x.v / x.w)

    lnpt=len(pt)

    M = 0
    sols=[0]*lnpt
    capa = capacity
    i = 0
    while capa > 0 and i < lnpt:
        if capa > pt[i].w:
            sols[i] += 1
            capa -= pt[i].w
            M += pt[i].v
        else:
            i += 1
    
    t2 = time()
    #todo
    ##################
    """
    
    T = T0
    sol_actuelle = sol_initial
    sol_meilleure = sol_initial
    tanque le num_it < max_it
    trouver x solution voisine // appartient à N(x) ou N(x) c’est l’ensemble de solutions
    calculer df = f(x) - f(sol_actuelle)
    si df > 0
    alors sol_actuelle = x
    sinon
    générer un Beta aléatoirement qui appartient à [0,1] (un paramètre de tolérance)
    si exp(-df/T) > beta (le critère de Metropolis )
    alors sol_actuelle = x
    sinon // la solution est rejetée
    Finsi
    si f(sol_actuelle) > f(sol_meilleure)
    sol_meilleure = sol_actuelle
    T= T * alpha // Mettre à jour la température de refroidissement T (Abaisser la température)
    Fin de la boucle tant que
    """
    t = t0param
    it=0
    sol_actu =sols
    best_sol =sols
    #while it<maxitparam:

















    #############
    t2=time()
    objs =[]
    vols =[]
    values =[]
    nb_exem =[]
    volume_taken=0

    for i in range(len(sols)):
        if sols[i]:
            objs.append(str(pt[i].idd))
            vols.append(str(pt[i].w))
            volume_taken += int((pt[i].w))*int(sols[i])
            values.append(str(pt[i].v))
            nb_exem.append(str(sols[i]))
    d=str("{:.15f}".format(t2-t1))+ ' s'

    return d, M, volume_taken, objs, vols,values, nb_exem 


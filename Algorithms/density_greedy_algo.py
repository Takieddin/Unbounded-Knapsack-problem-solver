

from time import time


class Product(object):

    def __init__(self, idd, v, w):
        self.idd = idd
        self.w = w
        self.v = v


def dgalgo(capacity, array):

    i = 1
    pt = []
    for row in array:
        p = Product('x' + str(i + 1), int(row[1]), int(row[0]))
        pt.append(p)
        i += 1

    pt.sort(key=lambda x:-x.v / x.w)

    t1 = time()
    lnpt = len(pt)
    capa = capacity
    M = 0
    sols = [0] * lnpt
    i = 0
    while capa > 0 and i < lnpt:
        if capa > pt[i].w:
            sols[i] += 1
            capa -= pt[i].w
            M += pt[i].v
        else:
            i += 1
    
        t2 = time()
        objs = []
        vols = []
        values = []
        nb_exem = []
        volume_taken = 0

    for i in range(len(sols)):
        if sols[i]:
            objs.append(str(pt[i].idd))
            vols.append(str(pt[i].w))
            volume_taken += int((pt[i].w)) * int(sols[i])
            values.append(str(pt[i].v))
            nb_exem.append(str(sols[i]))
    d = str("{:.15f}".format(t2 - t1)) + ' s'

    return d, M, volume_taken, objs, vols, values, nb_exem 

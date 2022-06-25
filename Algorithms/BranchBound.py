




import csv
from time import sleep
import numpy as np



from time import time

def import_csv(URL):
    URL += ".csv"
    f = open(URL)
    print('URL')
    print(URL)
    myReader = csv.reader(f)
    array = np.loadtxt(f, delimiter=",")

    return array
class Product(object):

    def __init__(self, idd, v, w):
        self.idd = idd
        self.w = w
        self.v = v

class Node(object):
    def __init__(self, i, l,v,lw,p,cc):
        self.i = i
        self.l = l
        self.v = v
        self.lw = lw
        self.p = p
        self.cc = cc

def BranchBound( capacity,array):

    i=0
    pt=[]
    for row in array :
        p=Product('x'+str(i+1),int(row[1]),int(row[0]))
        pt.append(p)
        i+=1

        


    pt.sort(key=lambda x:-x.v / x.w)

    t1=time()
    lnpt=len(pt)
    capacity = capacity

    M = 0
    sols=[0]*lnpt
    root=Node(0,-1,0,capacity,None,capacity//pt[0].w)
    ptr=root
    while ptr: 
        if ptr.l<lnpt-2:
            if ptr.cc>=0:
                clw=ptr.lw-(ptr.cc*pt[ptr.l+1].w)
                cccc=clw//pt[ptr.l+2].w
                cv=ptr.v+ptr.cc*pt[ptr.l+1].v
                eva = cv+clw*pt[ptr.l+2].v/pt[ptr.l+2].w
                if eva>=M+1:
                    ptrcc=ptr.cc
                    ptr.cc=ptr.cc-1
                    ptr= Node(ptrcc,ptr.l+1,cv,clw,ptr,cccc)
                else:
                    ptr.cc=ptr.cc-1
            else:
                ptr=ptr.p
        else:            
            reva=ptr.v+ptr.cc*pt[ptr.l+1].v
            if reva>=M+1:
                M=reva
                sols[lnpt-1]=ptr.cc
                ptr2=ptr
                for i in range(lnpt-2,-1,-1):
                    sols[i]=ptr2.i
                    ptr2=ptr2.p
            ptr=ptr.p
    
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

    return t2-t1, M, volume_taken, objs, vols,values, nb_exem 

def BranchBousnd(cap_sac, array):
    print('rr')
    print(array)
    print(array[0])
    print(array[0][0])
    objs=[]
    vols=[]
    values=[]
    nb_exem=[]
    for i in range(40):
        objs.append('x'+str(i) )
        vols.append(str(i*10) )
        values.append(str(i/10) )
        nb_exem.append(str(i) )
    return 10 ,20 , 15 , objs, vols,values, nb_exem
from copy import deepcopy
import numpy as np

def reg_bd3(bd0=None,bdr0=None):

    xc=np.sum(np.dot(bd0[1],abs(bd0[0]))) / np.sum(abs(bd0[0]))
    yc=np.sum(np.dot(bd0[0],abs(bd0[1]))) / np.sum(abs(bd0[1]))

    bd0=np.append([bd0[0]-yc], [bd0[1]-xc],axis=0)
    bd=deepcopy(bd0)
    bdr=deepcopy(bdr0)

    xc=np.sum(np.dot(bdr[1],abs(bdr[0]))) / np.sum(abs(bdr[0]))
    yc=np.sum(np.dot(bdr[0],abs(bdr[1]))) / np.sum(abs(bdr[1]))

    bdr=np.append([bdr[0] - yc],[bdr[1] - xc],axis=0)
    temp=deepcopy(bdr[1])
    bdr[1]=bdr[0]
    bdr[0]=temp
    temp=deepcopy(bd[1])
    bd[1]=bd[0]
    bd[0]=temp
    N=len(bd[0])
    costold=np.mean(sum(sum(np.power((bdr - bd),2))))
    bdout=deepcopy(bd)
    for k in range(1,N+1):
        idk=np.append(range(k,N+1),range(1,k))
        bdt = np.empty([len(idk),2])
        bdt[:]=np.nan
        for i in range(len(bd.transpose())):
            ind = int(idk[i]-1) 
            temp=bd.transpose()[ind]
            bdt[i] = temp
        temp=np.dot(bdr,bdt)
        u,_,v=np.linalg.svd(temp)
        v = v.T
        q=np.dot(v,u.transpose())
        bdtemp=np.dot(bdt,q)
        costnew=np.mean(sum(sum(np.power((bdr.transpose() - bdtemp),2))))
        if costnew < costold:
            bdout=deepcopy(bdtemp)
            costold=deepcopy(costnew)
        a= bdt[-1:0:-1]
        b= bdt[0]
        bdt = np.concatenate((bdt[-1:0:-1],[bdt[0]]),axis=0)
        temp=np.dot(bdr,bdt)
        u,_,v=np.linalg.svd(temp)
        v = v.T
        q=np.dot(v,u.T)
        bdtemp=np.dot(bdt,q)
        costnew=np.mean(sum(sum(np.power((bdr.T - bdtemp),2))))
        if costnew < costold:
            bdout=deepcopy(bdtemp)
            costold=deepcopy(costnew)
    regbd = deepcopy(bdout.T)
    regbd[:] = np.nan 
    regbd[0] = deepcopy(bdout.T[1])
    regbd[1] = deepcopy(bdout.T[0])
    ytot=costold.T
    return regbd, ytot

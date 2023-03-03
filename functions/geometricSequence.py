import math

def GiveGeomSeqElement(a1=2,factor=2,index=2):
    an = a1*factor**(index-1)
    return an



for i in range(10):
    print(GiveGeomSeqElement(3, 2, i))

def GiveFactorForGeomSeq(a1,a2):
    q = a2/a1
    return q

def GiveSumOfNElementsGeomSeq (a1=2,factor=2,n=2):
    sum = (a1*(1-factor**n))/(1-factor)
    return sum

print(GiveSumOfNElementsGeomSeq(2,3,4))

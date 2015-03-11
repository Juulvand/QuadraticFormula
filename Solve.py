import math

def ABC ():
    value_A = input ('a = ')
    fA = float (value_A)
    value_B = input ('b = ')
    fB = float (value_B)
    value_C = input ('c = ')
    fC = float (value_C)
    
    Discriminant (fA,fB,fC)
    


def Discriminant (a,b,c):
    vD = math.pow(b,2.0)- 4*a*c
    print 'Discriminant =' , vD

    if vD >= 0:    
        Solve (a,b,c,vD)
    else:
        print 'No Solution'


def Solve (a,b,c,d):
    x1 = (- b + math.sqrt (d))/2*a
    x2 = (- b - math.sqrt (d))/2*a
    print 'x1 =' , x1
    print 'x2 =' , x2

ABC ()
    
    

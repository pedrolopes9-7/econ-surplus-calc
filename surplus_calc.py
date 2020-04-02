import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def simps(f,a,b,N=50):
    if N % 2 == 1:
        raise ValueError("N must be an even integer.")
    dx = (b-a)/N
    x = np.linspace(a,b,N+1)
    y = f(x)
    S = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return S

def cons_surplus(pe,qe,Dq):
    cs = simps(Dq,0,qe,10) - pe*qe
    return cs

def prod_surplus(pe,qe,Sq):
    ps = pe*qe - simps(Sq,0, qe, 10)
    return ps

def surplus(Sq, Dq):
    y = lambda q: Sq(q) - Dq(q)
    x0 = 1
    qe = fsolve(y, x0)
    pe = Sq(qe)
    cs = cons_surplus(pe,qe,Dq)
    ps = prod_surplus(pe,qe,Sq)
    
    print ('Equilibrio de mercado encontrado em [pe;qe] = [',pe,qe,']')
    print('Excedente de oferta igual a: ' , ps)
    print('Excedente de produção igual a: ' , cs)

'''
    Exemplo de teste:
        Função de demanda: D(q) = 20 / (q+1)
        Função de oferta: S(q) = q + 2
'''

q = np.linspace(-100,100,1000)
dq = lambda q: 20 / (q + 1)
sq = lambda q: q + 5

surplus(sq, dq)

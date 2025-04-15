import numpy as np
from numpy import linalg as LA
def geoconstrain(C, Cg, tA, W, ratio, rho, step, err, itmax):
    diff = 1
    it = 1
    m, n = np.shape(Cg)
    A = C
    mu = 0.0
    while diff > err:
        Ai = LA.norm(A, axis = 1)
        Aig = np.diag(A@np.transpose(Cg))
        A1 = np.diag((1 - Aig/Ai)/Ai)
        A2 = np.diag(Aig/(Ai*Ai))
        gA1 = A1@(A2@A - Cg)
        
        InA = A@np.transpose(A)
        AIJ = Ai@np.transpose(Ai)
        CoA = InA/AIJ
        W1 = W*(1 - CoA)*CoA
        W2 = W*(1 - CoA)/AIJ
        DW1 = np.sum(W1, axis = 1)
        gA2 = np.diag(DW1/(Ai*Ai))@A - W2@A
        
        gA = (1 - mu)*gA1 + mu*gA2
        EA = (A - C - tA)
        TotalgA = rho*ratio*gA + rho*EA
        A = A - step*TotalgA
        
        diff = LA.norm(TotalgA)/LA.norm(A)
        #print("diff", diff, LA.norm(TotalgA),LA.norm(A), LA.norm(EA), LA.norm(gA))
        it = it + 1
        #print(it,diff)
        
        if it > itmax:
            print("Maximum iteration achived!")        
    return A       

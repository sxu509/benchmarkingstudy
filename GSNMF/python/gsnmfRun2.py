from GeoConstrain import *
import scipy.stats
from sklearn.cluster import SpectralClustering
import matplotlib.pyplot as plt
from scipy.optimize import nnls
from numpy import linalg as LA
from sklearn.decomposition import NMF
import pickle

with open('nmfGCP.pkl', 'rb') as file:
      
    # Call load method to deserialze
    myvar = pickle.load(file)

G = 1e0*myvar[0]
P0 = myvar[1]
C0 = myvar[2]
Ptt = myvar[3]
Wsub = myvar[4]

Ptt = Ptt[:, 9:] # only for the brainlungliver data




m, n = np.shape(G)
k = np.shape(P0)[0]
nn = int(m/k)




rhomin = 1e3
rhomax = 2e3
ratiomin = 1e1
ratiomax = 2e2

tol = 1e-3
err = 1
it = 1
itmax = 1000
rho = np.linspace(rhomin, rhomax, itmax)
rto = 1e-1      # gL constraint parameter

Csum1 = np.sum(C0, axis = 0)
Csumnorm1 = np.sum(1/Csum1)
Cscale1 = (1/Csum1)/Csumnorm1
P0 = np.diag(Cscale1)@P0
colsum = np.sum(P0, axis = 0)
P0 = P0@LA.inv(np.diag(colsum))

C = C0
P = P0
A = C0
Cg = np.zeros((m, k))
for i in range(k):
    Cg[i*nn:(i+1)*nn, i] = 1

C = Cg

tA = np.zeros((m, k))

while it < itmax:
    oldC = C
    oldP = P
    
    step = 1e-5         # solve for A
    err = 2e-3
    itmax2 = 4000
    
    
    dA = A - tA     # solve for C
    Csub = np.zeros((m, k))
    for j in range(m):
        Am = np.sqrt(1 + rho[it])*np.transpose(P)
        bm = (np.transpose(G[j,:]) + rho[it]*np.transpose(P)@np.transpose(dA[j,:]))
        bm = bm/np.sqrt(1 + rho[it])
        r = nnls(Am, bm)        # nonnegatie least square
        r0 = r[0]
        r0[r0 == 0] = 1e-2
        Csub[j,:] = np.transpose(r0)
    C = Csub
    
    
    A = geoconstrain(C, Cg, tA, Wsub, rto, rho[it], step, err, itmax2) 
    tA = tA + (C - A)
    C = A
    
    
    
    Psub = np.zeros((k, n))  
    for i in range(n):  # solve for P
        b = G[:,i]
        r = nnls(C, b)
        r0 = r[0]
        r0[r0 == 0] = 1e-2
        Psub[:, i] = r0
    P = Psub 
    #print(Cscale)
    #P = np.diag(Cscale)@P
    colsum = np.sum(P, axis = 0)
    P = P@LA.inv(np.diag(colsum))
     
    
    
    #error = (LA.norm(C - oldC) + LA.norm(P - oldP))/(LA.norm(C) + LA.norm(P))
    errorC = LA.norm(C - oldC) /LA.norm(C)
    errorP = LA.norm(P - oldP)/LA.norm(P)
    gap = G - C@Psub
    residue = LA.norm(gap)/LA.norm(G)
    print("exterior in C and P, residue: ", errorC, errorP, residue)
    it = it + 1


Csum2 = np.sum(C, axis = 0)
Csumnorm2 = np.sum(1/Csum2)
Cscale2 = (1/Csum2)/Csumnorm2
#Cscale = np.random.permutation(Cscale)
P = np.diag(Cscale2)@P
C = C@LA.inv(np.diag(Cscale2))
colsum = np.sum(P, axis = 0)
P = P@LA.inv(np.diag(colsum))


np.savetxt("prop_output.txt", P, fmt='%.5f')

#np.savetxt("mix_total_t2d_test_sc.txt", C, fmt='%.5f')

#cor1 = np.corrcoef(P[0, :], Ptt[2, :])
#cor2 = np.corrcoef(P[1, :], Ptt[1, :])
#cor3 = np.corrcoef(P[2, :], Ptt[0, :])

#print(cor1)
#print(cor2)
#print(cor3)

#xp = range(n)
#figure, axis = plt.subplots(k)

#axis[0].plot(xp, P[0, :], '*-')
#axis[0].plot(xp, P0[0, :], 'o-')
#axis[0].plot(xp, Ptt[2, :], '>-')
#axis[0].plot(xp, H[2, :], '.-')

#axis[1].plot(xp, P[1, :], '*-')
#axis[1].plot(xp, P0[1, :],'o-')
#axis[1].plot(xp, Ptt[1, :], '>-')
#axis[1].plot(xp, H[0, :], '.-')

#axis[2].plot(xp, P[2, :], '*-')
#axis[2].plot(xp, P0[2, :],'o-')
#axis[2].plot(xp, Ptt[0, :], '>-')
#axis[2].plot(xp, H[1, :], '.-')

#axis[3].plot(xp, P[3, :],'*-')
#axis[3].plot(xp, P0[3, :],'o-')
#axis[3].plot(xp, Ptt[1, :], '>-')
#axis[3].plot(xp, H[3, :], '.-')




plt.show()





print("done")
#from GeoConstrain import *
import numpy as np
import scipy.stats
import pandas as pd
from sklearn.cluster import SpectralClustering
import matplotlib.pyplot as plt
from scipy.optimize import nnls
from numpy import linalg as LA
from sklearn.decomposition import NMF
import pickle


def loadmydata(name,path):
    filename = "%s.txt"%name
    full_path = path + "/" + filename
    #data = np.loadtxt(filename, skiprows = 1, usecols=range(1,34))
    #data = np.loadtxt(filename, skiprows = 1, usecols=range(1,13))
    #geneid = np.genfromtxt(filename, dtype = str, skip_header = 1, usecols = (0))
    df = pd.read_csv(filename, sep='\t')
    df = df.drop(columns=df.columns[0])
    data = df.values
    geneid = df.index.to_numpy()
    return data, geneid

def load_true_prop(name):
    filename = "%s.txt"%name
    df = pd.read_csv(filename, sep='\t', skipinitialspace=True, index_col=0)
    pro = df.values
    pro = pro.astype(np.float64)
    colsum = np.sum(pro, axis = 0)
    Ptt = pro@LA.inv(np.diag(colsum))
    return Ptt
    

k = 6      # number of cell types
nn = 100        # number of marker genes for each type


# load the raw data and simple process     
rawdata, geneid_raw = loadmydata("mixture","c:/user")
Ptt = load_true_prop("proportionsLiverBrainLung")


#rawdata, geneid_raw = loadmydata("T2DCell_pseudo_bulk_counts")
#Ptt = load_true_prop("T2DCell-composition")
#rawdata = rawdata[:,6:]
#Ptt = Ptt[:,6:]

Nsize = np.shape(rawdata)       # size of the raw data
rownorm0 = rawdata.min(axis = 1)
rownorm0[np.where(rownorm0 > 0)] = 1
rownorm = np.linalg.norm(rawdata, axis = 1)*rownorm0
norm_aver = np.average(rownorm)
chosen = np.array(np.where((rownorm < 10*norm_aver) & (rownorm > 0.1*norm_aver)))
data = rawdata[chosen[0]]
geneid = geneid_raw[chosen[0]]



#ndata = data
## column normalize the data============
colsumP0 = np.sum(data, axis = 0)
ndata = data@LA.inv(np.diag(colsumP0))


## row normalize the data======
#rowsum = np.sum(data, axis = 1)
#ndata = LA.inv(np.diag(rowsum))@data
#==============================================================


# graph clustering
N = np.shape(data)[0]           # row size of the initially processed data
ncol = np.shape(data)[1]
W = np.zeros((N, N))
d = np.zeros((N, N))
sig = 0.25

columns_to_choose = ncol
random_column_indices = np.random.choice(ncol, size = columns_to_choose, replace=False)
sdata = ndata[:, random_column_indices]
d = 1 - np.corrcoef(sdata)               # distance matrix
W = np.exp(-np.square(d/sig))           # adjanct matrix
D = np.diag(np.sum(W, axis = 1))
DH = np.diag(np.power(np.sum(W, axis = 1), -0.5))
gL = D - W
gLsym = 1 - DH@W@DH
genesc = SpectralClustering(n_clusters = k, affinity='precomputed').fit(W)
labels = genesc.labels_

  
# pick the marker genes
idlist = []
for i in range(k):
    idlist.append(np.where(labels == i)[0])
    
setlist = []
for i in range(k): 
    setlist.append(data[idlist[i], :])
    
corlist = []
for i in range(k):
    corlist.append(np.corrcoef(setlist[i]))



sub_idlist = []
for i in range(k):
    corlist[i][np.where(corlist[i] < 0.8)] = 0
    csum = np.sum(corlist[i], axis = 0)
    s = np.argsort(-csum)
    sub_idlist.append(idlist[i][s[:nn]])

markeridlist = []
for i in range(k):
    markeridlist.append(geneid[sub_idlist[i]])

markerlist = []
for i in range(k):
    markerlist.append(data[sub_idlist[i]])


sub = np.array([],  dtype = int)
for i in range(k):
    sub = np.concatenate((sub, sub_idlist[i]), axis = 0)

W1 = W[sub, :]
Wsub = W1[:, sub]

## visualization
#ev, ec = np.linalg.eigh(gLsym)
#fig = plt.figure()
#ax = fig.add_subplot(projection='3d')

#ax.scatter(ec[:,0], ec[:,1],  ec[:,2],c=labels)
#ax.scatter(ec[sub_idlist[0], 0], ec[sub_idlist[0],1], ec[sub_idlist[0],2])
#ax.scatter(ec[sub_idlist[1], 0], ec[sub_idlist[1],1], ec[sub_idlist[1],2])
#ax.scatter(ec[sub_idlist[2], 0], ec[sub_idlist[2],1], ec[sub_idlist[2],2])
#ax.scatter(ec[sub_idlist[3], 0], ec[sub_idlist[3],1], ec[sub_idlist[3],2])
#plt.show()

# setup the initial condition of the model
P0 = np.zeros((k, np.shape(data)[1]))
for i in range(k):
    P0[i, :] = np.sum(markerlist[i], axis = 0)/np.shape(markerlist[i])[0]




GG = np.zeros((1, ncol))
for i in range(k):
    GG = np.concatenate((GG, markerlist[i]), axis = 0)
G = GG[1:np.shape(GG)[0],:]
C0 = G@np.transpose(P0)@np.linalg.inv(P0@np.transpose(P0))

myvar = [G, P0, C0, Ptt, Wsub]
  
# Open a file and use dump()
with open('nmfGCP.pkl', 'wb') as file:   
    # A new file will be created
    pickle.dump(myvar, file)

max_len = max(len(arr) for arr in markeridlist)  # Find the longest cluster
matrix = np.full((max_len, len(markeridlist)), np.nan)  # Initialize with NaN for missing values

for i, arr in enumerate(markeridlist):
    matrix[:len(arr), i] = arr  # Fill in the values

# Save markerlist to a text file
with open("markeridlist_output_t2d_bulk.txt", "w") as f:
    # Write column headers
    f.write("\t".join([f"Cluster{i+1}" for i in range(len(markeridlist))]) + "\n")
    # Write matrix
    np.savetxt(f, matrix, fmt='%.0f', delimiter="\t")  # %.0f to remove decimal points




print("done")
# Benchmarking and Evaluation of Deconvolution Algorithms
We present a comprehensive benchmark of the robustness and resilience of computational deconvolution methods for estimating cell type proportions in bulk tissue samples. This study focuses on comparing reference-based and reference-free approaches.  

## Cell level gene expression datasets

Below are all cell-level gene expression datasets used in this study.


| Data           | GSE19830                  | LM22                       | GSE81608                 | GSE67835                  |
|----------------|---------------------------|----------------------------|--------------------------|---------------------------|
| **Tissue Type**      | rat brain, liver, lung     | human blood                | human pancreas           | human brain               |
| **Platform**         | Affymetrix                 | Affymetrix                 | Illumina                 | Illumina                  |
| **Num. of genes**    | 13,841                     | 11,845                     | 39,849                   | 22,088                    |
| **Num. of cells**    | 9                          | 22                         | 1,492                    | 267                       |
| **Num. of cell types** | 3                          | 6                          | 4                        | 5                         |
| **Num. of subjects** | NA                         | NA                         | 18*                      | NA                        |
| **Reference**        | Shen-Orr *et al.* (2010)   | Newman *et al.* (2015)     | Xin *et al.* (2016)      | Darmanis *et al.* (2015)  |

---

| Data           | PBMC8K                   | E-MTAB-5061                | syn18485175              |
|----------------|--------------------------|----------------------------|--------------------------|
| **Tissue Type**      | human peripheral blood     | human pancreas              | human brain              |
| **Platform**         | Illumina                   | Smart-seq2                  | Illumina                 |
| **Num. of genes**    | 32,738                     | 25,453                      | 17,926                   |
| **Num. of cells**    | 8,381                      | 2,209                       | 75,060                   |
| **Num. of cell types** | 10                         | 4                           | 5                        |
| **Num. of subjects** | NA                         | 10**                        | 48                       |
| **Reference**        | 10X Genomics (2022)        | Segerstolpe *et al.* (2016) | Mathys *et al.* (2019)   |

---

**\*** 12 healthy and 6 T2D samples  
**\*\*** 6 healthy and 4 T2D samples

All datasets in this repository are pseudo-bulk data generated from publicly available single-cell RNA-seq (scRNA-seq) datasets.

**E-MTAB-5061** (ArrayExpress accession) and **syn18485175** (which requires access approval via [Synapse](https://www.synapse.org/Synapse:syn18485175)) are used as reference datasets for reference-based deconvolution methods in specific scenarios, but they are not used to generate pseudo-bulk data.

## Simulation Scenarios

The following scenarios were used to generate pseudo-bulk datasets by introducing different perturbations to the original expression levels:

| Scenario | Description |
|----------|-------------|
| **r1** | Mean shifting: Expression levels were augmented by adding **10%** of the average expression level for each cell type. |
| **r2** | Mean shifting: Expression levels were augmented by adding **30%** of the average expression level for each cell type. |
| **r3** | Mean shifting: Expression levels were augmented by adding **50%** of the average expression level for each cell type. |
| **r4** | Mean shifting: Expression levels were augmented by adding **70%** of the average expression level for each cell type. |
| **r5** | Truncation: The top **10%** of expressed cells for each cell type were selectively removed before generating pseudo-bulk tissue data. |
| **r6** | Truncation: The bottom **10%** of expressed cells for each cell type were selectively removed before generating pseudo-bulk tissue data. |
| **r7** | Factoring: Expression levels were scaled using a factor of **1.2** to allow downward adjustments. |
| **r8** | Factoring: Expression levels were scaled using a factor of **1.8** to allow downward adjustments. |
| **r9** | Factoring: Expression levels were scaled using a factor of **0.8** to allow upward adjustments. |
| **r10** | Factoring: Expression levels were scaled using a factor of **0.4** to allow upward adjustments. |

# GSNMF tutorial

**GSNMF** (Geometric Structure-Guided Non-Negative Matrix Factorization) is a reference-free deconvolution algorithm designed for estimating cell type proportions in bulk RNA-seq samples. It leverages geometric structure constraints within the framework of non-negative matrix factorization (NMF). The method was developed by **Dr. Duan Chen**, **Dr. Shaoyu Li**, and **Dr. Xue Wang**, and is published in *Foundations of Data Science*: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10798655/

---

### Download the python code

You can download the Python code from the `GSNMF/python` directory, which contains the following three main files:
- `gsclustering2.py` – for identifying marker genes via clustering
- `gsnmfRun2.py` – for performing deconvolution
- `GeoConstrain.py` – for constrains in algorithm


---

### Getting started with GSNMF

To begin using GSNMF, start with the `gsclustering2.py` file, which performs clustering on the input data to identify marker genes.


```python
k = 4  # Number of cell types
nn = 100 # Number of marker genes to identify per cell type
rawdata, geneid_raw = loadmydata("mixture", "c:/user") # Load your mixture data
```

---

### Deconvolution

Once the initial setup is complete, then you can run `gsnmfrun.py` to perform deconvolution on the mixture data. The resulting cell type proportions will be saved to an output file using the following code:

```python
np.savetxt("prop_output.txt", P, fmt='%.5f')
```

---


### Example

Mixture Dataset: `Dataset/GSE81608/mix_t2d_m.txt`  
Ground Truth Proportion: `Dataset/GSE81608/prop_t2d_m.txt`

To begin, run the `gsclustering2.py` script:

```python
k = 4       # Number of cell types
nn = 100    # Number of marker genes per cell type
rawdata, geneid_raw = loadmydata("mix_t2d_m", "c:/user/GSE81608") # Load your mixture data
```

Then, use `gsnmfrun.py` to estimate the proportions for the mixture dataset `mix_t2d_m.txt` and save as `t2d_m_output_prop.txt`:

```python
np.savetxt("t2d_m_output_prop.txt", P, fmt='%.5f')
```

Compare the estimated proportion (`t2d_m_output_prop.txt`) with the ground truth proportion (`GSE81608/prop_t2d_m.txt`). The figure and results below are generated using R studio:


| Cor.beta     | Cor.alpha    | Cor.delta    | Cor.gamma    | overall.cor  | RMSE     | mAD     |
|----------|----------|----------|----------|----------|----------|---------|
| 0.96780  | 0.98470  | 0.48940  | 0.91490  | 0.94820  | 0.10653  | 0.06967 |

<img src="https://github.com/user-attachments/assets/de4772c2-ccf8-4a66-b10f-bde253f4a33f" alt="Rplot" width="622" height="523">






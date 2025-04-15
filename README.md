# Benchmarking and Evaluation of Deconvolution Algorithms
We present a comprehensive benchmark of the robustness and resilience of computational deconvolution methods for estimating cell type proportions in bulk tissue samples. This study focuses on comparing reference-based and reference-free approaches.  Below are all cell-level gene expression datasets used in this study.


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

All datasets in this repository are pseudo-bulk data generated from publicly available single-cell RNA-seq (scRNA-seq) datasets.

**E-MTAB-5061** (ArrayExpress accession) and **syn18485175** (which requires access approval via [Synapse](https://www.synapse.org/Synapse:syn18485175)) are used as reference datasets for reference-based deconvolution methods in specific scenarios, but they are not used to generate pseudo-bulk data.


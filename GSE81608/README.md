# GSE81608 Dataset Collection

This folder contains simulated and labeled gene expression mixture data derived from the **GSE81608** single-cell RNA-seq dataset of human pancreatic tissue. These datasets are used for benchmarking deconvolution methods in bulk RNA-seq analysis.

## File Descriptions

| File Name                                 | Description                                                                 |
|------------------------------------------|-----------------------------------------------------------------------------|
| `mix_t2d_s.txt`                          | Simulated mixtures with **small** variation level                           |
| `mix_t2d_m.txt`                          | Simulated mixtures with **medium** variation level                          |
| `mix_t2d_l.txt`                          | Simulated mixtures with **large** variation level                           |
| `mix_t2d_rs1.txt` – `mix_t2d_rs10.txt`   | 10 alternative scenarios based on the **medium** variation level, used to assess method robustness and resilience |
| `prop_t2d_s.txt`                         | Ground-truth cell type proportions corresponding to `mix_t2d_s.txt`         |
| `prop_t2d_l.txt`                         | Ground-truth cell type proportions corresponding to `mix_t2d_l.txt`         |
| `prop_t2d_m.txt`                         | Ground-truth cell type proportions corresponding to both `mix_t2d_m.txt` and `mix_t2d_rs1.txt` – `mix_t2d_rs10.txt` |

---

## Dataset Origin

- **Source:** [GSE81608 - NCBI GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE81608)
- **Tissue Type:** Human pancreas
- **Platform:** Illumina
- **Genes:** 39,849
- **Cells:** 1,492
- **Cell Types Used:** 4
- **Subjects:** 18
- **Reference:** Xin *et al.* (2016)

---

## Purpose

These datasets are intended for:
- Evaluating the accuracy and robustness of deconvolution methods
- Testing sensitivity to noise and variation
- Benchmarking across repeated simulation replicates

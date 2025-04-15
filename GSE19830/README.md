# GSE19830 Dataset Collection

This folder contains simulated and labeled gene expression mixture data derived from the **GSE19830** dataset. These datasets are used for benchmarking deconvolution methods in bulk RNA-seq analysis.

## File Descriptions


| File Name                                 | Description                                                                 |
|------------------------------------------|-----------------------------------------------------------------------------|
| `mix_lbl_s.txt`                          | Simulated mixtures with **small** variation level                           |
| `mix_lbl_m.txt`                          | Simulated mixtures with **medium** variation level                          |
| `mix_lbl_l.txt`                          | Simulated mixtures with **large** variation level                           |
| `mix_lbl_m_rs1.txt` – `mix_lbl_m_rs10.txt` | 10 alternative scenarios based on the **medium** variation level, used to assess method robustness and resilience |
| `prop_lbl_s.txt`                         | Ground-truth cell type proportions corresponding to `mix_lbl_s.txt`         |
| `prop_lbl_l.txt`                         | Ground-truth cell type proportions corresponding to `mix_lbl_l.txt`         |
| `prop_lbl_m.txt`                         | Ground-truth cell type proportions corresponding to both `mix_lbl_m.txt` and `mix_lbl_m_rs1.txt` – `mix_lbl_m_rs10.txt` |


---
## Dataset Origin

- **Source:** [GSE19830 - NCBI GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE19830)
- **Tissue Types:** Rat brain, liver, lung
- **Platform:** Affymetrix
- **Genes:** ~13,841
- **Cell Types:** 3
- **Use:** Simulated pseudo-bulk gene expression mixtures based on real single-cell RNA-seq references


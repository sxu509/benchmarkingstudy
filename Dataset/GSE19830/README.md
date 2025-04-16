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



## Scenarios

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



## Dataset Origin

- **Source:** [GSE19830 - NCBI GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE19830)
- **Tissue Types:** Rat brain, liver, lung
- **Platform:** Affymetrix
- **Genes:** ~13,841
- **Cell Types:** 3
- **Reference:** Shen-Orr *et al.* (2010)


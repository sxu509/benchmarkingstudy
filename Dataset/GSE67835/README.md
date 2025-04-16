# GSE67835 Dataset Collection

This folder contains simulated and labeled gene expression mixture data derived from the **GSE67835** dataset. These datasets are used for benchmarking deconvolution methods in bulk RNA-seq analysis.

## File Descriptions

| File Name                                 | Description                                                                 |
|------------------------------------------|-----------------------------------------------------------------------------|
| `mix_hb_marker_s.txt`                          | Simulated mixtures with **small** variation level                           |
| `mix_hb_marker_m.txt`                          | Simulated mixtures with **medium** variation level                          |
| `mix_hb_marker_l.txt`                          | Simulated mixtures with **large** variation level                           |
| `mix_hb_marker_rs1.txt` – `mix_hb_marker_rs10.txt` | 10 alternative scenarios based on the **medium** variation level, used to assess method robustness and resilience |
| `prop_hb_s.txt`                         | Ground-truth cell type proportions corresponding to `mix_hb_marker_s.txt`  and `mix_scdesign_s_ref.txt`        |
| `prop_hb_l.txt`                         | Ground-truth cell type proportions corresponding to `mix_hb_marker_l.txt`  and `mix_scdesign_l_ref.txt`        |
| `prop_hb_m.txt`                         | Ground-truth cell type proportions corresponding to both `mix_hb_marker_m.txt`, `mix_scdesign_m_ref.txt` and `mix_hb_marker_rs1.txt` – `mix_hb_marker_rs10.txt` |
| `mix_scdesign_s_ref.txt`                         | Simulated mixtures from synthetic samples via **scDesign** under **small** variation using scRNA-seq from GSE67835         |
| `mix_scdesign_l_ref.txt`                         | Simulated mixtures from synthetic samples via **scDesign** under **large** variation using scRNA-seq from GSE67835         |
| `mix_scdesign_m_ref.txt`                         | 	Simulated mixtures from synthetic samples via **scDesign** under **medium** variation using scRNA-seq from GSE67835  |


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

- **Source:** [GSE67835 - NCBI GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE67835)
- **Tissue Type:** Human brain
- **Platform:** Illumina
- **Genes:** 22,088
- **Cells:** 267
- **Cell Types Used:** 5
- **Subjects:** NA
- **Reference:** Darmanis *et al.* (2015)


# LM22 Simulated Benchmarking Data

This directory contains simulated pseudo-bulk gene expression datasets based on the **LM22 Source GEPs**. These datasets are used for benchmarking deconvolution methods in bulk RNA-seq analysis.

## File Descriptions



| File Name                                 | Description                                                                 |
|------------------------------------------|-----------------------------------------------------------------------------|
| `mix_lm22_s.txt`                         | Simulated mixtures with **small** variation level                           |
| `mix_lm22_m.txt`                         | Simulated mixtures with **medium** variation level                          |
| `mix_lm22_l.txt`                         | Simulated mixtures with **large** variation level                           |
| `mix_lm22_rs1.txt` – `mix_lm22_rs10.txt` | 10 alternative scenarios based on the **medium** variation level, used to assess method robustness and resilience |
| `prop_lm22_s.txt`                        | Ground-truth cell type proportions corresponding to `mix_lm22_s.txt`        |
| `prop_lm22_m.txt`                        | Ground-truth cell type proportions corresponding to both `mix_lm22_m.txt` and `mix_lm22_rs1.txt` – `mix_lm22_rs10.txt` |
| `prop_lm22_l.txt`                        | Ground-truth cell type proportions corresponding to `mix_lm22_l.txt`        |


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

- **Signature matrix**: LM22 (CIBERSORTx)
- **Tissue Type**: Human blood-derived immune cells
- **Platform**: Affymetrix
- **Number of genes**: ~11,845
- **Number of cell types**: 22
- **Reference**: Newman *et al.* (2015)


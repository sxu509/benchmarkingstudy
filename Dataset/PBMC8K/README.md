
# PBMC8K Dataset Collection

This folder contains simulated gene expression mixtures based on real single-cell RNA-seq data from the **PBMC8K** dataset, using the **LM22 Source GEPs** as the reference for reference-based deconvolution methods. It includes both simulations guided by real cell-type proportions and synthetic simulations generated using **scDesign**.

These datasets are designed to benchmark deconvolution methods under realistic and controlled conditions using peripheral blood mononuclear cells (PBMCs).


## File Descriptions

| File Name                                       | Description                                                                 |
|------------------------------------------------|-----------------------------------------------------------------------------|
| `mix_lm22_pbmc_s_f.txt`                        | Simulated mixtures with **small** variation level using scRNA-seq from PBMC8K |
| `mix_lm22_pbmc_m_f.txt`                        | Simulated mixtures with **medium** variation level using scRNA-seq from PBMC8K |
| `mix_lm22_pbmc_l_f.txt`                        | Simulated mixtures with **large** variation level using scRNA-seq from PBMC8K |
| `lm22_pbmc_real_prop_s.txt`                    | Ground-truth cell type proportions for `mix_lm22_pbmc_s_f.txt`  and   `mix_lm22_pbmc_scdesign_s_f.txt`         |
| `lm22_pbmc_real_prop_m.txt`                    | Ground-truth cell type proportions for `mix_lm22_pbmc_m_f.txt`   and   `mix_lm22_pbmc_scdesign_m_f.txt`             |
| `lm22_pbmc_real_prop_l.txt`                    | Ground-truth cell type proportions for `mix_lm22_pbmc_l_f.txt`   and   `mix_lm22_pbmc_scdesign_l_f.txt`             |
| `mix_lm22_pbmc_scdesign_s_f.txt`               | Simulated mixtures from synthetic samples via **scDesign** under small variation using scRNA-seq from PBMC8K |
| `mix_lm22_pbmc_scdesign_m_f.txt`               | Simulated mixtures from synthetic samples via **scDesign** under medium variation using scRNA-seq from PBMC8K |
| `mix_lm22_pbmc_scdesign_l_f.txt`               | Simulated mixtures from synthetic samples via **scDesign** under large variation using scRNA-seq from PBMC8K |


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

- **Source:** [PBMC8K (10X Genomics)](https://support.10xgenomics.com/single-cell-gene-expression/datasets/2.1.0/pbmc8k)
- **Tissue Type:** Human peripheral blood
- **Platform:** Illumina
- **Genes:** 32,738
- **Cells:** 8,381
- **Cell Types Used:** 10
- **Subjects:** NA
- **Reference:** 10X Genomics (2022)

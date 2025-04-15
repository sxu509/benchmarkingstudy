
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

---

## Dataset Origin

- **Source:** [PBMC8K (10X Genomics)](https://support.10xgenomics.com/single-cell-gene-expression/datasets/2.1.0/pbmc8k)
- **Tissue Type:** Human peripheral blood
- **Platform:** Illumina
- **Genes:** 32,738
- **Cells:** 8,381
- **Cell Types Used:** 10
- **Subjects:** NA
- **Reference:** 10X Genomics (2022)

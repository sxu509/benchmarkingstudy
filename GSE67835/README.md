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
| `mix_scdesign_s_ref.txt`                         | Simulated mixtures from synthetic samples via scDesign under **small** variation using scRNA-seq from GSE67835         |
| `mix_scdesign_l_ref.txt`                         | Simulated mixtures from synthetic samples via scDesign under **large** variation using scRNA-seq from GSE67835         |
| `mix_scdesign_m_ref.txt`                         | 	Simulated mixtures from synthetic samples via scDesign under **medium** variation using scRNA-seq from GSE67835  |

---

## Dataset Origin

- **Source:** [GSE67835 - NCBI GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE67835)
- **Tissue Type:** Human brain
- **Platform:** Illumina
- **Genes:** 22,088
- **Cells:** 267
- **Cell Types Used:** 5
- **Subjects:** NA
- **Reference:** Darmanis *et al.* (2015)


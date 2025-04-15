# LM22 Simulated Benchmarking Data

This directory contains simulated pseudo-bulk gene expression datasets based on the **LM22 Source GEPs**, commonly used in immune deconvolution benchmarking. These files are intended for evaluating the performance of deconvolution algorithms under varying noise conditions and repeated simulations.

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


---
## Dataset Origin

- **Signature matrix**: LM22 (CIBERSORTx)
- **Tissue Type**: Human blood-derived immune cells
- **Platform**: Affymetrix
- **Number of genes**: ~11,845
- **Number of cell types**: 22
- **Reference**: Newman *et al.* (2015)


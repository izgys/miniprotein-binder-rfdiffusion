# De Novo Miniprotein Binder Design with RFdiffusion + Rosetta

**Author:** Iker Zapirain Gysling  
**Project Type:** Generative AI + Computational Protein Design + Structural Bioinformatics  
**Status:** 🚧 In Progress  

---

## Project Overview

This project demonstrates the use of state-of-the-art AI tools to design novel miniprotein binders from scratch, targeting a therapeutically relevant protein. The pipeline integrates RFdiffusion for backbone generation, ProteinMPNN for sequence design, and Rosetta/AlphaFold2 for structure refinement and ranking.

This is a step-by-step, fully documented learning project aimed at:
- Gaining practical experience with generative protein design workflows
- Understanding binder-target interactions
- Building a public portfolio that shows ML + structural bioinformatics integration

---

## Objectives

- Select a therapeutic target with available 3D structure (e.g., IL-6, HER2, PD-1)
- Generate candidate binder backbones with RFdiffusion
- Design sequences with ProteinMPNN
- Predict/refine final binder structures using AlphaFold2 or RosettaRelax
- Rank and filter binders based on scores (pLDDT, Rosetta energy, interface quality)
- Visualize binding interfaces and structural quality with PyMOL
- Maintain a clean, reproducible, and documented GitHub project

---

## Tools and Technologies

| Tool/Library             | Purpose                                                |
|--------------------------|--------------------------------------------------------|
| RFdiffusion              | Backbone generation toward target structure            |
| ProteinMPNN              | Sequence design for generated backbones                |
| AlphaFold2 / ColabFold   | Structure prediction for designed sequences            |
| RosettaRelax / Rosetta scoring | Structure refinement and ranking                 |
| PyMOL / ChimeraX         | Structural visualization of binders and complexes      |
| Python + NumPy + Matplotlib | Data analysis, scoring, visual plots              |
| Git + GitHub             | Version control and documentation                      |

---


## Target Protein

- **Target:** SARS-CoV-2 Spike Receptor Binding Domain (RBD)
- **PDB ID:** [6M0J](https://www.rcsb.org/structure/6M0J)
- **Target Chain:** E (RBD only)
- **Why this target?** Critical for viral entry into human cells, high therapeutic relevance, well-characterized, and widely used in binder design studies.


---

## Workflow Summary

```mermaid
graph TD
    A[Select Target Protein and Structure] --> B[Analyze Binding Interface]
    B --> C[Generate Miniprotein Backbones - RFdiffusion]
    C --> D[Design Sequences - ProteinMPNN]
    D --> E[Predict Structures - AlphaFold2 or RosettaRelax]
    E --> F[Score and Rank Candidates]
    F --> G[Visualize and Analyze Binders]
    G --> H[Summarize Top Designs]
```
---

## Folder Structure

```text
miniprotein-binder-rfdiffusion/  
├── README.md  
├── .gitignore  
├── data/  
│   ├── target/  
│   └── rf_backbones/  
├── notebooks/  
│   └── 01_target_analysis.ipynb  
├── scripts/  
│   └── run_protein_mpnn.py  
├── results/  
│   ├── sequences/  
│   ├── structures/  
│   └── analysis/  
└── logs/  
```

---

## Commit Progress

- Initial commit: project structure and README  
- Added HER2 target PDB and sequence data  
- Generated RFdiffusion backbones  
- Designed sequences with ProteinMPNN  
- Predicted 3D structures with AlphaFold2  
- Scored and ranked designs with Rosetta  
- Added visualizations and summary plots  

---

## Outcomes & Learnings

- Top binder sequences with highest pLDDT / lowest Rosetta energy  
- Interface analysis and contact maps  
- Reflections on RFdiffusion usability and binder design challenges  

---

## References

- https://github.com/RosettaCommons/RFdiffusion  
- https://github.com/dauparas/ProteinMPNN  
- https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2_mmseqs2.ipynb  
- https://www.rosettacommons.org/  
- https://www.rcsb.org/  

---

This project is a part of a series of portfolio projects focused on AI-driven protein design for drug discovery and biotechnology.


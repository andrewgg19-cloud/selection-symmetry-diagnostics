# Selection Symmetry Diagnostics

**Author:** German Garcia

This repository contains the reproducible materials for the manuscript:

**Selection Symmetry as an Operational Diagnostic for Correlations under Data Filtering**

Core contribution:

> A reproducible and interdisciplinary framework for diagnosing when a correlation is invariant under data selection and when it can be explained as information introduced by the filtering mechanism itself.

The repository includes the manuscript, figures, scripts, result tables, citation metadata, license, and submission materials.

## Reproducibility

Install dependencies:

```bash
pip install -r requirements.txt
python scripts/run_all.py
latexmk -pdf paper/main.tex
```

## Scope

This work is a model-independent operational diagnostic. It does not propose new physics and does not reinterpret established experiments as invalid. It provides reproducible stress tests for selection symmetry, biased filtering, information bounds, and robustness of correlations under data selection.


# Production-Line-Performance-Analyzer-Manufacturing-Analytics-
Analyze machine performance, downtime, throughput, and quality across production shifts to identify bottlenecks and propose improvements that increase yield and reduce unplanned downtime.
# Production Line Performance Analyzer

**Domain:** Manufacturing / Mechanical Industry Analytics  
**Project Type:** Data Analytics — EDA, KPI calculation, visualization, basic insights

## Project Summary
Analyze production line data to find bottlenecks, identify machines needing maintenance, measure yield, and produce actionable recommendations to improve throughput and reduce defects.

## Contents
- `data/production_line_data.csv` — dataset (synthetic)
- `src/data_generation.py` — script to reproduce dataset
- `src/analysis.py` — analysis script (produces outputs)
- `notebooks/analysis.ipynb` — exploratory notebook (optional)
- `outputs/` — generated summaries and figures
- `linkedin_caption.txt` — ready-to-post LinkedIn caption

## How to run
1. Create virtual environment and install packages:
   ```bash
   python -m venv venv
   source venv/bin/activate   # or venv\\Scripts\\activate on Windows
   pip install pandas matplotlib numpy jupyter

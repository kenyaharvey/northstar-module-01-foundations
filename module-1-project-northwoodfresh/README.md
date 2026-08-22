# NorthwoodFresh Southeast Diagnosis

## What is this?
The name of the project is The NorthwoodFresh Southeast Diagnosis. The client is Sven Anderson. The question being investigated is whether NorthwoodFresh's Southeast region revenue drop to a new, lower level is a real, statistically significant change or could be explained by normal random variation.

## What's in the folder?
- `generate_northwoodfresh_data.py` — generates the synthetic sales dataset and saves it as a CSV
- `northwoodfresh_sales.csv` — the generated dataset (48 rows: 4 regions x 12 months)
- `northwoodfresh_analysis.ipynb` — the full analysis notebook (data inspection, summary stats, visualizations, and the Southeast statistical test)
- `sven_anderson_memo.md` — the 1-page executive memo summarizing findings for the client
- `README.md` — this file

## How to reproduce the analysis
1. Activate the conda environment: `conda activate northstar`
2. Run the data generation script: `python generate_northwoodfresh_data.py`
3. Open the notebook: `northwoodfresh_analysis.ipynb`
4. Run it top to bottom using the `northstar` kernel

## The headline finding
Southeast's monthly revenue dropped by $98,887.74 (21.43%) after the mid-year change, with a 95% confidence interval of $74,410.93 to $123,364.55 that notably excludes zero. The t-test confirms this is statistically significant (p = 0.000013), far below the typical 0.05 threshold, the drop is highly unlikely to be random chance. Together, these numbers show a real, substantial decline in Southeast's revenue, not just noise.


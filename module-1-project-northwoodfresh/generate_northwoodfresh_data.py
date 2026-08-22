import numpy as np
import pandas as pd

np.random.seed(42)

region_baselines = {
    'Northeast': 520000,
    'Southeast': {**{month: 480000 for month in range(1, 7)}, **{month: 370000 for month in range(7, 13)}},
    'Midwest': 510000,
    'West': 590000,
}

rows = []

for region, baseline in region_baselines.items():
    for month in range(1, 13):
        if isinstance(baseline, dict):
            month_baseline = baseline[month]
        else:
            month_baseline = baseline
        std_dev = 0.05 * month_baseline
        revenue = np.random.normal(loc=month_baseline, scale=std_dev)
        rows.append({'region': region, 'month': month, 'revenue': revenue})

df = pd.DataFrame(rows)
df['revenue'] = df['revenue'].round(2)
df.to_csv('northwoodfresh_sales.csv', index=False)

print("=== Verification ===")
print(f"Total rows: {len(df)}")
print()
print("Mean revenue per region:")
print(df.groupby('region')['revenue'].mean())
print()

southeast = df[df['region'] == 'Southeast']
southeast_h1 = southeast[southeast['month'] <= 6]['revenue'].mean()
southeast_h2 = southeast[southeast['month'] >= 7]['revenue'].mean()

print(f"Southeast mean, months 1-6: {southeast_h1:.2f}")
print(f"Southeast mean, months 7-12: {southeast_h2:.2f}")


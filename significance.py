import pandas as pd
from statsmodels.stats.proportion import proportions_ztest

df = pd.read_csv('experiment_results.csv')
q2_stats = df.groupby(['segment', 'variant'])['converted'].agg(['count', 'sum']).unstack()

for segment in q2_stats.index:
    count_ctrl = q2_stats.loc[segment, ('count', 'control')]
    )
    print(f"{segment}: p-value = {pval:.4f}")

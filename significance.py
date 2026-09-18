import pandas as pd
from statsmodels.stats.proportion import proportions_ztest

df = pd.read_csv('experiment_results.csv')
q2_stats = df.groupby(['segment', 'variant'])['converted'].agg(['count', 'sum']).unstack()

for segment in q2_stats.index:
    count_ctrl = q2_stats.loc[segment, ('count', 'control')]
    count_trt = q2_stats.loc[segment, ('count', 'treatment')]
    success_ctrl = q2_stats.loc[segment, ('sum', 'control')]
    success_trt = q2_stats.loc[segment, ('sum', 'treatment')]
    
    counts = [success_trt, success_ctrl]
    nobs = [count_trt, count_ctrl]
    stat, pval = proportions_ztest(counts, nobs)
    print(f"{segment}: p-value = {pval:.4f}")

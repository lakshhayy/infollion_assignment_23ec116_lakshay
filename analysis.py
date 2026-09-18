import pandas as pd

df = pd.read_csv('experiment_results.csv')

print("=== Q1 ===")
q1_stats = df.groupby('variant')['converted'].agg(['count', 'mean'])
n_control = q1_stats.loc['control', 'count']
n_treatment = q1_stats.loc['treatment', 'count']
cr_control = q1_stats.loc['control', 'mean']
cr_treatment = q1_stats.loc['treatment', 'mean']
naive_lift_pp = (cr_treatment - cr_control) * 100
print(f"naive_lift_pp: {naive_lift_pp}")
print(f"n_control: {n_control}")
print(f"n_treatment: {n_treatment}")
print(f"cr_control: {cr_control}")
print(f"cr_treatment: {cr_treatment}")

print("\n=== Q2 ===")
q2_stats = df.groupby(['segment', 'variant'])['converted'].agg(['count', 'mean']).unstack()
print(q2_stats)

print("\n=== Q3 ===")
total_users = len(df)
segment_shares = df.groupby('segment').size() / total_users
segment_lifts = q2_stats[('mean', 'treatment')] - q2_stats[('mean', 'control')]
mix_adjusted_lift = (segment_lifts * segment_shares).sum()
mix_adjusted_lift_pp = mix_adjusted_lift * 100
print(f"mix_adjusted_lift_pp: {mix_adjusted_lift_pp}")

print("\n=== Q5 ===")
variant_shares_by_segment = df.groupby('segment')['variant'].value_counts(normalize=True).unstack()
print(variant_shares_by_segment)

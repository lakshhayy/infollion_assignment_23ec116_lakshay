import scipy.stats as stats

# referral
as + trt_conv_as) / (ctrl_n_as + trt_n_as)

se_as = (p_pool_as * (1 - p_pool_as) * (1/ctrl_n_as + 1/trt_n_as)) ** 0.5
z_as = (p_trt_as - p_ctrl_as) / se_as
p_value_as = 2 * (1 - stats.norm.cdf(abs(z_as)))

print(f"App store z-score: {z_as}")
print(f"App store p-value: {p_value_as}")

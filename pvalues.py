import scipy.stats as stats

# referral
ctrl_conv = 338
ctrl_n = 1441
trt_conv = 367
trt_n = 1397

# Two-proportion z-test
p_ctrl = ctrl_conv / ctrl_n
p_trt = trt_conv / trt_n
p_pool = (ctrl_conv + trt_conv) / (ctrl_n + trt_n)

se = (p_pool * (1 - p_pool) * (1/ctrl_n + 1/trt_n)) ** 0.5
z = (p_trt - p_ctrl) / se
p_value = 2 * (1 - stats.norm.cdf(abs(z)))

print(f"Referral z-score: {z}")
print(f"Referral p-value: {p_value}")

# app_store
ctrl_conv_as = 81
ctrl_n_as = 925
trt_conv_as = 192
trt_n_as = 960

p_ctrl_as = ctrl_conv_as / ctrl_n_as
p_trt_as = trt_conv_as / trt_n_as
p_pool_as = (ctrl_conv_as + trt_conv_as) / (ctrl_n_as + trt_n_as)

se_as = (p_pool_as * (1 - p_pool_as) * (1/ctrl_n_as + 1/trt_n_as)) ** 0.5
z_as = (p_trt_as - p_ctrl_as) / se_as
p_value_as = 2 * (1 - stats.norm.cdf(abs(z_as)))

print(f"App store z-score: {z_as}")
print(f"App store p-value: {p_value_as}")

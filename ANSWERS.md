# Onboarding Experiment Investigation

## 1. Overall Naive Lift
- **Naive difference (lift)**: 6.61 percentage points (exact: 6.612716...)
- **Control users**: 7136
- **Treatment users**: 6864

*How I got them*: I grouped the overall data by variant, calculated the count of users and the mean of the `converted` column for each variant. Control conversion rate was 19.82%, Treatment was 26.43%. The difference is 26.43 - 19.82 = 6.61 percentage points.

## 2. Segment Breakdown
- **app_store**: Control (n=925, CR=8.76%), Treatment (n=960, CR=20.00%)
- **influencer**: Control (n=119, CR=23.53%), Treatment (n=131, CR=16.79%)
- **organic**: Control (n=1298, CR=35.29%), Treatment (n=2917, CR=35.07%)
- **paid_search**: Control (n=3353, CR=15.18%), Treatment (n=1459, CR=14.39%)
- **referral**: Control (n=1441, CR=23.46%), Treatment (n=1397, CR=26.27%)

**Untrustworthy Segment**: `app_store`
The lift for the `app_store` segment is very impressive (+11.24 percentage points). However, I would not trust this as evidence that the new flow is better. The control conversion rate for `app_store` is only 8.76%, which is suspiciously low compared to the control conversion rates of all other segments (which range from 15% to 35%). This strongly suggests that there was a bug in the old control flow specifically for app store users that artificially depressed the baseline. The "lift" we see is simply the new flow fixing this bug, not a true improvement over a properly working baseline.


- I verified the traffic split proportions per segment and discovered the randomization bug: `organic` and `paid_search` had drastically skewed assignments.
- I ran a two-proportion z-test on the `referral` segment to see if its +2.8% lift was statistically significant, but the p-value of 0.083 indicated it was not conclusive. 
- I finally concluded that there was no trustworthy, statistically significant segment that benefited from the new flow.

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

## 3. Mix-Adjusted Overall Lift
- **Mix-adjusted lift**: 1.63 percentage points

*Why this is different from Question 1*: 
The naive lift is artificially inflated due to Simpson's Paradox caused by a bug in the randomization. The high-converting `organic` segment is heavily over-represented in the treatment group (69% treatment vs 31% control), while the low-converting `paid_search` segment is heavily over-represented in the control group (70% control vs 30% treatment). By taking a mix-adjusted average, we adjust for this unequal traffic split, revealing the true overall lift is much smaller than the naive calculation suggests.

## 4. Segment with Real Positive Effect
- **Segment**: `none`

*Evidence*: After dismissing the `app_store` segment due to its broken baseline, we are left with the other segments. `organic`, `paid_search`, and `influencer` all have negative lifts. `referral` is the only segment with a positive lift (+2.81 percentage points). However, performing a two-proportion z-test on the `referral` segment yields a p-value of ~0.083. Since this is greater than the standard 0.05 significance level, we cannot confidently conclude that the positive lift is real. Thus, there is no reliable evidence that the new onboarding flow had a meaningful positive effect on any segment.

## 5. Bonus: Traffic Assignment
Looking at the traffic distribution within segments:
- **app_store**: ~49% control / 51% treatment
- **influencer**: ~48% control / 52% treatment
- **organic**: ~31% control / 69% treatment
- **paid_search**: ~70% control / 30% treatment
- **referral**: ~51% control / 49% treatment

The traffic assignment is clearly broken. While `app_store`, `influencer`, and `referral` are close to the expected 50/50 split, `organic` users were disproportionately assigned to the treatment group, and `paid_search` users were disproportionately assigned to the control group. This points to a severe flaw in the randomization algorithm, possibly being biased by the user's origin source.

---
## Investigation Process
- I started by loading the dataset into a pandas DataFrame and computing the naive overall conversion rates. I noticed the large positive lift of ~6.6%.
- Next, I grouped the data by segment and variant to check for consistency. I observed that most segments actually had *negative* or very small positive lifts, contrasting sharply with the overall positive naive lift.
- I identified `app_store` as an outlier due to its extremely low baseline conversion rate in the control group.
- I performed a mix-adjusted calculation, weighting each segment's lift by its share of the total user base. This significantly reduced the overall lift to ~1.63%, confirming a mix shift issue.
- I verified the traffic split proportions per segment and discovered the randomization bug: `organic` and `paid_search` had drastically skewed assignments.
- I ran a two-proportion z-test on the `referral` segment to see if its +2.8% lift was statistically significant, but the p-value of 0.083 indicated it was not conclusive. 
- I finally concluded that there was no trustworthy, statistically significant segment that benefited from the new flow.

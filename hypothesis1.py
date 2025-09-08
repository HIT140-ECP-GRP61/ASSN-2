import pandas as pd
from scipy.stats import ttest_ind

df = pd.read_csv('cleaned_dataset1.csv')

import pandas as pd
import scipy as st
from scipy.stats import ttest_ind
import statistics as stats
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('cleaned_dataset1.csv')

# BAT LANDING TO FOOD COLUMN (RATIO DATA)
# central tendency
bat_landing_to_food = df["bat_landing_to_food"]

mean_landing = stats.mean(bat_landing_to_food) # average time the bat took to go for food
median_landing = stats.median(bat_landing_to_food) # skewness
sample_size_landing = bat_landing_to_food.size
variance_landing = bat_landing_to_food.var(ddof=1) # ddof is the degrees of freedom calculation (sample size - 1)
standard_deviation_landing = bat_landing_to_food.std(ddof=1)

# Compare risk boolean value to corresponding bat seconds
avoidance_times = df.loc[df['risk'] == 0, 'bat_landing_to_food']
risk_times = df.loc[df['risk'] == 1, 'bat_landing_to_food']

avoidance_mean = stats.mean(avoidance_times)
risk_mean = stats.mean(risk_times)
avoidance_variance = avoidance_times.var(ddof=1) # ddof is the degrees of freedom calculation (sample size - 1)
avoidance_standard_deviation = avoidance_times.std(ddof=1) 
risk_variance = risk_times.var(ddof=1) 
risk_standard_deviation = risk_times.std(ddof=1)

print("Avoidance/Risk Mean: ", avoidance_mean, risk_mean)
print("Avoidance/Risk Standard Deviation: ", avoidance_standard_deviation, risk_standard_deviation)


# IQR (detecting outliers?) #TODO IQR for the risk/avoidance
percentile25th = np.percentile(bat_landing_to_food, 25)
percentile75th = np.percentile(bat_landing_to_food, 75)

avoidance_iqr = percentile75th - percentile25th

a_val = 1.5 * avoidance_iqr
print(percentile25th, "75th ", percentile75th, avoidance_iqr, a_val)
aQ1 = percentile25th - a_val # producing a negative value from the extreme low values (0.0000001), resort to using 0?
aQ3 = percentile75th + a_val

print("IQR: ", aQ1, aQ3)

filtered_df = df[df['bat_landing_to_food'] > aQ3]
filtered_low = df[df['bat_landing_to_food'] < 1.0]
print(filtered_df["bat_landing_to_food"], filtered_low["bat_landing_to_food"])

# Histogram(s)
max_val = avoidance_times.max()
min_val = avoidance_times.min()
the_range = max_val - min_val
bin_width = 5
bin_count= int(the_range/bin_width)
plt.hist(avoidance_times, color='red', edgecolor='black', bins=bin_count)
plt.title("Histogram of Avoidance Bats")
plt.xlabel("Avoidance times (sec)")
plt.ylabel("Frequency")
plt.show()

max_val = risk_times.max()
min_val = risk_times.min()
the_range = max_val - min_val
bin_width = 5
bin_count= int(the_range/bin_width)
plt.hist(risk_times, color='red', edgecolor='black', bins=bin_count)
plt.title("Histogram of Risk Taking Bats")
plt.xlabel("Risk times (sec)")
plt.ylabel("Frequency")
plt.show()

'''
Hypothesis 1: Avoidance divided by risky/avoidant bats
<br />
Variables:<br />
   risk — split into risky/avoidant bats
   <br />
    test: compare bat_landing_to_food (how much they hesitate after landing)
    <br />
Hypotheses :<br />
     H0: Risky bats and avoidant bats take equally long to approach food.<br />
    H1: Risky and avoidant bats take different time to approach food when they land soon after rat arrival ( vigilance).<br />

'''
risky_group = df[df['risk'] == 1]['bat_landing_to_food']
avoidant_group = df[df['risk'] == 0]['bat_landing_to_food']

t_stat, p_value = ttest_ind(risky_group.dropna(), avoidant_group.dropna())

print(f"T-statistic: {t_stat}, P-value: {p_value}")

if p_value < 0.05:
    print("Reject the null hypothesis: There is a significant difference between risky and avoidant bats in their approach time to food.")
else:
    print("Fail to reject the null hypothesis: No significant difference between risky and avoidant bats in their approach time to food.")

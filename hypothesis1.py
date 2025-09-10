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

mean_landing = stats.mean(bat_landing_to_food) 
median_landing = stats.median(bat_landing_to_food) 
sample_size_landing = bat_landing_to_food.size
variance_landing = bat_landing_to_food.var(ddof=1) 
standard_deviation_landing = bat_landing_to_food.std(ddof=1)


# Compare risk boolean value to corresponding bat seconds
avoidance_times = df.loc[df['risk'] == 0, 'bat_landing_to_food']
risk_times = df.loc[df['risk'] == 1, 'bat_landing_to_food']

# Histogram(s)
max_val = avoidance_times.max()
min_val = avoidance_times.min()
the_range = max_val - min_val
bin_width = 5
bin_count= int(the_range/bin_width)

r_max_val = avoidance_times.max()
r_min_val = avoidance_times.min()
r_the_range = r_max_val - r_min_val

r_bin_count= int(r_the_range/bin_width)

plt.hist(avoidance_times, color='red', edgecolor='black', bins=bin_count, alpha=0.6)
plt.hist(risk_times, color='green', edgecolor='black', bins=r_bin_count, alpha=0.6)
plt.title("Histogram of Avoidance (Green) and Risky Bats (Red)")
plt.xlabel("Avoidance/Risk time (sec)")
plt.ylabel("Frequency")
plt.show()

avoidance_mean = stats.mean(avoidance_times)
risk_mean = stats.mean(risk_times)
avoidance_variance = avoidance_times.var(ddof=1) # ddof is the degrees of freedom calculation (sample size - 1)
avoidance_standard_deviation = avoidance_times.std(ddof=1) 
risk_variance = risk_times.var(ddof=1) 
risk_standard_deviation = risk_times.std(ddof=1)

print("Avoidance/Risk Mean: ", avoidance_mean, risk_mean)
print("Avoidance/Risk Median: ", stats.median(avoidance_times), stats.median(risk_times))

# Calculate Q1 and Q3
Q1 = np.percentile(avoidance_times, 25)
Q3 = np.percentile(avoidance_times, 75)
# Calculate IQR
IQR = Q3 - Q1
# Calculate the 1.5 * IQR factor
iqr_factor = 1.5 * IQR
# Calculate lower and upper bounds
lower_bound = max(0, Q1 - iqr_factor)  # Time can't be negative
upper_bound = Q3 + iqr_factor
print("IQR: ", IQR, iqr_factor, lower_bound, upper_bound)

filtered_lower = avoidance_times[avoidance_times <= 0]
filtered_upper = avoidance_times[avoidance_times >= 13.5]
filtered = avoidance_times[(avoidance_times >= lower_bound) & (avoidance_times <= upper_bound)]
print(len(filtered))
print("times ", len(filtered_lower), len(filtered_upper))

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

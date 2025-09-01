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

print("Central Tendency (Mean, Median, Sample Size): ", mean_landing, median_landing, sample_size_landing)

# dispersion
variance_landing = bat_landing_to_food.var(ddof=1) # ddof is the degrees of freedom calculation (sample size - 1)
standard_deviation_landing = bat_landing_to_food.std(ddof=1)
# The variance describes how much, on average, all values in a series vary around the mean
print("Variance: ", variance_landing)
print("Standard Deviation: ", standard_deviation_landing)

# IQR (detecting outliers?)
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


max_val = bat_landing_to_food.max()
min_val = bat_landing_to_food.min()
the_range = max_val - min_val
bin_width = 5
bin_count= int(the_range/bin_width)

print("Range: ", the_range)

# plot histogram
plt.hist(bat_landing_to_food, color='red', edgecolor='black', bins=bin_count)
plt.title("Histogram of Landing to Food")
plt.xlabel("Delay (sec)")
plt.ylabel("Frequency")
plt.show()

risk = df['risk']
avoidance_bool = risk == 0
risky_bool = risk == 1

num_avoidant_bats = avoidance_bool.sum()
num_risky_bats = risky_bool.sum()

# Compare risk boolean value to corresponding bat seconds
avoidance_times = df.loc[avoidance_bool, 'bat_landing_to_food']
risk_times = df.loc[risky_bool, 'bat_landing_to_food']

avoidance_mean = stats.mean(avoidance_times)
risk_mean = stats.mean(risk_times)
#06.00 - 18.00 = 6AM - 6PM 
#17.59 - 05.59 = 6PM - 6AM
avoidance_variance = avoidance_times.var(ddof=1) # ddof is the degrees of freedom calculation (sample size - 1)
avoidance_standard_deviation = avoidance_times.std(ddof=1) 
risk_variance = risk_times.var(ddof=1) 
risk_standard_deviation = risk_times.std(ddof=1)

print("Avoidance/Risk Mean: ", avoidance_mean, risk_mean)
print("Avoidance/Risk Standard Deviation: ", avoidance_standard_deviation, risk_standard_deviation)

max_val = avoidance_times.max()
min_val = avoidance_times.min()
the_range = max_val - min_val

print("Avoidance max/min/range: ", max_val, min_val, the_range)
bin_width = 5
bin_count= int(the_range/bin_width)
# plot histogram
plt.hist(avoidance_times, color='red', edgecolor='black', bins=bin_count)
plt.title("Histogram of Avoidance Bats")
plt.xlabel("Avoidance times (sec)")
plt.ylabel("Frequency")
plt.show()

max_val = risk_times.max()
min_val = risk_times.min()
the_range = max_val - min_val
print("Risk max/min/range: ", max_val, min_val, the_range)
bin_width = 5
bin_count= int(the_range/bin_width)
# plot histogram
plt.hist(risk_times, color='red', edgecolor='black', bins=bin_count)
plt.title("Histogram of Risk Taking Bats")
plt.xlabel("Risk times (sec)")
plt.ylabel("Frequency")
plt.show()



# RISK COLUMN (CATEGORIAL DATA)
risk = df["risk"]
# central tendency
mean_risk = stats.mean(risk)
sample_size_risk = risk.size

# dispersion

variance_risk = risk.var(ddof=1) # ddof is the degrees of freedom calculation (sample size - 1)
standard_deviation_risk = risk.std(ddof=1)

# plot histogram
plt.hist(risk, color='red', edgecolor='black', bins=10)
plt.title("Histogram of Risk Taking")
plt.xlabel("Risk")
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

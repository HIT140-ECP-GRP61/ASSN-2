import pandas as pd
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('cleaned_dataset1.csv')

median_time = df['seconds_after_rat_arrival'].median()
df['group'] = df['seconds_after_rat_arrival'] < median_time
early_group = df.loc[df['group'], 'bat_landing_to_food']
late_group = df.loc[~df['group'], 'bat_landing_to_food']

print("Early: ", early_group.describe())
print("Late: ", late_group.describe())

mean_early = early_group.mean()
median_early = early_group.median()
standard_deviation_early = early_group.std(ddof=1)

mean_late = late_group.mean()
median_late = late_group.median()
standard_deviation_late = late_group.std(ddof=1)


# IQR (detecting outliers?) #TODO late group IQR
Q1 = np.percentile(early_group, 25)
Q3 = np.percentile(early_group, 75)

IQR = Q3 - Q1

a_val = 1.5 * IQR
print(Q1, "75th ", Q3, IQR, a_val)
lower_bound = Q1 - a_val 
upper_bound = Q3 + a_val

print(lower_bound, upper_bound)

filtered = early_group[early_group <= upper_bound]

#histograms
max_val_early = early_group.max()
min_val_early = early_group.min()
the_range_early = max_val_early - min_val_early
bin_width = 5
bin_count_early= int(the_range_early/bin_width)

max_val = late_group.max()
min_val = late_group.min()
the_range_late = max_val - min_val
bin_count= int(the_range_late/bin_width)

plt.hist(early_group, bins=bin_count_early, alpha=0.6, label='Early Arrival Bats', color='red', edgecolor='black')
plt.hist(late_group, bins=bin_count, alpha=0.6, label='Late Arrival Bats', color='green', edgecolor='black')
plt.title('Bat Hesitation Time Based on Rat Arrival (Early=Red Late=Green)')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.show()

'''
Hypothesis 3: Do bats hesitate more when rats just arrived?<br />
Variables:<br />
test:<br />
Group A (high threat): Bats that landed within median seconds of rat arrival<br />
Group B (low threat): Bats that landed after median seconds <br />
Compare:<br />
bat_landing_to_food (hesitation time)<br />
Hypotheses:<br />

H₀ (null): There is no difference in mean hesitation between early/late landers after rat arrival<br />

H₁ (alt): Bats that land soon after rats arrive hesitate longer (↑ bat_landing_to_food)<br />
'''
median = df['seconds_after_rat_arrival'].median()

df['near'] = df['seconds_after_rat_arrival'] <= median
df['not_near'] = df['seconds_after_rat_arrival'] > median

near = df[df['near']]['bat_landing_to_food']
not_near = df[df['not_near']]['bat_landing_to_food']

t_stat, p_value = ttest_ind(near.dropna(), not_near.dropna())

print(f"T-statistic: {t_stat}, P-value: {p_value}")

if p_value < 0.05:
    print("There is significant difference in mean hesitation between early/late landers after rat arrival")
else:
    print("Fail to reject the null hypothesis. There is no difference in mean hesitation between early/late landers after rat arrival.")

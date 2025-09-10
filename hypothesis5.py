import pandas as pd
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('cleaned_dataset2.csv')

median = df['rat_minutes'].median()

df['rat_present'] = df['rat_minutes'] > median
print(df['rat_present'].value_counts())

rat_present = df.loc[df['rat_present'], 'bat_landing_number']
rat_absent = df.loc[~df['rat_present'], 'bat_landing_number']

mean_present = rat_present.mean()
median_present = rat_present.median() # Skewed data, use median
present_standard_deviation = rat_present.std(ddof=1)

mean_absent = rat_present.mean()
median_absent = rat_absent.median() # Skewed data, use median
absent_standard_deviation = rat_absent.std(ddof=1)

print("Rats Present: ", rat_present.describe(), median_present, "\nRats Absent: ", rat_absent.describe(), median_absent)

#IQR for present and absent (median)
Q1 = np.percentile(rat_present, 25)
Q3 = np.percentile(rat_present, 75)

IQRp = Q3 - Q1

a_val = 1.5 * IQRp
lower_bound = Q1 - a_val 
upper_bound = Q3 + a_val

# 83.5 upper bound
print("Q1: ", lower_bound, " Q3: ", upper_bound)

absent_Q1 = np.percentile(rat_absent, 25)
absent_Q3 = np.percentile(rat_absent, 75)

rats_absent_iqr = absent_Q3 - absent_Q1

a_val = 1.5 * rats_absent_iqr
lower_bounda = absent_Q1 - a_val 
upper_bounda = absent_Q3 + a_val

# 107.0 upper bound
print("Q1: ", lower_bounda, " Q3: ", upper_bounda)

# Remove outliers and view data
cleaned_present = rat_present[(rat_present <= upper_bound) & (rat_present >= lower_bound)]
cleaned_absent = rat_absent[(rat_absent <= upper_bounda) & (rat_absent >= lower_bounda)]

# histograms
max_val_present = rat_present.max()
min_val_present = rat_present.min()
the_range_present = max_val_present - min_val_present
bin_width = 5
bin_count_present= int(the_range_present/bin_width)

max_val = rat_absent.max()
min_val = rat_absent.min()
the_range = max_val - min_val
bin_count= int(the_range/bin_width)

plt.hist(rat_present, bins=bin_count_present, alpha=0.6, color='red', edgecolor='black')
plt.hist(rat_absent, bins=bin_count, alpha=0.6, color='green', edgecolor='black')
plt.title('Bat Landings for High and Low Rat Presence (Red=Present Green=Absent)')
plt.xlabel('Bat Landing Number')
plt.ylabel('Frequency')
plt.show()


'''
Hypothesis 5: Rat Presence Reduces Bat Traffic<br />
Variables:<br />
test:<br />
     High vs. Low rat_minutes<br />
Compare:<br />
    bat_landing_number<br />
Hypotheses:<br />
    H0: Rats being around doesn't affect how many bats come.<br />
    H1: Bats land less often when rats dominate the platform. <br />

'''
median= df['rat_minutes'].median()
df['high_rat_minutes'] = df['rat_minutes'] > median

high_group = df[df['high_rat_minutes']]['bat_landing_number']
low_group = df[~df['high_rat_minutes']]['bat_landing_number']

t_stat, p_value = ttest_ind(low_group, high_group, equal_var=False)

print(f"  t-statistic = {t_stat:.3f}")
print(f"  p-value     = {p_value:.6f}")

if p_value < 0.05:
    print("Bats land less often when rats dominate the platform.")
else:
    print("Rats being around doesn't affect how many bats come.")

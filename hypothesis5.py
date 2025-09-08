import pandas as pd
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

df = pd.read_csv('cleaned_dataset2.csv')

median = df['rat_minutes'].median()
print(median)
df['rat_present'] = df['rat_minutes'] > median
print(df['rat_present'].value_counts())

rat_present = df.loc[df['rat_present'], 'bat_landing_number']
rat_absent = df.loc[~df['rat_present'], 'bat_landing_number']
print("presence: ", rat_present.mean())
print("absence: ", rat_absent.mean()) # more traffic when less rats

mean_present = rat_present.mean()
median_present = rat_present.median()
present_standard_deviation = rat_present.std(ddof=1)

mean_absent = rat_present.mean()
median_absent = rat_absent.median()
absent_standard_deviation = rat_absent.std(ddof=1)


#IQR for present and absent


#TODO histograms
max_val_present = rat_present.max()
min_val_present = rat_present.min()
the_range_present = max_val_present - min_val_present
bin_width = 5
bin_count_present= int(the_range_present/bin_width)

max_val = rat_absent.max()
min_val = rat_absent.min()
the_range = max_val - min_val
bin_count= int(the_range/bin_width)

plt.hist(rat_present, bins=bin_count_present, alpha=0.6, label='Risky Reward Bats', color='red', edgecolor='black')
plt.hist(rat_absent, bins=bin_count, alpha=0.6, label='Avoidant Reward Bats', color='green', edgecolor='black')
plt.title('Bat Presence for High and Low Rat Presence')
plt.xlabel('Rat Presence')
plt.ylabel('Bat Frequency')
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

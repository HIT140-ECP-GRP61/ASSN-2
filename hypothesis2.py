import pandas as pd
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('cleaned_dataset1.csv')

start_time = pd.to_datetime(df['start_time'], dayfirst=False)
rat_period_start = pd.to_datetime(df['rat_period_start'], dayfirst=False)
rat_period_end = pd.to_datetime(df['rat_period_end'], dayfirst=False)
# start time is later than all rat start time and earlier than all rat end time (rats always present)
df['rats_present'] = ((start_time >= rat_period_start) & (start_time <= rat_period_end)) 

rats_present_group = df[df['rats_present'] == True]['bat_landing_to_food']
rats_absent_group = df[df['rats_present'] == False]['bat_landing_to_food']

# continue with knowing there are 0 absent, use present rats only

print("Rats present Mean: ", rats_present_group.mean())
print("Rats absent Mean: ", rats_absent_group.mean()) # NaN

print("Rats present: ", rats_present_group.describe())
print("Rats absent: ", rats_absent_group.describe())
mean = rats_present_group.mean()
median = rats_present_group.median()

standard_deviation = rats_present_group.std(ddof=1)

# Calculate Q1 and Q3
Q1 = np.percentile(rats_present_group, 25)
Q3 = np.percentile(rats_present_group, 75)
# Calculate IQR
IQR = Q3 - Q1
# Calculate the 1.5 * IQR factor
iqr_factor = 1.5 * IQR
# Calculate lower and upper bounds
lower_bound = max(0, Q1 - iqr_factor)
upper_bound = Q3 + iqr_factor
print("IQR: ", IQR, iqr_factor, lower_bound, upper_bound)

filtered = rats_present_group[rats_present_group <= upper_bound]
#TODO histogram for present only
max_val_present = rats_present_group.max()
min_val_present = rats_present_group.min()
the_range_present = max_val_present - min_val_present
bin_width = 5
bin_count_present= int(the_range_present/bin_width)

plt.hist(rats_present_group, bins=bin_count_present, alpha=0.6, label='Rats Present', color='red', edgecolor='black')
#plt.hist(rats_absent_group, bins=bin_count, alpha=0.6, label='Rats Absent', color='green', edgecolor='black')

plt.title('Bat Hesitation Time Based on Rat Presence')
plt.xlabel('Time from Landing to Food (seconds)')
plt.ylabel('Frequency')
plt.show()

'''
Hypothesis 2: Do bats behave different whether rats are present?<br />
Variables:<br />
test:<br />
     whether rats are present on platform when bats start eating<br />
Compare:<br />
    bat_landing_to_food (how much they hesitate after landing)
    <br />
Hypotheses:<br />
    H0: The mean hesitation time is the same whether rats are present or not when the bat approaches the food.<br />
    H1: The mean hesitation time is different whether rats are present or not when the bat approaches the food. <br />
'''
df['bat_landing_to_food'] = pd.to_numeric(df['bat_landing_to_food'], errors='coerce')
df['start_time'] = pd.to_datetime(df['start_time'], errors='coerce')

df['feeding_time'] = df['start_time'] + pd.to_timedelta(df['bat_landing_to_food'], unit='s')
df['rat_absent_at_feeding'] = (
    (df['feeding_time'] < df['rat_period_start']) |
    (df['feeding_time'] > df['rat_period_end'])
)
df['rat_present_at_feeding'] = ~df['rat_absent_at_feeding']


present = df[df['rat_present_at_feeding']]['bat_landing_to_food']
absent  = df[df['rat_absent_at_feeding']]['bat_landing_to_food']

t_stat, p_value = ttest_ind(present.dropna(), absent.dropna())

print(f"T-statistic: {t_stat}, P-value: {p_value}")

if p_value < 0.05:
    print("Bats wait longer to feed when rats are not present bec they delay feeding until after rats leave")
else:
    print("Fail to reject the null hypothesis. No significant difference in bat approaching food time when rats are present or absent.")

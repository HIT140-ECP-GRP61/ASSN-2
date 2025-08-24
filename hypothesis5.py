import pandas as pd
from scipy.stats import ttest_ind

df = pd.read_csv('dataset2.csv')

#TODO:clean data
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

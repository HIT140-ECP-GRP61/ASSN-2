import pandas as pd
from scipy.stats import ttest_ind

df = pd.read_csv('dataset1.csv')

#TODO:clean data
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
import pandas as pd
from scipy.stats import ttest_ind

df = pd.read_csv('dataset1.csv')

#TODO:clean data
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
import pandas as pd
from scipy.stats import ttest_ind

df = pd.read_csv('dataset1.csv')

#TODO:clean data
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
import pandas as pd
from scipy.stats import ttest_ind

df = pd.read_csv('dataset1.csv')

#TODO:clean data
'''
Hypothesis 4: Does foraging success (reward = 1) differ based on rat presence at feeding time, separately for risky and avoidant bats?<br />
Variables:<br />
divide risky/avoidant bats and test each group reward rate
test:<br />
     whether rats are present on platform when bats start eating<br />
Compare:<br />
    reward rate
    <br />
Hypotheses:<br />
    H0: Rats being around doesn't affect reward rates for risky/avoidant bats.<br />
    H1: Rats being around affect reward rates for risky/avoidant bats. <br />
    
'''
df['bat_landing_to_food'] = pd.to_numeric(df['bat_landing_to_food'], errors='coerce')
df['start_time'] = pd.to_datetime(df['start_time'], errors='coerce')

df['feeding_time'] = df['start_time'] + pd.to_timedelta(df['bat_landing_to_food'], unit='s')
df['rat_absent_at_feeding'] = (
    (df['feeding_time'] < df['rat_period_start']) |
    (df['feeding_time'] > df['rat_period_end'])
)
df['rat_present_at_feeding'] = ~df['rat_absent_at_feeding']

df['is_risky'] = df['risk'] == 1
df['is_avoidant'] = df['risk'] == 0

grouped = df.groupby(['is_risky', 'rat_present_at_feeding'])['reward'].agg(['mean', 'count'])



risky_present = df[(df['is_risky']) & (df['rat_present_at_feeding'])]['reward']
risky_absent  = df[(df['is_risky']) & (~df['rat_present_at_feeding'])]['reward']
t_risky, p_risky = ttest_ind(risky_present, risky_absent, equal_var=False)

avoidant_present = df[(df['is_avoidant']) & (df['rat_present_at_feeding'])]['reward']
avoidant_absent  = df[(df['is_avoidant']) & (~df['rat_present_at_feeding'])]['reward']
t_avoidant, p_avoidant = ttest_ind(avoidant_present, avoidant_absent, equal_var=False)

print("Risky bats: Rat present vs absent")
print(f"  t-statistic = {t_risky:.3f}")
print(f"  p-value     = {p_risky:.6f}\n")
if p_risky < 0.05:
    print("There is significant impact of whether rats being around affecting reward rates for risky bats")
else:
    print("Fail to reject the null hypothesis. There is no significant impact of whether rats being around affecting reward rates for risky bats")

print("Avoidant bats: Rat present vs absent")
print(f"  t-statistic = {t_avoidant:.3f}")
print(f"  p-value     = {p_avoidant:.6f}")

if p_avoidant < 0.05:
    print("There is significant impact of whether rats being around affecting reward rates for avoidant bats")
else:
    print("Fail to reject the null hypothesis. There is no significant impact of whether rats being around affecting reward rates for avoidant bats")

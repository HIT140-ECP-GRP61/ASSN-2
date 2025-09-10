import pandas as pd
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

df = pd.read_csv('cleaned_dataset1.csv')

avoidant_bat = df[df['risk'] == 0]
risky_bat = df[df['risk'] == 1]

reward_risky = risky_bat['reward']
reward_avoidant = avoidant_bat['reward']

mean_risky = reward_risky.mean()
median_risky = reward_risky.median()
standard_deviation_risky = reward_risky.std(ddof=1)

mean_avoidant = reward_avoidant.mean()
median_avoidant = reward_avoidant.median()
standard_deviation_avoidant = reward_avoidant.std(ddof=1)

percent_rewarded_risky = (reward_risky / len(risky_bat)) * 100
percent_rewarded_avoidant = (reward_avoidant / len(avoidant_bat)) * 100
print("Risky bats rewarded: ", reward_risky.value_counts(), "\nTotal length: ", len(risky_bat), "\nAvoidant bats rewarded: ", reward_avoidant.value_counts(), "\nTotal length: ", len(avoidant_bat))

# Plot
labels = ['Risky Bats', 'Avoidant Bats']
counts = [reward_risky.sum(), reward_avoidant.sum()]
colors = ['red', 'green']

plt.bar(labels, counts, color=colors, edgecolor='black')
plt.title('Number of Rewarded Bats (Red=Risky Green=Avoidance)')
plt.ylabel('Frequency')
plt.show()

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

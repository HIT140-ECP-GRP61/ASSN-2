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

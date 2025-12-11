import pandas as panda
import matplotlib.pyplot as plot
import seaborn as sns
import statsmodels.api as statmodel

df = panda.read_csv('dataset_6.csv')
df["GenderLabel"] = df["Gender"].map({0:"Male", 1:"Female"})
def question_two():
    #Answer to Question 2A

    #Calculating the mean for the dataset
    mean_stress = df['StressScore'].mean()
    mean_screen_time = df['WeeklyScreentimeHours'].mean()
    mean_sleep_quality = df['SleepQualityScore'].mean()

    #Calculating the standard deviation for the dataset
    sd_stress = df['StressScore'].std()
    sd_screen_time = df['WeeklyScreentimeHours'].std()
    sd_sleep_quality = df['SleepQualityScore'].std()

    print("Question 1A Results:\n")
    print(f"Mean Stress Score: {mean_stress:.4f}, SD: {sd_stress:.4f}")
    print(f"Mean Weekly Screentime Hours: {mean_screen_time:.4f}, SD: {sd_screen_time:.4f}")
    print(f"Mean Sleep Quality Score: {mean_sleep_quality:.4f}, SD: {sd_sleep_quality:.4f}")

    gender_comparison = df.groupby('GenderLabel')['StressScore'].mean()

    print("\nQuestion 1B Results:\n")
    print(gender_comparison)

def question_three():
    #Answer of Question 3A
    plot.figure(figsize=(8, 5))
    sns.boxplot(x='StressScore', data=df, palette='pastel',color='pink')
    plot.title("Boxplot of Stress Score")
    plot.xlabel("Stress Score")
    plot.savefig('./plots/boxplot_stress_score.png',dpi=300, bbox_inches='tight')
    plot.show()

    #Answer of Question 3B
    plot.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x='WeeklyScreentimeHours', y='StressScore', hue='GenderLabel')
    plot.title('Stress Score vs. Weekly Screen Time')
    plot.xlabel('Weekly Screen Time (Hours)')
    plot.ylabel('Stress Score')
    plot.savefig('./plots/scatterplot_stress_vs_screen_time.png', dpi=300, bbox_inches='tight')
    plot.show()

def question_four():
    #Answer to Question 4A
    X = statmodel.add_constant(df['WeeklyScreentimeHours'])
    Y = df['StressScore']

    model_screen = statmodel.OLS(Y, X).fit()
    print("--- Regression: Stress vs. Screen Time ---")
    print(model_screen.summary())

    x_sleep = statmodel.add_constant(df['SleepQualityScore'])
    model_sleep = statmodel.OLS(Y, x_sleep).fit()
    print("\n--- Regression: Stress vs. Sleep Quality ---")
    print(model_sleep.summary())


question_four()

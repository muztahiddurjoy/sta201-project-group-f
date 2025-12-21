import pandas as panda
import matplotlib.pyplot as plot
import seaborn as sns
import numpy as np
import statsmodels.api as statmodel
import csv

df = panda.read_csv('dataset_6.csv')



def print_sd_table(series, col_name):
        """
        Creates and prints a table showing x, x-mean, and (x-mean)^2
        to demonstrate how SD is calculated.
        """

        mean_val = series.mean()
        
        # Create a temporary DataFrame for the calculation
        calc_df = panda.DataFrame()
        calc_df['x'] = series
        calc_df['x - mean'] = series - mean_val
        calc_df['(x - mean)^2'] = (series - mean_val) ** 2
        
        # Calculate the Sum of Squares
        sum_squares = calc_df['(x - mean)^2'].sum()
        variance = sum_squares / (len(series) - 1)
        sd = np.sqrt(variance)

        print(f"\n--- Calculation Table for '{col_name}' ---")
        with open(f"{col_name}_sd.csv", 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)            
            writer.writerow([f'x ({col_name})', 'x - mean', '(x - mean)^2'])     
            writer.writerows(calc_df.values)

df["GenderLabel"] = df["Gender"].map({0:"Male", 1:"Female"})
def question_two():
    #Answer to Question 2A
    print("Printing the table")
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
    #onek boro contribution

    print_sd_table(df['StressScore'], "StressScore")
    print_sd_table(df['WeeklyScreentimeHours'], "WeeklyScreentimeHours")
    print_sd_table(df['SleepQualityScore'], "SleepQualityScore")

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

def question_four(df):
    """
    Performs Simple and Multiple Linear Regression analysis for Stress Score.
    Generates summaries and regression plots.
    """
    
    # --- PART A: Simple Linear Regression (Screen Time -> Stress) ---
    X_screen = statmodel.add_constant(df['WeeklyScreentimeHours'])
    Y = df['StressScore']
    
    model_screen = statmodel.OLS(Y, X_screen).fit()
    print("\n" + "="*40)
    print("1. Simple Regression: Stress vs. Screen Time")
    print("="*40)
    print(model_screen.summary())

    # Visualization for Screen Time
    plot.figure(figsize=(10, 4))
    sns.regplot(x='WeeklyScreentimeHours', y='StressScore', data=df, line_kws={'color':'red'})
    plot.title('Impact of Weekly Screen Time on Stress Score')
    plot.show()

    # --- PART B: Simple Linear Regression (Sleep Quality -> Stress) ---
    X_sleep = statmodel.add_constant(df['SleepQualityScore'])
    
    model_sleep = statmodel.OLS(Y, X_sleep).fit()
    print("\n" + "="*40)
    print("2. Simple Regression: Stress vs. Sleep Quality")
    print("="*40)
    print(model_sleep.summary())

    # Visualization for Sleep Quality
    plot.figure(figsize=(10, 4))
    sns.regplot(x='SleepQualityScore', y='StressScore', data=df, line_kws={'color':'green'})
    plot.title('Impact of Sleep Quality on Stress Score')
    plot.show()

    # --- PART C: Multiple Linear Regression (Both -> Stress) ---
    # This is likely the core requirement for "Question 4" if Q1-3 were descriptive.
    # It checks the combined effect of both variables.
    X_mult = df[['WeeklyScreentimeHours', 'SleepQualityScore']]
    X_mult = statmodel.add_constant(X_mult)
    
    model_mult = statmodel.OLS(Y, X_mult).fit()
    print("\n" + "="*40)
    print("3. Multiple Regression: Stress vs. (Screen Time + Sleep Quality)")
    print("="*40)
    print(model_mult.summary())

# Usage Example:
# question_four(df)


def question_five_split_gender(df):
    print("========================================")
    print("5. Regression by Gender (Males vs Females)")
    print("========================================")

    # 1. Split the Data
    # (Make sure your column name is 'Gender' and values are 'Male'/'Female')
    male_df = df[df['Gender'] == 0]
    female_df = df[df['Gender'] == 1]

    # --- MODEL A: MALES ---
    X_male = statmodel.add_constant(male_df['WeeklyScreentimeHours'])
    Y_male = male_df['StressScore']
    
    model_male = statmodel.OLS(Y_male, X_male).fit()
    print("\n--- MALE Regression Results ---")
    print(model_male.summary())

    # --- MODEL B: FEMALES ---
    X_female = statmodel.add_constant(female_df['WeeklyScreentimeHours'])
    Y_female = female_df['StressScore']
    
    model_female = statmodel.OLS(Y_female, X_female).fit()
    print("\n--- FEMALE Regression Results ---")
    print(model_female.summary())

    # --- VISUALIZATION: Compare the Lines ---
    plot.figure(figsize=(10, 6))
    
    # Plot Males (Blue)
    sns.regplot(x='WeeklyScreentimeHours', y='StressScore', data=male_df, 
                color='blue', label='Male', ci=None)
    
    # Plot Females (Red)
    sns.regplot(x='WeeklyScreentimeHours', y='StressScore', data=female_df, 
                color='red', label='Female', ci=None)

    plot.title('Stress vs. Screen Time (By Gender)')
    plot.legend()
    plot.grid(True, alpha=0.3)
    plot.show()

# Usage
question_five_split_gender(df)


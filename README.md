# STA201 Project - Group F - Fall 2025

## 📋 Project Overview

This project analyzes how **screen time and sleep quality affect student stress levels**. We collected data from students and used statistical analysis and visualizations to understand these relationships.
<!-- 
### Research Questions
1. **What are the typical stress levels, screen time, and sleep quality among students?**
2. **Do male and female students experience different stress levels?**
3. **What patterns can we see visually between stress and screen time?**
4. **How much does screen time and sleep quality predict stress levels?**

--- -->

## 📁 Project Files

### Main Files
- **`calculations.py`** - The main Python script that does all the analysis and creates charts
- **`dataset_6.csv`** - The raw data containing information about students
- **`plots/`** - Folder where all generated charts are saved

### Data File Details (`dataset_6.csv`)

The dataset contains **52 students** with the following information:

| Column Name | What It Means | Example Values |
|---|---|---|
| **ID** | Unique student identifier | 1, 2, 3... |
| **Gender** | 0 = Male, 1 = Female | 0 or 1 |
| **WeeklyScreentimeHours** | Hours spent on screens per week | 8.7, 10.8, 13.8 |
| **CoCurricularHours** | Hours spent in activities per week | 2.9, 5, 6 |
| **SleepQualityScore** | Quality of sleep (1-5 scale, higher is better) | 1, 2, 3, 4, 5 |
| **StressScore** | Stress level (higher = more stressed) | 16, 27, 37 |

---

## 🔍 What Each Analysis Does

### Question 1: Basic Statistics
**What we calculated:**
- **Mean (Average)** - The typical value for each measurement
- **Standard Deviation (SD)** - How spread out the values are (higher = more variation)

**Results Show:**
- Average stress score across all students
- Average weekly screen time
- Average sleep quality
- Comparison of stress levels between males and females

### Question 2: Visual Patterns
**Charts Created:**
1. **Boxplot of Stress Scores** - Shows how stress is distributed, highlights extreme cases
2. **Scatterplot** - Shows the relationship between screen time and stress, colored by gender

**What to look for:**
- Do students with more screen time have higher stress?
- Do males and females show different patterns?

### Question 3: Prediction Model (Regression)
**What it does:** Creates mathematical models to predict stress levels based on:
- Screen time alone
- Sleep quality alone

**Simple explanation:**
- If we know someone's screen time, can we predict their stress level?
- If we know their sleep quality, can we predict their stress level?
- The results show how strong these predictions are

---

## 💻 How to Use This Project

### Requirements
You need to have Python installed with these libraries:
- `pandas` - For working with data tables
- `matplotlib` - For creating charts
- `seaborn` - For making prettier charts
- `statsmodels` - For statistical analysis

### Installation
```bash
# Install required packages
pip install pandas matplotlib seaborn statsmodels
```

### Running the Analysis
```bash
# Navigate to the project folder
cd sta201-project-group-f

# Run the analysis
python3 calculations.py
```

### What Happens When You Run It
1. The script reads the student data
2. It calculates statistics (averages, standard deviations)
3. It creates two charts and saves them to the `plots/` folder
4. It performs regression analysis and prints detailed results
5. All output is printed to your screen

---

## 📊 Understanding the Results

### When You Run the Script, You'll See:

**Question 1A Results:**
```
Mean Stress Score: 25.5, SD: 8.3
Mean Weekly Screentime Hours: 11.2, SD: 2.1
Mean Sleep Quality Score: 2.8, SD: 1.4
```
*Translation:* The average student has a stress score of 25.5, spends 11.2 hours on screens weekly, and rates their sleep quality as 2.8 out of 5.

**Question 1B Results:**
```
GenderLabel
Male      23.4
Female    27.1
```
*Translation:* Female students report slightly higher stress (27.1) compared to male students (23.4).

### Charts Generated

**📈 boxplot_stress_score.png**
- Shows the spread of stress scores
- The box shows where most students fall
- Points outside show unusually high or low stress

**📊 scatterplot_stress_vs_screen_time.png**
- Each dot represents one student
- Horizontal position = screen time
- Vertical position = stress level
- Color = gender (blue/orange)
- Pattern = shows if more screen time relates to more stress

### Regression Results
The output includes:
- **R-squared value** (0-1): How well the prediction works (1 = perfect prediction, 0 = no prediction)
- **Coefficient**: The strength of the relationship
- **P-value**: Whether the relationship is statistically significant (p < 0.05 means significant)

---

## 🎯 Key Insights to Look For

1. **Screen Time & Stress**: Does the scatterplot show more stressed students have more screen time?
2. **Sleep Quality & Stress**: Do students with poor sleep quality have higher stress?
3. **Gender Differences**: Do males and females show different stress patterns?
4. **Statistical Significance**: Are the relationships strong enough to be meaningful?

---

## 📝 Notes for Group Members

- All code is written in Python, a beginner-friendly programming language
- Comments in the code (starting with #) explain what each section does
- The `plots/` folder must exist before running the script (should already be created)
- Data is read from a CSV file, which is like a spreadsheet

---

## 🚀 Future Improvements

Potential analyses to add:
- Multi-variable regression (combining multiple factors)
- Correlation matrix to see all relationships at once
- Statistical tests comparing male vs female stress
- Analysis by co-curricular activity hours

---

## 👥 Group F Members


---

## 📞 Questions?

If the code doesn't work or you need clarification on any results, refer to the inline comments in `calculations.py` or reach out to the group.

---

**Last Updated:** December 2025

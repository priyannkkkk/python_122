# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# For better visualizations
sns.set(style='whitegrid')

# ---------------------------------------------
# Step 1: Data Loading and Cleaning
# ---------------------------------------------

# Load the dataset (replace with your file path)
file_path = r"C:\Users\priya\Downloads\MovieFranchises.csv"
try:
    movies_df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"File not found at {file_path}. Please check the path and try again.")
    exit()

# Display the first few rows of the dataset
print(movies_df.head())

# Checking for missing values
print("\nMissing values per column:")
print(movies_df.isnull().sum())

# Convert relevant columns to numeric first
movies_df['Budget'] = pd.to_numeric(movies_df['Budget'], errors='coerce')
movies_df['Lifetime Gross'] = pd.to_numeric(movies_df['Lifetime Gross'], errors='coerce')

# Fill missing values for Budget and Lifetime Gross with median values
movies_df['Budget'] = movies_df['Budget'].fillna(movies_df['Budget'].median())
movies_df['Lifetime Gross'] = movies_df['Lifetime Gross'].fillna(movies_df['Lifetime Gross'].median())

# Removing duplicates if any
movies_df.drop_duplicates(inplace=True)

# Handling outliers - Remove entries where Budget or Lifetime Gross are in the top 1%
movies_df = movies_df[(movies_df['Budget'] < movies_df['Budget'].quantile(0.99)) & 
                      (movies_df['Lifetime Gross'] < movies_df['Lifetime Gross'].quantile(0.99))]

# Normalize Lifetime Gross data (optional step for better visualizations)
movies_df['Lifetime Gross'] = np.log1p(movies_df['Lifetime Gross'])

# Show basic stats of cleaned dataset
print("\nCleaned dataset statistics:")
print(movies_df.describe())

# ---------------------------------------------
# Step 2: Descriptive Statistics
# ---------------------------------------------

# Descriptive statistics for VoteAvg and Lifetime Gross collections
mean_rating = movies_df['VoteAvg'].mean()
median_rating = movies_df['VoteAvg'].median()
std_rating = movies_df['VoteAvg'].std()

mean_box_office = movies_df['Lifetime Gross'].mean()
median_box_office = movies_df['Lifetime Gross'].median()
std_box_office = movies_df['Lifetime Gross'].std()

print(f"\nMean Rating: {mean_rating:.2f}, Median Rating: {median_rating:.2f}, Rating Std Dev: {std_rating:.2f}")
print(f"Mean Box Office: {mean_box_office:.2f}, Median Box Office: {median_box_office:.2f}, Box Office Std Dev: {std_box_office:.2f}")

# ---------------------------------------------
# Step 3: Data Visualization
# ---------------------------------------------

# Bar graph - Franchise distribution
plt.figure(figsize=(12, 6))
sns.countplot(x='FranchiseID', data=movies_df, order=movies_df['FranchiseID'].value_counts().index)
plt.title("Movie Franchise Distribution")
plt.xticks(rotation=45)
plt.show()

# Histogram - Ratings
plt.figure(figsize=(12, 6))
sns.histplot(movies_df['VoteAvg'], bins=20, kde=True)
plt.title("Movie Ratings Distribution")
plt.xlabel("Vote Average")
plt.ylabel("Frequency")
plt.show()

# Box plot - Budgets by FranchiseID
plt.figure(figsize=(12, 6))
sns.boxplot(x='FranchiseID', y='Budget', data=movies_df)
plt.title("Movie Budget Distribution by Franchise")
plt.xticks(rotation=45)
plt.show()

# Scatter plot - Ratings vs Lifetime Gross
plt.figure(figsize=(12, 6))
sns.scatterplot(x='VoteAvg', y='Lifetime Gross', data=movies_df)
plt.title("Movie Ratings vs Lifetime Gross Collections")
plt.xlabel("Vote Average")
plt.ylabel("Lifetime Gross (Log Scale)")
plt.yscale('log')
plt.show()

# ---------------------------------------------
# Step 4: Inferential Statistics - Hypothesis Testing
# ---------------------------------------------

# Split dataset into high and low budget movies
median_budget = movies_df['Budget'].median()
high_budget_movies = movies_df[movies_df['Budget'] > median_budget]['VoteAvg']
low_budget_movies = movies_df[movies_df['Budget'] <= median_budget]['VoteAvg']

# Perform t-test
t_stat, p_value = ttest_ind(high_budget_movies, low_budget_movies, nan_policy='omit')

print(f"\nT-statistic: {t_stat:.2f}, P-value: {p_value:.4f}")
if p_value < 0.05:
    print("Reject the null hypothesis - There is a significant difference between high and low budget movies' ratings.")
else:
    print("Fail to reject the null hypothesis - No significant difference between high and low budget movies' ratings.")

# ---------------------------------------------
# Step 5: Predictive Modeling Using Linear Regression
# ---------------------------------------------

# Features (independent variables)
X = movies_df[['Budget', 'VoteAvg']]

# Target (dependent variable)
y = movies_df['Lifetime Gross']

# Check for missing values in X and y
print("Missing values in X:\n", X.isnull().sum())
print("Missing values in y:\n", y.isnull().sum())

# Optionally, drop rows with missing values
X = X.loc[~X.isnull().any(axis=1)]
y = y[X.index]  # Align y with the dropped rows in X

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initialize and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate model performance (R-squared score)
r_squared = model.score(X_test, y_test)
print(f"\nR-squared score for the model: {r_squared:.4f}")

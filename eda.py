import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "sample_dataset.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

sns.set_theme(style="whitegrid")

# 1. Load dataset
df = pd.read_csv(DATA_FILE)

print("\n========== FIRST 5 ROWS ==========")
print(df.head())

print("\n========== DATASET SHAPE ==========")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

print("\n========== DATA TYPES ==========")
print(df.dtypes)

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Basic cleaning
df.columns = df.columns.str.strip()
df = df.drop_duplicates()

numeric_cols = df.select_dtypes(include="number").columns
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Save cleaned data
cleaned_path = os.path.join(OUTPUT_DIR, "cleaned_dataset.csv")
df.to_csv(cleaned_path, index=False)

# 2. Descriptive statistics
print("\n========== DESCRIPTIVE STATISTICS ==========")
print(df.describe())

# 3. Category distribution
category_counts = df["Category"].value_counts()
plt.figure(figsize=(8, 5))
category_counts.plot(kind="bar")
plt.title("Number of Products by Category")
plt.xlabel("Category")
plt.ylabel("Number of Products")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "01_category_distribution.png"), dpi=200)
plt.close()

# 4. Sales by category
sales_by_category = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
sales_by_category.plot(kind="bar")
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "02_sales_by_category.png"), dpi=200)
plt.close()

# 5. Price distribution
plt.figure(figsize=(8, 5))
plt.hist(df["Price"], bins=8)
plt.title("Product Price Distribution")
plt.xlabel("Price")
plt.ylabel("Number of Products")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "03_price_distribution.png"), dpi=200)
plt.close()

# 6. Rating vs sales
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Rating", y="Sales", hue="Category", s=90)
plt.title("Rating vs Sales")
plt.xlabel("Rating")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "04_rating_vs_sales.png"), dpi=200)
plt.close()

# 7. Sales by product
top_sales = df.sort_values("Sales", ascending=False).head(10)
plt.figure(figsize=(9, 6))
sns.barplot(data=top_sales, x="Sales", y="Product")
plt.title("Top 10 Products by Sales")
plt.xlabel("Sales")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "05_top_10_products.png"), dpi=200)
plt.close()

# 8. Correlation heatmap
corr = df.select_dtypes(include="number").corr()
plt.figure(figsize=(7, 5))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Numerical Feature Correlation")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "06_correlation_heatmap.png"), dpi=200)
plt.close()

# 9. Automatically print useful findings
best_category = sales_by_category.idxmax()
best_product = df.loc[df["Sales"].idxmax(), "Product"]
avg_rating = df["Rating"].mean()
avg_price = df["Price"].mean()

print("\n========== KEY FINDINGS ==========")
print(f"Highest-selling category: {best_category}")
print(f"Highest-selling individual product: {best_product}")
print(f"Average product rating: {avg_rating:.2f}")
print(f"Average product price: ₹{avg_price:,.2f}")
print("\nEDA completed successfully.")
print(f"Charts saved in: {OUTPUT_DIR}")

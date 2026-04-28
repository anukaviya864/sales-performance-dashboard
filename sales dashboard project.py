import kagglehub
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Fix save location
os.chdir(r"c:\Users\91897\OneDrive\Documents\Python Scripts")

# Load data
path = kagglehub.dataset_download("rohitsahoo/sales-forecasting")
df = pd.read_csv(os.path.join(path, "train.csv"), encoding='latin1')
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)

# Chart 1 - Sales by Category
plt.figure(figsize=(8,5))
cat_sales = df.groupby('Category')['Sales'].sum().sort_values()
cat_sales.plot(kind='barh', color='steelblue')
plt.title('Sales by Category')
plt.xlabel('Total Sales')
plt.tight_layout()
plt.savefig('sales_by_category.png')
plt.show()
print("Chart 1 done!")

# Chart 2 - Monthly Sales Trend
plt.figure(figsize=(10,5))
df['Month'] = df['Order Date'].dt.to_period('M')
monthly = df.groupby('Month')['Sales'].sum()
monthly.plot(kind='line', marker='o', color='teal')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.savefig('monthly_sales.png')
plt.show()
print("Chart 2 done!")

# Chart 3 - Sales by Region
plt.figure(figsize=(8,5))
region = df.groupby('Region')['Sales'].sum().sort_values()
region.plot(kind='bar', color='coral')
plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.savefig('sales_by_region.png')
plt.show()
print("Chart 3 done!")

# Chart 4 - Top 10 Sub-Categories
plt.figure(figsize=(8,5))
top_sub = df.groupby('Sub-Category')['Sales'].sum().nlargest(10).sort_values()
top_sub.plot(kind='barh', color='purple')
plt.title('Top 10 Sub-Categories by Sales')
plt.xlabel('Total Sales')
plt.tight_layout()
plt.savefig('top_subcategories.png')
plt.show()
print("Chart 4 done!")

print("\nAll charts saved! Ready for Tableau.")
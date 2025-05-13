import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages

# Load the dataset
df = pd.read_csv("train1.csv")

# Convert 'Order Date' to datetime (adjusting for day-first format)
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)

# Set visual style
sns.set(style="whitegrid")

# Create PDF file
pdf = PdfPages("Superstore_Report.pdf")

# --- Chart 1: Monthly Sales Trend ---
monthly_sales = df.resample('M', on='Order Date')['Sales'].sum().reset_index()
plt.figure(figsize=(10, 5))
sns.lineplot(data=monthly_sales, x='Order Date', y='Sales', marker='o', color='steelblue')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.xticks(rotation=45)
plt.tight_layout()
pdf.savefig()
plt.close()

# --- Chart 2: Sales by Category ---
category_sales = df.groupby('Category')['Sales'].sum().sort_values()
plt.figure(figsize=(8, 5))
category_sales.plot(kind='barh', color='mediumseagreen')
plt.title('Sales by Category')
plt.xlabel('Sales ($)')
plt.tight_layout()
pdf.savefig()
plt.close()

# --- Chart 3: Sales by Sub-Category ---
subcategory_sales = df.groupby('Sub-Category')['Sales'].sum().sort_values()
plt.figure(figsize=(10, 6))
subcategory_sales.plot(kind='barh', color='skyblue')
plt.title('Sales by Sub-Category')
plt.xlabel('Sales ($)')
plt.tight_layout()
pdf.savefig()
plt.close()

# --- Chart 4: Sales by Region ---
region_sales = df.groupby('Region')['Sales'].sum().sort_values()
plt.figure(figsize=(8, 5))
region_sales.plot(kind='bar', color='orange')
plt.title('Sales by Region')
plt.ylabel('Sales ($)')
plt.xticks(rotation=0)
plt.tight_layout()
pdf.savefig()
plt.close()

# --- Chart 5: Sales by Segment ---
segment_sales = df.groupby('Segment')['Sales'].sum()
plt.figure(figsize=(6, 5))
segment_sales.plot(kind='bar', color='coral')
plt.title('Sales by Segment')
plt.ylabel('Sales ($)')
plt.xticks(rotation=0)
plt.tight_layout()
pdf.savefig()
plt.close()

# Close the PDF
pdf.close()

print("✅ Report saved as 'Superstore_Report.pdf'")

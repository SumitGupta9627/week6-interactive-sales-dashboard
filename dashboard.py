"""
Week 6 - Interactive Sales Dashboard
Seaborn + Matplotlib + Plotly
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

DATA_FILE = "sales_data.csv"
OUT_DIR = "visualizations"
CONFIG = {'date_col': 'Date', 'product_col': 'Product', 'category_col': 'Product', 'region_col': 'Region', 'sales_col': 'Total_Sales', 'quantity_col': 'Quantity', 'price_col': 'Price'}

os.makedirs(OUT_DIR, exist_ok=True)
sns.set_theme(style="whitegrid", context="notebook")

df = pd.read_csv(DATA_FILE)

# Convert date when available
if CONFIG["date_col"] and CONFIG["date_col"] in df.columns:
    df[CONFIG["date_col"]] = pd.to_datetime(df[CONFIG["date_col"]], errors="coerce")

sales = CONFIG["sales_col"]
product = CONFIG["product_col"]
category = CONFIG["category_col"]
region = CONFIG["region_col"]
quantity = CONFIG["quantity_col"]
price = CONFIG["price_col"]

print("Dataset loaded successfully")
print(f"Rows: {len(df)} | Columns: {len(df.columns)}")
print("\nColumns:", list(df.columns))

# 1. Box plot
if category and price and category in df.columns and price in df.columns:
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x=category, y=price)
    plt.title("Price Distribution by Category")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "boxplot.png"), dpi=150)
    plt.close()

# 2. Violin plot
if category and price and category in df.columns and price in df.columns:
    plt.figure(figsize=(10, 6))
    sns.violinplot(data=df, x=category, y=price)
    plt.title("Price Distribution - Violin Plot")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "violinplot.png"), dpi=150)
    plt.close()

# 3. Correlation heatmap
num = df.select_dtypes(include=np.number)
if not num.empty:
    plt.figure(figsize=(10, 7))
    sns.heatmap(num.corr(), annot=True, fmt=".2f", cmap="Blues", linewidths=.5)
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "correlation_heatmap.png"), dpi=150)
    plt.close()

# 4. Sales trend
if sales and sales in df.columns:
    if CONFIG["date_col"] and CONFIG["date_col"] in df.columns:
        trend = df.dropna(subset=[CONFIG["date_col"]]).groupby(CONFIG["date_col"], as_index=False)[sales].sum()
        fig = px.line(trend, x=CONFIG["date_col"], y=sales,
                      title="Interactive Sales Trend", markers=True,
                      hover_data=[sales])
    else:
        trend = df.groupby(df.index)[sales].sum().reset_index()
        fig = px.line(trend, x="index", y=sales, title="Interactive Sales Trend",
                      markers=True, hover_data=[sales])
    fig.write_html(os.path.join(OUT_DIR, "sales_trend_interactive.html"))

# 5. Product performance
if product and sales and product in df.columns and sales in df.columns:
    prod = df.groupby(product, as_index=False)[sales].sum().sort_values(sales, ascending=False)
    fig = px.bar(prod, x=product, y=sales, title="Product Performance",
                 color=sales, hover_data=[sales])
    fig.write_html(os.path.join(OUT_DIR, "product_performance_interactive.html"))

# 6. Region/category interactive chart
group_col = region if region in df.columns else category
if group_col and sales and group_col in df.columns and sales in df.columns:
    grp = df.groupby(group_col, as_index=False)[sales].sum()
    fig = px.pie(grp, names=group_col, values=sales,
                 title=f"Sales Distribution by {group_col}",
                 hole=0.35)
    fig.write_html(os.path.join(OUT_DIR, "sales_distribution_interactive.html"))

# Static 2x2 dashboard
fig, axes = plt.subplots(2, 2, figsize=(16, 11))
fig.suptitle("Week 6 Sales Visualization Dashboard", fontsize=20, fontweight="bold")

if category and price and category in df.columns and price in df.columns:
    sns.boxplot(data=df, x=category, y=price, ax=axes[0,0])
    axes[0,0].set_title("Price Distribution")
    axes[0,0].tick_params(axis="x", rotation=25)
else:
    axes[0,0].text(.5,.5,"Box plot unavailable",ha="center")

if category and price and category in df.columns and price in df.columns:
    sns.violinplot(data=df, x=category, y=price, ax=axes[0,1])
    axes[0,1].set_title("Violin Plot")
    axes[0,1].tick_params(axis="x", rotation=25)
else:
    axes[0,1].text(.5,.5,"Violin plot unavailable",ha="center")

if not num.empty:
    sns.heatmap(num.corr(), annot=True, fmt=".2f", cmap="Blues", ax=axes[1,0])
    axes[1,0].set_title("Correlation Heatmap")
else:
    axes[1,0].text(.5,.5,"Heatmap unavailable",ha="center")

if product and sales and product in df.columns and sales in df.columns:
    top = df.groupby(product)[sales].sum().sort_values(ascending=False).head(10)
    axes[1,1].bar(top.index.astype(str), top.values)
    axes[1,1].set_title("Top Products by Sales")
    axes[1,1].tick_params(axis="x", rotation=35)
else:
    axes[1,1].text(.5,.5,"Product chart unavailable",ha="center")

plt.tight_layout(rect=[0,0,1,.96])
plt.savefig(os.path.join(OUT_DIR, "dashboard_overview.png"), dpi=150)
plt.close()

print("\nDashboard generation complete.")
print(f"Check the '{OUT_DIR}' folder for charts and interactive HTML files.")

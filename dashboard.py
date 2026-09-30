import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'sales_data.csv')
OUT_DIR = os.path.join(BASE_DIR, 'visualizations')
os.makedirs(OUT_DIR, exist_ok=True)

sns.set_theme(style='whitegrid', context='notebook')
df = pd.read_csv(DATA_FILE)
df['Date'] = pd.to_datetime(df['Date'])

print('Dataset loaded successfully')
print(f'Rows: {len(df)} | Columns: {len(df.columns)}')
print(f'Columns: {list(df.columns)}')

# 1. Box plot
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Product', y='Total_Sales')
plt.title('Sales Distribution by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, 'boxplot.png'), dpi=160)
plt.close()

# 2. Violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(data=df, x='Product', y='Total_Sales', inner='quartile')
plt.title('Sales Distribution and Density by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, 'violinplot.png'), dpi=160)
plt.close()

# 3. Correlation heatmap
numeric = df.select_dtypes(include=np.number)
plt.figure(figsize=(8, 6))
sns.heatmap(numeric.corr(), annot=True, fmt='.2f', cmap='Blues', square=True)
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, 'correlation_heatmap.png'), dpi=160)
plt.close()

# 4. Interactive sales trend
trend = df.sort_values('Date')
fig = px.line(trend, x='Date', y='Total_Sales', color='Product', markers=True,
              title='Interactive Sales Trend', hover_data=['Quantity', 'Price', 'Region'])
fig.update_layout(template='plotly_white', hovermode='x unified')
fig.write_html(os.path.join(OUT_DIR, 'sales_trend_interactive.html'))

# 5. Interactive product performance with dropdown
product_summary = df.groupby('Product', as_index=False).agg(
    Total_Sales=('Total_Sales', 'sum'), Quantity=('Quantity', 'sum'),
    Average_Price=('Price', 'mean')
)
fig = px.bar(product_summary, x='Product', y='Total_Sales', color='Product',
             title='Product Performance', hover_data=['Quantity', 'Average_Price'])
fig.update_layout(template='plotly_white', showlegend=False)
fig.write_html(os.path.join(OUT_DIR, 'product_performance_interactive.html'))

# 6. Interactive sales distribution
fig = px.histogram(df, x='Total_Sales', color='Product', nbins=15,
                   title='Interactive Sales Distribution', hover_data=['Customer_ID', 'Region'])
fig.update_layout(template='plotly_white', bargap=0.08)
fig.write_html(os.path.join(OUT_DIR, 'sales_distribution_interactive.html'))

# 7. Customer segmentation: RFM-like value grouping from available fields
customer = df.groupby('Customer_ID', as_index=False).agg(
    Total_Sales=('Total_Sales', 'sum'),
    Quantity=('Quantity', 'sum'),
    Orders=('Customer_ID', 'count')
)
q1, q2 = customer['Total_Sales'].quantile([0.33, 0.66]).tolist()
customer['Segment'] = np.select(
    [customer['Total_Sales'] <= q1, customer['Total_Sales'] <= q2],
    ['Low Value', 'Regular'],
    default='High Value'
)
fig = px.scatter(customer, x='Quantity', y='Total_Sales', size='Orders', color='Segment',
                 hover_name='Customer_ID', hover_data=['Orders'],
                 title='Customer Segmentation by Sales Value and Quantity',
                 labels={'Quantity': 'Total Quantity', 'Total_Sales': 'Total Sales'})
fig.update_layout(template='plotly_white')
fig.write_html(os.path.join(OUT_DIR, 'customer_segmentation_interactive.html'))

# 8. 2x2 dashboard overview
fig, axes = plt.subplots(2, 2, figsize=(16, 10))

sns.lineplot(data=trend, x='Date', y='Total_Sales', ax=axes[0, 0])
axes[0, 0].set_title('Sales Trend')
axes[0, 0].tick_params(axis='x', rotation=30)

sns.barplot(data=product_summary, x='Product', y='Total_Sales', hue='Product', legend=False, ax=axes[0, 1])
axes[0, 1].set_title('Product Performance')

sns.boxplot(data=df, x='Product', y='Total_Sales', ax=axes[1, 0])
axes[1, 0].set_title('Sales Distribution by Product')

sns.heatmap(numeric.corr(), annot=True, fmt='.2f', cmap='Blues', ax=axes[1, 1])
axes[1, 1].set_title('Correlation Heatmap')

plt.suptitle('Interactive Sales Dashboard - Overview', fontsize=18, y=1.01)
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, 'dashboard_overview.png'), dpi=160, bbox_inches='tight')
plt.close()

print('Dashboard generation complete.')
print('Check the visualizations folder for charts and interactive HTML files.')

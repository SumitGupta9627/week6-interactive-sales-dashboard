# Dashboard Guide & Visualization Interpretation

## 1. Project Overview
The Interactive Sales Dashboard analyzes sales trends, product performance, customer purchasing activity, and relationships between numerical variables. It combines Seaborn/Matplotlib statistical charts with Plotly interactive visualizations.

## 2. Box Plot — Sales Distribution by Product
The box plot compares the spread of total sales for each product. The median shows the central sales value, while the box and whiskers show the distribution and possible variation/outliers.

**Interpretation:** A wider box indicates greater variation in sales values. Products with higher median positions generally have higher typical sales values.

## 3. Violin Plot — Sales Density
The violin plot shows both distribution and density of sales values for each product.

**Interpretation:** Wider sections indicate where more observations are concentrated. Comparing the shapes helps identify products with concentrated or widely distributed sales.

## 4. Correlation Heatmap
The heatmap displays correlations among Quantity, Price, and Total Sales.

**Interpretation:** Values close to +1 indicate a strong positive relationship, values close to -1 indicate a negative relationship, and values around 0 indicate a weak linear relationship.

## 5. Sales Trend
The interactive line chart shows Total Sales over time and can be filtered visually by product through the legend.

**Interpretation:** Peaks indicate periods of higher sales activity, while lower points indicate weaker sales periods. Hovering over points provides date, quantity, price, and region details.

## 6. Product Performance
The interactive bar chart compares total sales by product.

**Interpretation:** Taller bars represent products contributing more total sales. Hover information also provides total quantity and average price.

## 7. Sales Distribution
The interactive histogram shows how total sales values are distributed.

**Interpretation:** The shape helps identify common sales ranges and whether the dataset contains unusually high or low sales values.

## 8. Customer Segmentation
Customers are grouped into Low Value, Regular, and High Value segments using total sales thresholds based on the dataset's 33rd and 66th percentiles.

**Interpretation:** High Value customers contribute comparatively higher sales, Regular customers fall in the middle range, and Low Value customers contribute comparatively lower sales. The scatter plot also relates customer quantity to total sales.

## 9. Dashboard Overview
The 2×2 dashboard combines sales trend, product performance, sales distribution, and correlation analysis into one coordinated layout.

**Interpretation:** The combined view allows users to compare time trends, product contribution, distribution patterns, and numerical relationships without opening each chart separately.

## 10. Interactive Features
Plotly charts provide hover information, legends, zooming, panning, and interactive exploration. Customer segmentation is also available as an interactive Plotly scatter plot.

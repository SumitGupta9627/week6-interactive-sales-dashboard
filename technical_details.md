# Technical Details

## Architecture
1. `sales_data.csv` provides the source dataset.
2. `dashboard.py` loads and validates the data using Pandas.
3. Seaborn and Matplotlib generate statistical and dashboard overview visuals.
4. Plotly generates interactive HTML visualizations.
5. Generated files are stored in `visualizations/`.

## Algorithms and Data Processing
- Date values are converted to datetime format.
- Product-level summaries are calculated using Pandas `groupby` and aggregation.
- Numerical correlations are calculated with Pandas correlation functions.
- Customer segments are created using the 33rd and 66th percentiles of customer total sales.

## Main Data Structures
- Pandas DataFrame for the complete sales dataset.
- Grouped DataFrames for product performance and customer segmentation.
- NumPy arrays/values for numeric processing and segment conditions.

## Technical Requirements Covered
- Seaborn statistical plots: box plot, violin plot, and correlation heatmap.
- More than five chart types: box plot, violin plot, heatmap, line chart, bar chart, histogram, and scatter plot.
- Plotly interactive elements with hover data, legends, zooming, and panning.
- Cohesive visual styling using Seaborn themes and Plotly's white template.
- Professional 2×2 dashboard overview.

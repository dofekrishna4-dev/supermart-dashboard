# Supermart Grocery Sales Dashboard

Interactive dashboard answering the four business questions in `project_brief.pdf`.

## Open it
Double-click `supermart_dashboard.html` (needs internet once, to load the Chart.js library).
The data is embedded in the page. Use the Year, Region and Category filters at the top.

## Contents
- `supermart_dashboard.html` - the dashboard
- `project_brief.pdf` - the project brief
- `data/supermart_grocery_sales_original.csv` - source data (9,994 orders, 2015-2018)
- `scripts/clean_and_summarise.py` - fixes the two date formats, writes `data/supermart_grocery_sales_cleaned.csv`, prints the headline numbers

## Notes
- Order dates use two formats (dd-mm-yyyy and m/d/yyyy); both are converted.
- The data has no product-name column, so sub-category is used as the product level.
- All orders are in Tamil Nadu; North has one order.
- "High sales, low profit" = top-half sales with margin below the overall margin.

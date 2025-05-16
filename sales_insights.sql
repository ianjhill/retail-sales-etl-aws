-- Top 5 sold Products
SELECT 
  product_name, 
  ROUND(SUM(total_price), 2) AS total_revenue
FROM cleaned_cleaned
GROUP BY product_name
ORDER BY total_revenue DESC
LIMIT 5;

-- Sales by Dept.
SELECT 
  department, 
  SUM(quantity_sold) AS total_units,
  ROUND(SUM(total_price), 2) AS total_revenue
FROM cleaned_cleaned
GROUP BY department
ORDER BY total_revenue DESC;

-- Sales over Time (May)
SELECT 
  date, 
  SUM(quantity_sold) AS total_units_sold,
  ROUND(SUM(total_price), 2) AS total_sales
FROM cleaned_cleaned
GROUP BY date
ORDER BY date;

-- Top 3 Cities by Revenue
SELECT 
  location, 
  ROUND(SUM(total_price), 2) AS revenue
FROM cleaned_cleaned
GROUP BY location
ORDER BY revenue DESC
LIMIT 3;

-- Avg. Order Value by Dept.
SELECT 
  department, 
  ROUND(AVG(total_price), 2) AS avg_order_value
FROM cleaned_cleaned
GROUP BY department
ORDER BY avg_order_value DESC;
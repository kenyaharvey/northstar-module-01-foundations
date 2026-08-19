# Brainstorm: Crescent Bakery Analytical Questions

## Prompt used

Role: Act as a senior data analyst helping me scope an analytical project for
a small fictional bakery client.

Task: Brainstorm analytical questions I should consider asking of the dataset
described below. I'm at the Define stage of the analytics lifecycle and need
a candidate list of questions before I start writing any code.

Context: The dataset is for Crescent Bakery, a fictional regional bakery.
50 rows, one row per customer. Columns:

- customer_id: string, unique identifier per customer (nominal)
- region: categorical, one of {Downtown, North Side, South Side, West End} (nominal)
- first_visit_year: integer year between 2018 and 2025 inclusive (interval)
- satisfaction: integer 1 to 5, customer satisfaction rating (ordinal)
- total_spent_usd: continuous, total dollars the customer has spent (ratio)
- visits_last_year: integer, number of visits in the last year (ratio)

The bakery is interested in understanding customer behavior to inform
marketing and product decisions.

Constraints:
1. Only suggest questions that can be answered from the columns listed above.
   Don't invent additional columns.
2. For each suggested question, identify which columns would be used and
   what statistical method would be appropriate.
3. Make sure the statistical methods you propose are appropriate for the
   data type of each column (mean for ratio, mode for nominal, etc.).

Output Format: A numbered list of 8 to 12 analytical questions. For each:
- The question (one sentence)
- The columns involved
- The recommended statistical or visualization method


## Tool 1: Claude output

1. **Which region generates the highest average customer spend?**
   - Columns: `region`, `total_spent_usd`
   - Method: Group by region, compare means (bar chart of mean `total_spent_usd` per region); one-way ANOVA or Kruskal-Wallis if checking whether differences are statistically significant.

2. **Is there a relationship between how long someone has been a customer and how much they've spent?**
   - Columns: `first_visit_year`, `total_spent_usd`
   - Method: Scatter plot with Pearson or Spearman correlation coefficient.

3. **Does customer satisfaction correlate with visit frequency?**
   - Columns: `satisfaction`, `visits_last_year`
   - Method: Spearman rank correlation (appropriate since `satisfaction` is ordinal), visualized with a box plot of `visits_last_year` grouped by satisfaction level.

4. **What is the overall distribution of customer satisfaction ratings?**
   - Columns: `satisfaction`
   - Method: Frequency table / bar chart; median and mode as the central tendency measures appropriate for ordinal data.

5. **How is total spending distributed across all customers, and are there outliers?**
   - Columns: `total_spent_usd`
   - Method: Histogram and box plot; mean, median, standard deviation (ratio data supports all of these).

6. **Does the region a customer belongs to relate to their satisfaction level?**
   - Columns: `region`, `satisfaction`
   - Method: Cross-tabulation (contingency table) with a stacked bar chart; Chi-square test of independence.

7. **Are newer customers (recent first-visit year) visiting less frequently than long-tenured ones?**
   - Columns: `first_visit_year`, `visits_last_year`
   - Method: Scatter plot with Pearson/Spearman correlation, or group customers by first-visit-year cohort and compare mean `visits_last_year` per cohort.

8. **What's the average number of visits last year, and how much does it vary?**
   - Columns: `visits_last_year`
   - Method: Mean and standard deviation, histogram for shape of distribution.

9. **Which region has the most customers, and how is the customer base distributed geographically?**
   - Columns: `customer_id`, `region`
   - Method: Frequency count / mode; pie chart or bar chart of counts per region.

10. **Is there a relationship between visit frequency and total spending (i.e., do frequent visitors spend more overall)?**
    - Columns: `visits_last_year`, `total_spent_usd`
    - Method: Scatter plot with Pearson correlation coefficient; optionally a simple linear regression to quantify the relationship.

11. **Has the year customers first visited shifted the regional composition of the customer base over time?**
    - Columns: `first_visit_year`, `region`
    - Method: Grouped bar chart (count of customers per region per first-visit-year cohort); Chi-square test if testing for association.

12. **Do high-spending customers (top spenders) tend to report higher satisfaction?**
    - Columns: `total_spent_usd`, `satisfaction`
    - Method: Spearman correlation (mixing ratio and ordinal data calls for a rank-based method); box plot of `total_spent_usd` grouped by satisfaction level.

A note on method choice: since `satisfaction` is ordinal, I've used Spearman correlation and medians wherever it's involved rather than Pearson correlation or means — Pearson/means technically run on ordinal codes but assume equal spacing between categories, which a 1–5 rating scale doesn't guarantee.

## Tool 2: Gemini output

Here is a targeted candidate list of analytical questions scoped strictly to Crescent Bakery’s dataset, tailored for the Define stage of your analytics lifecycle:

## 1: What is the overall customer satisfaction level, and how is it distributed across the customer base?

Columns involved: satisfaction

Method: Described using the median and interquartile range (IQR) or mode, alongside a bar chart showing the frequency distribution of ratings (1 through 5).

## 2: Which region generates the highest average spending per customer?
Columns involved: region, total_spent_usd

Method: Calculate the mean total spent per region (or median if heavily skewed) paired with a one-way ANOVA or Kruskal-Wallis test to check for significant differences across regions, visualized using a grouped box plot.

## 3: Is there a relationship between customer satisfaction ratings and total spend?
Columns involved: satisfaction, total_spent_usd

Method: Compute Spearman's rank correlation coefficient (ρ)—appropriate for ordinal vs. continuous data—and display the distribution using a grouped box plot (spend distribution per satisfaction rating level).

## 4: Do customers who visit more frequently also spend more in total?
Columns involved: visits_last_year, total_spent_usd

Method: Compute Pearson’s correlation coefficient (r) (or Spearman’s if non-normal) and render a scatter plot with a trendline.

## 5: How are Crescent Bakery’s customers distributed geographically across regions?
Columns involved: region

Method: Compute the mode and categorical frequency/relative percentage of customers per region, visualized with a horizontal bar chart.

## 6: Are more recent customer cohorts (by first_visit_year) spending differently compared to long-term customers?
Columns involved: first_visit_year, total_spent_usd

Method: Group continuous spending by cohort year using median total spent per cohort (given small sample size per year, e.g., ~50 rows across 8 years), visualized via a line chart or annual box plot.

## 7: Does customer visit frequency in the last year vary significantly by region?
Columns involved: region, visits_last_year

Method: Compare median/mean visits per region using a Kruskal-Wallis test or one-way ANOVA, presented via a bar chart with error bars.

## 8: Are earlier cohorts (older first_visit_year) visiting more frequently than newer cohorts?
Columns involved: first_visit_year, visits_last_year

Method: Compute Spearman's rank correlation between tenure year and visit count, supported by a bivariate scatter plot or aggregated mean visit line graph by year.

## 9: Do regional customer bases exhibit different levels of reported satisfaction?
Columns involved: region, satisfaction

Method: Perform a Chi-Square Test of Independence (or Fisher's Exact Test due to the small N=50 count), paired with a 100% stacked bar chart showing satisfaction proportions per region.

## 10: Is higher visit frequency associated with higher customer satisfaction ratings?
Columns involved: visits_last_year, satisfaction

Method: Calculate Spearman’s rank correlation between visits and satisfaction score, visualized using a jittered scatter plot or box plot of visits grouped by satisfaction level.

## Verification



| # | Verification question | Source | Columns used | Column check | Method check | Business context check | Status |
|---|---|---|---|---|---|---|---|
| 1 | Which region generates the highest average customer spend?| Both | `region`, `total_spent_usd` | Pass | Pass: compare mean or median spending by region | Pass | ✓ Verified
| 2 | Is there a relationship between how long someone has been a customer and how much they've spent?| Tool 1 | `first_visit_year`, `total_spent_usd` | Pass | Pass: use a scatter plot; use Pearson correlation if the relationship is approximately linear with no major outliers, or Spearman correlation if it is monotonic, non-normal, or has outliers.  | Pass | ✓ Verified
| 3 | Does customer satisfaction correlate with visit frequency?| Both | `satisfaction`, `visits_last_year` | Pass: Use Spearman rank correlation because `satisfaction` is ordinal. Visualize the relationship with a box plot of `visits_last_year` grouped by satisfaction level. | Pass | ✓ Verifed
| 4 | What is the overall distribution of customer satisfaction ratings?| Both | `satisfaction` | Pass | Pass: Frequency table / bar chart; median and mode as the central tendency measures appropriate for ordinal data. | Pass | ✓ Verified
| 5 | How is total spending distributed across all customers, and are there outliers?| Tool 1 | total_spent_usd`| Pass | Pass: Histogram and box plot; mean, median, standard deviation (ratio data supports all of these). | Pass | ✓ Verified
| 6 | Does the region a customer belongs to relate to their satisfaction level?| Both | `region`, `satisfaction` | Pass | Pass: Use a cross-tabulation (contingency table) and stacked bar chart; use a chi-square test of independence if expected cell counts meet the required threshold. | Pass | ✓ Verified
| 7 | Are newer customers (recent first-visit year) visiting less frequently than long-tenured ones?| Tool 1 | `first_visit_year`, `visits_last_year` | Pass: tenure can be derived from `first_visit_year` | Pass: Use a scatter plot with Pearson or Spearman correlation, or group customers into first-visit-year cohorts and compare mean or median `visits_last_year` across cohorts. | Pass | ✓ Verified
| 8 | What's the average number of visits last year, and how much does it vary?| Tool 1 | `visits_last_year` | Pass | Pass: Use the mean and standard deviation; inspect the distribution with a histogram. Also report the median and IQR if the count distribution is skewed or has outliers.| Pass | ✓ Verified
| 9 | Which region has the most customers, and how is the customer base distributed geographically? | Tool 1 | `customer_id`, `region` | Pass | Pass: Frequency count / mode; bar chart of counts per region. | Pass | ✓ Verified
| 10 | Is there a relationship between visit frequency and total spending (i.e., do frequent visitors spend more overall)? | Tool 1 | `visits_last_year`, `total_spent_usd` | Pass | Pass: Use a scatter plot; use Pearson correlation and simple linear regression if the relationship is approximately linear with no major outliers, or Spearman correlation if the relationship is monotonic, skewed, or has outliers. | Pass | ✓ Verified
| 11 | Has the year customers first visited shifted the regional composition of the customer base over time?| Tool 1 | `first_visit_year`, `region` | Pass | Pass: Use a grouped bar chart or a table of regional counts/proportions for each `first_visit_year`. Use a chi-square test of independence to test association only if expected cell counts are sufficient.  | Pass | ✓ Verified
| 12 | Do high-spending customers (top spenders) tend to report higher satisfaction?| Tool 1 | `total_spent_usd`, `satisfaction` | Define “high-spending” using a cutoff derived from `total_spent_usd`, such as the top 20% or 25%. | Pass: Use Spearman rank correlation because `satisfaction` is ordinal and spending is ratio data; visualize with a box plot of `total_spent_usd` grouped by satisfaction level. | Pass | ✓ Verified
| 13 | What is the overall customer satisfaction level, and how is it distributed across the customer base?| Both | 'satisfaction' | Pass | Pass: Described using the median and interquartile range (IQR) or mode, alongside a bar chart showing the frequency distribution of ratings (1 through 5). | Pass | ✓ Verified
| 14 | Which region generates the highest average spending per customer?| Both | 'region, total_spent_usd' | Pass | Pass: Calculate the mean total spent per region (or median if heavily skewed) paired with a one-way ANOVA or Kruskal-Wallis test to check for significant differences across regions, visualized using a grouped box plot. | Pass | ✓ Verified
| 15 | Is there a relationship between customer satisfaction ratings and total spend?| Tool 2 | 'satisfaction, total_spent_usd' | Pass | Pass: Compute Spearman's rank correlation coefficient (\(\rho\)), which is appropriate for ordinal satisfaction ratings and continuous spending data. Display spending distributions with a box plot grouped by satisfaction level. | Pass | ✓  Verified
| 16 | Do customers who visit more frequently also spend more in total?| 'visits_last_year, total_spent_usd' | Pass | Pass: Compute Pearson’s correlation coefficient (\(r\)) if the relationship is approximately linear and there are no major outliers; use Spearman’s correlation if the relationship is monotonic, skewed, or non-normal. Visualize with a scatter plot and trendline. | Pass | ✓ Verified
| 17 | How are Crescent Bakery’s customers distributed geographically across regions?| Both | 'region' | Pass | Pass: Compute the mode and categorical frequency/relative percentage of customers per region, visualized with a horizontal bar chart. | Pass | ✓ Verified
| 18| Are more recent customer cohorts (by first_visit_year) spending differently compared to long-term customers?| Tool 2 | 'first_visit_year, total_spent_usd' | Pass | Pass: Group continuous spending by cohort year using median total spent per cohort (given small sample size per year, e.g., ~50 rows across 8 years), visualized via a line chart or annual box plot. | Pass | ✓ Verified
| 19| Does customer visit frequency in the last year vary significantly by region?| Tool 2 | 'region, visits_last_year' | Pass | Pass: Compare median/mean visits per region using a Kruskal-Wallis test or one-way ANOVA, presented via a bar chart with error bars. | Pass | ✓  Verified
| 20 | Are earlier cohorts (older first_visit_year) visiting more frequently than newer cohorts? | Both | 'first_visit_year, visits_last_year' | Pass | Pass : Compute Spearman's rank correlation between tenure year and visit count, supported by a bivariate scatter plot or aggregated mean visit line graph by year. | Pass | ✓  Verified
| 21 | Do regional customer bases exhibit different levels of reported satisfaction? | Both |  'region, satisfaction' | Pass | Pass: Perform a Chi-Square Test of Independence (or Fisher's Exact Test due to the small N=50 count), paired with a 100% stacked bar chart showing satisfaction proportions per region. | Pass | ✓ Verified
| 22 | Is higher visit frequency associated with higher customer satisfaction ratings?| Both | 'visits_last_year, satisfaction' | Pass | Pass: Calculate Spearman’s rank correlation between visits and satisfaction score, visualized using a jittered scatter plot or box plot of visits grouped by satisfaction level. | Pass | ✓ Verified


## Verified question list

| # | Verified question | Tool source |
|---|---|---|
| 1 | Which region generates the highest average customer spend? | Both |
| 2 | How is total spending distributed across all customers, and are there outliers? | Tool 1 |
| 3 | Is visit frequency associated with total spending? | Both |
| 4 | Does customer satisfaction correlate with visit frequency? | Both |
| 5 | Do high-spending customers tend to report higher satisfaction? | Tool 1 |
| 6 | Does customer satisfaction differ across regions? | Both |
| 7 | Which region has the most customers, and how is the customer base distributed geographically? | Both |
| 8 | What is the average number of visits last year, and how much does it vary? | Tool 1 |
| 9 | Do newer customers visit less frequently than long-tenured customers? | Both |
| 10 | Do recent customer cohorts spend differently from longer-term customers? | Tool 2 |
| 11 | Does visit frequency differ by region? | Tool 2 |
| 12 | Has regional composition shifted across first-visit-year cohorts? | Tool 1 |
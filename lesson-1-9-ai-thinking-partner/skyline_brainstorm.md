# Brainstorm: Skyline Online Courses Analytical Questions

## Prompt used

Role: Act as a senior data analyst helping me scope an analytical project for a small online learning platform client.

Task: Brainstorm analytical questions I should consider asking of the dataset described below. I'm at the Define stage of the analytics lifecycle and need a candidate list of questions before I start writing any code.

Context: The dataset is for Skyline, a small online learning platform. One row per student enrollment. Columns:

* `enrollment_id`: string, unique identifier per enrollment (nominal)
* `course_name`: categorical, name of the course enrolled in (nominal)
* `enrollment_year`: integer year, the year the student enrolled (interval)
* `final_grade`: categorical/ordered grade (e.g., A/B/C/D/F, or similar ordered scale) (ordinal)
* `hours_studied`: continuous, total hours the student spent studying (ratio)
* `completion_status`: categorical, whether the student completed the course (e.g., Completed/Dropped/In Progress) (nominal)

Skyline is interested in understanding course performance and student behavior to inform curriculum and support decisions.

Constraints:

1. Only suggest questions that can be answered from the columns listed above. Don't invent additional columns.
2. For each suggested question, identify which columns would be used and what statistical method would be appropriate.
3. Make sure the statistical methods you propose are appropriate for the data type of each column (mean for ratio, mode for nominal, median/rank-based methods for ordinal, etc.). Do not propose a method that assumes equal spacing or numeric meaning for a nominal or ordinal column.

Output Format: A numbered list of 8 to 12 analytical questions. For each:

* The question (one sentence)
* The columns involved
* The recommended statistical or visualization method


## Tool 1: Claude output

1. Which course has the highest completion rate?
Columns: course_name, completion_status
Method: Cross-tabulation (contingency table) of course by completion status; bar chart of completion rate per course.

2. Is there a relationship between hours studied and final grade?
Columns: hours_studied, final_grade
Method: Spearman rank correlation (appropriate since final_grade is ordinal and shouldn't be treated as numeric); box plot of hours_studied grouped by grade level.

3. What is the distribution of final grades across all enrollments?
Columns: final_grade
Method: Frequency table / bar chart; median and mode as measures of central tendency for ordinal data.

4. Does course completion status vary by enrollment year?
Columns: enrollment_year, completion_status
Method: Cross-tabulation with a grouped bar chart; Chi-square test of independence.

5. How many hours do students typically study, and how much does that vary?
Columns: hours_studied
Method: Mean, median, and standard deviation; histogram to show distribution shape.

6. Which courses attract the most enrollments?
Columns: course_name, enrollment_id
Method: Frequency count / mode; bar chart of enrollment counts per course.

7. Do students who study more hours have a higher likelihood of completing the course?
Columns: hours_studied, completion_status
Method: Box plot of hours_studied grouped by completion status; Mann-Whitney U test (or Kruskal-Wallis if more than two completion categories) since the outcome is grouped/nominal and the predictor is continuous.

8. Has student enrollment grown or declined over time?
Columns: enrollment_year, enrollment_id
Method: Line chart of enrollment counts by year; trend inspection (no correlation coefficient needed since one variable is a count, not paired continuous data).

9. Do certain courses tend to produce better final grades than others?
Columns: course_name, final_grade
Method: Cross-tabulation with stacked bar chart of grade distribution per course; Kruskal-Wallis test (rank-based, appropriate for an ordinal outcome across multiple groups).

10. Is there a relationship between the year a student enrolled and how many hours they studied?
Columns: enrollment_year, hours_studied
Method: Scatter plot with Pearson or Spearman correlation coefficient.

11. Do dropped students show different study-hour patterns than those who completed or are still in progress?
Columns: completion_status, hours_studied
Method: Box plot comparing hours_studied across the three completion categories; Kruskal-Wallis test.

12. Which combination of course and enrollment year has the lowest completion rate, signaling where support may be needed?
Columns: course_name, enrollment_year, completion_status
Method: Grouped cross-tabulation (course × year) with completion rate as the cell value; heatmap visualization to spot low-performing cells.

## Tool 2: Gemini output

1. What is the overall distribution of student completion statuses across the platform?
Columns involved: completion_status
Method: Compute frequency counts, percentages, and the mode, visualized using a bar chart or pie chart.

2. Which specific courses generate the highest total volume of student enrollments?
Columns involved: course_name
Method: Calculate category frequencies and the mode, visualized via a horizontal bar chart.

3. What is the difference in study hours between students who complete their courses versus those who drop out?
Columns involved: hours_studied, completion_status
Method: Compare group means or medians using an independent samples t-test or Mann-Whitney U test, paired with a grouped box plot.

4. Is there a monotonic relationship between the total hours studied and student final grades?
Columns involved: hours_studied, final_grade
Method: Compute Spearman's rank correlation coefficient (treating final grade as ordinal) and display the distribution using a box plot of study hours grouped by grade level.

5. Does the distribution of course completion statuses vary significantly across different courses?
Columns involved: course_name, completion_status
Method: Perform a Chi-Square Test of Independence to evaluate categorical association, visualized with a 100% stacked bar chart.

6. How has the annual volume of total student enrollments evolved across enrollment years?
Columns involved: enrollment_year
Method: Calculate annual frequency counts (treating year as interval/numeric trend), visualized using a time-series line chart.

7. How do the proportions of final grades differ across individual courses?
Columns involved: course_name, final_grade
Method: Analyze cross-tabulated proportions using a Chi-Square Test of Independence, visualized via a faceted or stacked bar chart.

8. Have the average study hours invested by students changed across different enrollment years?
Columns involved: enrollment_year, hours_studied
Method: Compute mean or median study hours per year using a one-way ANOVA or Kruskal-Wallis test, visualized with a line or box plot.

9. Are higher final grades associated with specific completion statuses?
Columns involved: completion_status, final_grade
Method: Evaluate the association between two categorical/ordinal variables using a Chi-Square Test of Independence or contingency table analysis, displayed with a mosaic plot or stacked bar chart.

10. How do median study hours compare across different final grade categories?
Columns involved: final_grade, hours_studied
Method: Calculate group medians and interquartile ranges (IQR) evaluated via a Kruskal-Wallis test, visualized using a box plot.

| # | Verification question | Source | Columns used | Column check | Method check | Business context check | Status |
|---|---|---|---|---|---|---|---|
| 1 |  Which course has the highest completion rate?| Both | Pass | Pass | Pass | Pass |  ✓  Verified
| 2 |  Is there a relationship between hours studied and final grade?| Both | Pass | Pass | Pass | Pass | ✓ Verified
| 3 |  What is the distribution of final grades across all enrollments?| Tool 1 | Pass | Pass | Pass | Pass | ✓ Verified
| 4 |  Does course completion status vary by enrollment year?| Both | Pass | Pass | Pass | Pass | ✓ Verified 
| 5 |  How many hours do students typically study, and how much does that vary?| Both | Pass | Pass | Pass | Pass |  ✓ Verified
| 6 |  Which courses attract the most enrollments?| Both | Pass | Pass | Pass | Pass | ✓ Verified
| 7 |  Do students who study more hours have a higher likelihood of completing the course?| Tool 1 | Pass | Pass | Pass | Pass | ✓ Verified
| 8 | Has student enrollment grown or declined over time?| Both | Pass | Pass | Pass | Pass | ✓  Verified
| 9 | Do certain courses tend to produce better final grades than others?| Tool 1 | Pass | Pass | Pass | Pass |  ✓ Verified
| 10 | Is there a relationship between the year a student enrolled and how many hours they studied?| Tool 1 | Pass | Pass | Pass | Pass | ✓ Verified
| 11 | Do dropped students show different study-hour patterns than those who completed or are still in progress?| Tool 1 | Pass | Pass | Pass | Pass | ✓ Verified
| 12 | Which combination of course and enrollment year has the lowest completion rate, signaling where support may be needed?| Tool 1 | Pass | Pass | Pass | Pass | ✓ Verified
| 13 | What is the overall distribution of student completion statuses across the platform?| Tool 2 | Pass | Pass | Pass | Pass |  ✓ Verified
| 14 | Which specific courses generate the highest total volume of student enrollments?| Both | Fail | Pass | Pass | Pass | Context-missing
| 15 | What is the difference in study hours between students who complete their courses versus those who drop out?| Tool 2 | Pass | Pass | Pass |Pass | ✓ Verified
| 16 | Is there a monotonic relationship between the total hours studied and student final grades?| Both | Pass | Pass | Pass | Pass | ✓ Verified
| 17 | Does the distribution of course completion statuses vary significantly across different courses?| Both | Pass | Pass | Pass | Pass | ✓ Verified
| 18 | How has the annual volume of total student enrollments evolved across enrollment years?| Both | Pass | Pass | Pass | Pass | ✓ Verified
| 19 | How do the proportions of final grades differ across individual courses?| Tool 2 | Pass | Pass | Pass | Pass | ✓  Verified
| 20 | Have the average study hours invested by students changed across different enrollment years?| Tool 2 | Pass | Pass | Pass | Pass | ✓ Verified 
| 21 | Are higher final grades associated with specific completion statuses?| Tool 2 | Pass | Pass | Pass | Pass | ✓ Verified
| 22 | How do median study hours compare across different final grade categories?| Tool 2 | Pass | Pass |  Pass | Pass | ✓ Verified


## Verified question list

| # | Theme | Verified question |
|---|---|---|
| 1 | Course Performance | Which course has the highest completion rate? |
| 2 | Course Performance | Which courses attract the most enrollments? |
| 3 | Course Performance | Do certain courses tend to produce better final grades than others? |
| 4 | Course Performance | Which specific courses generate the highest total volume of student enrollments? |
| 5 | Course Performance | How do the proportions of final grades differ across individual courses? |
| 6 | Course Performance | Does the distribution of course completion statuses vary significantly across different courses? |
| 7 | Student Behavior | Is there a relationship between hours studied and final grade? |
| 8 | Student Behavior | What is the distribution of final grades across all enrollments? |
| 9 | Student Behavior | How many hours do students typically study, and how much does that vary? |
| 10 | Student Behavior | Is there a monotonic relationship between the total hours studied and student final grades? |
| 11 | Student Behavior | How do median study hours compare across different final grade categories? |
| 12 | Student Behavior | What is the difference in study hours between students who complete their courses versus those who drop out? |
| 13 | Completion Patterns | What is the overall distribution of student completion statuses across the platform? |
| 14 | Completion Patterns | Does course completion status vary by enrollment year? |
| 15 | Completion Patterns | Do students who study more hours have a higher likelihood of completing the course? |
| 16 | Completion Patterns | Do dropped students show different study-hour patterns than those who completed or are still in progress? |
| 17 | Completion Patterns | Which combination of course and enrollment year has the lowest completion rate, signaling where support may be needed? |
| 18 | Completion Patterns | Are higher final grades associated with specific completion statuses? |
| 19 | Time Trends | How has the annual volume of total student enrollments evolved across enrollment years? |
| 20 | Time Trends | Has student enrollment grown or declined over time? |
| 21 | Time Trends | Is there a relationship between the year a student enrolled and how many hours they studied? |
| 22 | Time Trends | Have the average study hours invested by students changed across different enrollment years? |
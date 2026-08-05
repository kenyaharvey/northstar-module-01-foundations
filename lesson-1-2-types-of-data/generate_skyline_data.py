
# generate_skyline_data.py
# Lesson 1.2: Types of Data and Where to Find It
# Author: Kenya Harvey
# Date: 08/05/2026
#
# Generates a synthetic dataset of 100 fictional Skyline Hotel guests
# illustrating the four scales of measurement (nominal, ordinal, interval,
# ratio). Saves the result as skyline_guests.csv.

import random
import numpy as np
import pandas as pd

random.seed(123)
np.random.seed(123)

n_students = 100

# course_name (nominal scale: categorial with no order)
course_name = np.random.choice(
    ["Intro to Analytics", "Python for Beginners", "SQL Basics", "Tableau Fundamentals", "Statistics 101"], size=n_students)


# final_grade (ordinal scale: ordered categories with unequal gaps)
final_grade = np.random.choice(
    ["A", "B", "C", "D", "F"], size=n_students)


# enrollment_year (interval scale: ordered with equal gaps, no true zero)
enrollment_year = np.random.randint(2022, 2027, size=n_students)

# hours_studied (ratio scale: ordered, equal gaps, true zero)
hours_studied = np.random.normal(30, 5, n_students)
hours_studied = np.round(hours_studied, 2)
hours_studied = np.maximum(hours_studied, 0)

# enrollment_ids (nominal: numerical-looking labels with no order)
enrollment_ids = [f"ENR-{random.randint(1000, 9999)}"for _ in range(n_students)]

# completion_status (nominal scale: categorical with no order)
completion_status = np.random.choice(["Completed", "In Progress", "Dropped"], size=n_students, p=[0.54, 0.25, 0.21])

skyline_enrollments = pd.DataFrame({
    "Enrollment_ids": enrollment_ids,
    "Course_name": course_name,
    "enrollment_year": enrollment_year,
    "Final_grade": final_grade,
    "Hours_studied": hours_studied,
    "Completion_status": completion_status
})

print(skyline_enrollments.head(10))
print(f"\nShape:{skyline_enrollments.shape}")
print(f"\nColumn types:\n{skyline_enrollments.dtypes}")

output_path = "skyline_enrollments.csv"
skyline_enrollments.to_csv(output_path, index=False)
print(f"\nDataset saved to {output_path}")

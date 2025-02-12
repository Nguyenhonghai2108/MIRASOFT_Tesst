from collections import defaultdict
import random

def generate_student_ages(class_sizes, avg_age_years, avg_age_months, age_variation=6):
    avg_age_in_months = avg_age_years * 12 + avg_age_months
    lower_bound = avg_age_in_months - age_variation
    upper_bound = avg_age_in_months + age_variation
    
    student_ages = {i: [] for i in range(1, len(class_sizes) + 1)}
    
    for class_id, size in enumerate(class_sizes, start=1):
        student_ages[class_id] = [random.randint(avg_age_in_months - 12, avg_age_in_months + 12) for _ in range(size)]
    
    return student_ages, lower_bound, upper_bound

def count_students_by_age(student_ages, lower_bound, upper_bound):
    result = defaultdict(lambda: {'younger': 0, 'older': 0})
    
    for class_id, ages in student_ages.items():
        for age in ages:
            if age < lower_bound:
                result[class_id]['younger'] += 1
            elif age > upper_bound:
                result[class_id]['older'] += 1
    
    return result

# Given class sizes
class_sizes = [35]*5 + [45]*6 + [30]*10 + [40]*4

# Average age
avg_age_years = 20
avg_age_months = 8

# Generate student ages and count the ones outside the range
student_ages, lower_bound, upper_bound = generate_student_ages(class_sizes, avg_age_years, avg_age_months)
count_result = count_students_by_age(student_ages, lower_bound, upper_bound)

# Print the result
for class_id, counts in count_result.items():
    print(f"Class {class_id}: Younger than {avg_age_years}y {avg_age_months-6}m: {counts['younger']}, Older than {avg_age_years}y {avg_age_months+6}m: {counts['older']}")

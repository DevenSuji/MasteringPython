# Class Average program with sequence-controlled repetition

# Initialization phase
total = 0  # Sum of grades
grade_counter = 0
grades = [98, 71, 76, 87, 83, 90, 57, 79, 82, 94]  # List of 10 grades

# Processing phase
for grade in grades:
    total += grade  # Adding current grade to the running total
    grade_counter += 1  # Indicate that one more grade was added.

# Termination phase
average = total / grade_counter
print(f'Class average is {average}')

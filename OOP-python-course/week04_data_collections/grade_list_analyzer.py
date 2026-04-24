grades_FGA = []
for i in range(1, 6):
    grade = float(input(f"Enter grade {i}: "))
    grades_FGA.append(grade)

average = sum(grades_FGA) / len(grades_FGA)
highest = max(grades_FGA)
lowest = min(grades_FGA)

print(f"Average Grade: {average:.1f}")
print(f"Highest Grade: {highest}")
print(f"Lowest Grade: {lowest}")



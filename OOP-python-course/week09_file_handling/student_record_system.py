name_FGA = input("Enter student name: ")
course_FGA = input("Enter course: ")
with open("students.txt", "a") as file_FGA:
    file_FGA.write(name_FGA + "," + course_FGA + "\n")

print("\nStudent Records")
with open("students.txt", "r") as file_FGA:
    for line_FGA in file_FGA:
        print(line_FGA.strip())



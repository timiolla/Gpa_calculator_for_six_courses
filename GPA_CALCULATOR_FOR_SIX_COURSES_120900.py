def calculate_gpa():
    # Dictionary to store grade points
    grade_points = {
        'A': 5.0,
        'B': 4.0,
        'C': 3.0,
        'D': 2.0,
        'F': 0.0
    }

    total_credits = 0
    total_grade_points = 0

    print("Enter details for 6 courses:")
    
    for i in range(6):
        print(f"\nCourse {i+1}:")
        # Get course credit hours
        while True:
            try:
                credits = float(input("Enter credit hours (e.g., 3): "))
                if credits < 0:
                    print("Credit hours cannot be negative. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Enter a number for credit hours.")
        
        # Get course grade
        while True:
            grade = input("Enter grade (A, B, C, D, F): ").upper()
            if grade in grade_points:
                break
            else:
                print("Invalid grade. Enter A, B, C, D, or F.")

        # Calculate grade points for the course
        course_grade_points = grade_points[grade] * credits
        total_grade_points += course_grade_points
        total_credits += credits

    # Calculate GPA
    if total_credits == 0:
        gpa = 0.0
        print("No credits entered, GPA set to 0.0")
    else:
        gpa = total_grade_points / total_credits
        print(f"\nTotal Credits: {total_credits}")
        print(f"Total Grade Points: {total_grade_points:.2f}")
        print(f"Your GPA is: {gpa:.2f}")

# Run the program
if __name__ == "__main__":
    print("Student GPA Calculator for 6 Courses")
    calculate_gpa()

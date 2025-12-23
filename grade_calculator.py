# Student Grade Calculator
# Week 2 Project - Control Flow & Data Structures
# Author: [Your Name]

import os

def calculate_grade(average):
    """Calculate grade and provide a personalized comment."""
    if average >= 90:
        return 'A', 'Excellent! Keep up the great work!'
    elif average >= 80:
        return 'B', 'Very Good! You\'re doing well.'
    elif average >= 70:
        return 'C', 'Good. Room for improvement.'
    elif average >= 60:
        return 'D', 'Needs Improvement. Please study more.'
    else:
        return 'F', 'Failed. Please seek help from teacher.'

def get_valid_number(prompt, min_val=0, max_val=100):
    """Input validation for numbers within a specific range."""
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Error: Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input! Please enter a valid numeric value.")

def display_summary(students):
    """Prints a formatted table of all student results."""
    if not students:
        print("\n[!] No student records found.")
        return

    print("\n" + "=" * 85)
    print(f"{'Name':<20} | {'Math':>5} | {'Sci':>5} | {'Eng':>5} | {'Avg':>6} | {'Grade':^5} | Comment")
    print("-" * 85)
    
    for s in students:
        marks = s['marks']
        print(f"{s['name']:<20} | {marks[0]:>5.0f} | {marks[1]:>5.0f} | {marks[2]:>5.0f} | "
              f"{s['average']:>6.1f} | {s['grade']:^5} | {s['comment']}")
    print("=" * 85)

def save_to_file(students):
    """Saves the current session data to a text file."""
    if not students:
        print("\n[!] Nothing to save.")
        return
    
    try:
        with open("grade_report.txt", "w") as f:
            f.write("STUDENT GRADE REPORT\n" + "="*30 + "\n")
            for s in students:
                f.write(f"Name: {s['name']} | Avg: {s['average']:.2f} | Grade: {s['grade']}\n")
        print("\n[✓] Report successfully saved to 'grade_report.txt'")
    except Exception as e:
        print(f"An error occurred while saving: {e}")

def main():
    # This list will store dictionaries for each student
    # Structure: {'name': str, 'marks': [], 'average': float, 'grade': str, 'comment': str}
    all_students = []

    while True:
        print("\n" + "═" * 30)
        print("  STUDENT GRADE SYSTEM")
        print("" + "═" * 30)
        print("1. Add Student Marks")
        print("2. View All Results & Stats")
        print("3. Search for a Student")
        print("4. Save Report to File")
        print("5. Exit")
        
        choice = input("\nSelect an option (1-5): ")

        if choice == '1':
            while True:
                try:
                    num = int(input("\nHow many students to add? "))
                    if num > 0: break
                    print("Enter a positive number.")
                except ValueError: print("Invalid input.")

            for i in range(num):
                print(f"\n--- Entry {i+1} ---")
                name = input("Student Name: ").strip()
                while not name:
                    name = input("Name cannot be empty. Student Name: ").strip()
                
                m = get_valid_number("  Math Mark: ")
                s = get_valid_number("  Science Mark: ")
                e = get_valid_number("  English Mark: ")
                
                avg = (m + s + e) / 3
                grade, comment = calculate_grade(avg)
                
                all_students.append({
                    'name': name,
                    'marks': [m, s, e],
                    'average': avg,
                    'grade': grade,
                    'comment': comment
                })

        elif choice == '2':
            display_summary(all_students)
            if all_students:
                avgs = [s['average'] for s in all_students]
                print(f"Class Average: {sum(avgs)/len(avgs):.2f}")
                print(f"Highest Score: {max(avgs):.2f}")
                print(f"Lowest Score:  {min(avgs):.2f}")

        elif choice == '3':
            query = input("\nEnter student name to search: ").lower()
            found = [s for s in all_students if query in s['name'].lower()]
            if found:
                display_summary(found)
            else:
                print("\n[!] No student found with that name.")

        elif choice == '4':
            save_to_file(all_students)

        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
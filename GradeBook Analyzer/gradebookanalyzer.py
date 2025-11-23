# --- Task 1: Project Setup ---
# Name: soumya subhashri sahoo
# Date:24-11-2025
# Title: GradeBook Analyzer

import csv  # For Task 2 (CSV Import)
import statistics # For Task 3 (Median)
import sys # To exit the program

def show_menu():
    """Task 1: Prints the main welcome menu."""
    print("\n" + "="*40)
    print("      GradeBook Analyzer CLI Tool      ")
    print("="*40)
    print("1. Enter student marks manually")
    print("2. Load marks from a CSV file")
    print("3. Exit program")
    return input("Please choose an option (1-3): ")

def get_data_manual():
    """Task 2a: Get student names and marks via manual input."""
    print("\n--- Manual Data Entry ---")
    marks_dict = {}
    
    
    while True:
        num_students = int(input("How many students to enter? "))
        if num_students <= 0:
            print("Please enter a positive number.")
            continue
        break
            
    for i in range(num_students):
        name = input(f"Enter name for student {i+1}: ").strip().title()
        
        while True:
            score = int(input(f"Enter mark for {name} (0-100): "))
            if 0 <= score <= 100:
                marks_dict[name] = score
                break
            else:
                print("Invalid mark. Please enter a value between 0 and 100.")

    print("Data entry complete.")
    return marks_dict

def get_data_csv():
    """Task 2b: Load student names and marks from a CSV file."""
    print("\n--- CSV File Import ---")
    filename = input("Enter the CSV filename (e.g., students.csv): ")
    marks_dict = {}
    
    
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader) # Skip the header row
        print(f"Reading from {filename}... (Header: {header})")
        
        for row in reader:
            if not row: continue # Skip empty rows
            
            
            name = row[0].strip().title()
            score = int(row[1])
            
            if 0 <= score <= 100:
                marks_dict[name] = score
            else:
                print(f"Skipping {name}: mark {score} is out of range (0-100).")
                
    print(f"Successfully loaded {len(marks_dict)} students.")
    return marks_dict

def calculate_stats(marks_dict):
    """Task 3: Calculate average, median, max, and min scores."""
    if not marks_dict:
        return 0, 0, (None, 0), (None, 0)
        
    marks_list = list(marks_dict.values())
    
    avg = statistics.mean(marks_list)
    median = statistics.median(marks_list)
    
    # Find max/min score and the student's name
    max_student, max_score = max(marks_dict.items(), key=lambda item: item[1])
    min_student, min_score = min(marks_dict.items(), key=lambda item: item[1])
    
    return avg, median, (max_student, max_score), (min_student, min_score)

def assign_grades(marks_dict):
    """Task 4a: Assign a letter grade to each student's mark."""
    grades_dict = {}
    for name, score in marks_dict.items():
        if score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        elif score >= 60:
            grade = 'D'
        else:
            grade = 'F'
        grades_dict[name] = grade
    return grades_dict

def get_grade_distribution(grades_dict):
    """Task 4b: Count the number of students in each grade category."""
    distribution = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for grade in grades_dict.values():
        if grade in distribution:
            distribution[grade] += 1
    return distribution

def filter_pass_fail(marks_dict):
    """Task 5: Use list comprehensions to filter pass/fail students."""
    PASS_MARK = 40
    
    passed_students = {name: score for name, score in marks_dict.items() if score >= PASS_MARK}
    failed_students = {name: score for name, score in marks_dict.items() if score < PASS_MARK}
    
    return passed_students, failed_students

def display_results_table(marks_dict, grades_dict):
    """Task 6: Print a neatly formatted table of all results."""
    print("\n" + "="*35)
    print("      Full Student Grade Report      ")
    print("="*35)
    print(f"{'Name':<15} | {'Mark':^7} | {'Grade':^7}")
    print("-"*35)
    
    # Sort by name for a clean list
    for name in sorted(marks_dict.keys()):
        mark = marks_dict[name]
        grade = grades_dict[name]
        print(f"{name:<15} | {mark:^7} | {grade:^7}")
    print("-"*35)

def save_results_csv(marks_dict, grades_dict):
    """Bonus Task: Save the final results to a new CSV file."""
    filename = input("\nEnter filename to save results (e.g., results.csv): ")
    
    
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Mark', 'Grade']) # Write header
        
        for name in sorted(marks_dict.keys()):
            writer.writerow([name, marks_dict[name], grades_dict[name]])
    print(f"Successfully saved results to {filename}")

def run_analysis_pipeline(marks_dict):
    """A helper function to run all analysis tasks in order."""
    if not marks_dict:
        print("No data to analyze.")
        return

    # Task 3: Statistics
    avg, med, max_info, min_info = calculate_stats(marks_dict)
    
    # Task 4: Grading
    grades_dict = assign_grades(marks_dict)
    distribution = get_grade_distribution(grades_dict)
    
    # Task 5: Pass/Fail
    passed, failed = filter_pass_fail(marks_dict)
    
    # --- Start Printing Report ---
    print("\n" + "#"*40)
    print("        CLASS STATISTICS REPORT        ")
    print("#"*40)
    
    print("\n--- Key Statistics ---")
    print(f"Total Students: {len(marks_dict)}")
    print(f"Class Average:    {avg:.2f}")
    print(f"Class Median:     {med}")
    print(f"Highest Score:  {max_info[1]} (by {max_info[0]})")
    print(f"Lowest Score:   {min_info[1]} (by {min_info[0]})")
    
    print("\n--- Grade Distribution ---")
    for grade, count in distribution.items():
        print(f"Grade {grade}: {count} student(s)")
        
    print("\n--- Pass/Fail Summary (Pass Mark: 40) ---")
    print(f"Passed: {len(passed)} student(s) - {list(passed.keys())}")
    print(f"Failed: {len(failed)} student(s) - {list(failed.keys())}")

    # Task 6: Results Table
    display_results_table(marks_dict, grades_dict)
    
    # Bonus: Save to CSV
    if input("\nDo you want to save this report to a CSV? (y/n): ").strip().lower() == 'y':
        save_results_csv(marks_dict, grades_dict)


# --- Task 6: Main User Loop ---
def main():
    """Main function to run the CLI loop."""
    while True:
        choice = show_menu()
        marks_data = None
        
        if choice == '1':
            # Task 2a: Manual Entry
            marks_data = get_data_manual()
            run_analysis_pipeline(marks_data)
            
        elif choice == '2':
            # Task 2b: CSV Import
            marks_data = get_data_csv()
            if marks_data: # Only run if file was loaded successfully
                run_analysis_pipeline(marks_data)
                
        elif choice == '3':
            print("Exiting GradeBook Analyzer. Goodbye!")
            sys.exit() # Cleanly exits the program
            
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
            
        input("\nPress Enter to return to the main menu...")

# Standard Python entry point
if __name__ == "__main__":
    main()
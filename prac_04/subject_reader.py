"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Load subject data from file and display it in a formatted way."""
    subjects = load_data()
    display_subject_details(subjects)


def load_data():
    """Read data from file and return it as a list of lists."""
    subjects = []
    
    with open(FILENAME, "r") as input_file:
        for line in input_file:
            line = line.strip()  # Remove newline character
            parts = line.split(',')  # Split into components
            parts[2] = int(parts[2])  # Convert student number to an integer
            subjects.append(parts)  # Store each subject as a sublist
    
    return subjects


def display_subject_details(subjects):
    """Display formatted details for each subject."""
    for subject in subjects:
        subject_code, lecturer, student_count = subject
        print(f"{subject_code} is taught by {lecturer} and has {student_count} students")


main()

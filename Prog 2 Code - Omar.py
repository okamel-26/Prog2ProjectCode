# Dictionary to store student grades
# Keys: Student Names, Values: Dictionary of subjects and grades
students = {}

# Function to add a new student
def add_student(name):
   """Adds a new student to the system."""
   if name in students:
       print(f"{name} is already in the system.")
   else:
       students[name] = {}  # Initialize an empty dictionary for the student’s grades
       print(f"{name} has been added.")

# Function to add or update a student's grade for a subject
def add_grade(name, subject, grade):
   """Adds or updates a student's grade for a specific subject."""
   if name not in students:
       print(f"Student {name} not found. Please add the student first.")
   else:
       students[name][subject] = grade  # Store the grade inside the student's dictionary
       print(f"Grade added: {name} - {subject}: {grade}")

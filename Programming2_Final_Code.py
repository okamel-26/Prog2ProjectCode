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
# Function to calculate a student's GPA
def calculate_gpa(name):
   """Calculates and returns the GPA for a student."""
   if name not in students or not students[name]:  # Check if student exists and has grades
       print(f"No grades available for {name}.")
       return None

   grades = students[name].values()  # Get all grades
   gpa = sum(grades) / len(grades)  # Calculate average
   return round(gpa, 2)  # Return rounded GPA value

# Function to display a student's report
def display_report(name):
   """Displays the student's grades and GPA."""
   if name not in students:
       print(f"Student {name} not found.")
   elif not students[name]:  # If the student has no grades
       print(f"{name} has no grades recorded yet.")
   else:
       print(f"\nReport for {name}:")
       for subject, grade in students[name].items():  # Loop through subjects and grades
           print(f"{subject}: {grade}")
       print(f"GPA: {calculate_gpa(name)}\n")  # Print GPA
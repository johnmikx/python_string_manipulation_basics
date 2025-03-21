# Prog05: Create a program that ask the user to input their fullname 
# in incorrect casing. Print the input in proper casing.

# Example:
# Input: jUAn DEla CrUZ
# Output: Juan Dela Cruz

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program that converts user input to proper case (title case).
# - Scope: Command-line application that accepts a string in incorrect casing and outputs it in proper case.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Accept full name input from the user via command line in incorrect casing
#     - Convert the input to proper case (title case)
#     - Preserve spaces and capitalize the first letter of each word
#     - Display the properly formatted result

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Input user's full name in incorrect casing
#     2. Convert the input to proper case using string manipulation
#     3. Display full name in proper case (first letter of each word capitalized)

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Program to convert user input to proper case (title case)
full_name = input("Enter your full name in incorrect casing: ")
result = full_name.title()
print(f"Output: {result}")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1:
# - Input: "jUAn DEla CrUZ"
# - Expected Output: "Juan Dela Cruz"

# Test Case 2:
# - Input: "MIKE kaizen"
# - Expected Output: "Mike Kaizen"

# Test Case 3:
# - Input: "john mike P. aSUNCION"
# - Expected Output: "John Mike P. Asuncion"

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 5

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike
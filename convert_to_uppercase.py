# Prog03: Create a program that ask the user to input their fullname. 
# Print the input in all capital letter.

# Example:
# Input: Juan Dela Cruz
# Output: JUAN DELA CRUZ

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program that converts user input to uppercase.
# - Scope: Command-line application that accepts a string and outputs it in all capital letters.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Accept full name input from the user via command line
#     - Convert all characters to uppercase
#     - Preserve spaces and other non-alphabetical characters
#     - Display the properly formatted result

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Input user's full name in any case
#     2. Convert all characters to uppercase using string manipulation
#     3. Display full name in all capital letters

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Program to remove leading spaces from user input
full_name = input("Enter your full name: ")
result = full_name.upper()
print(f"Output: {result}")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1:
# - Input: "Juan Dela Cruz"
# - Expected Output: "JUAN DELA CRUZ"

# Test Case 2:
# - Input: "mike kaizen"
# - Expected Output: "MIKE KAIZEN"

# Test Case 3:
# - Input: "John Mike P. Asuncion"
# - Expected Output: "JOHN MIKE P. ASUNCION"

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 5

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike
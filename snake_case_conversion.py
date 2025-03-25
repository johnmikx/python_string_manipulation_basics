# Prog10: Create a program that ask the user to input their fullname 
# in incorrect casing. Print the input in snake case.

# Example:
# Input: jUAn DEla CrUZ
# Output: juan_dela_cruz

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program that converts user input to snake case.
# - Scope: Command-line application that accepts a string and outputs it in snake case.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Accept full name input from the user via command line in incorrect casing
#     - Convert the input to snake case (all lowercase, words separated by underscores)
#     - Display the properly formatted result

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Input user's full name in incorrect casing
#     2. Convert to lowercase and replace spaces with underscores
#     3. Display full name in snake case format

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Program to convert user input to snake case
full_name = input("Enter your full name in incorrect casing: ")
result = full_name.lower().replace(" ", "_")
print(f"Output: {result}")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1:
# - Input: "jUAn DEla CrUZ"
# - Expected Output: "juan_dela_cruz"

# Test Case 2:
# - Input: "MIKE kaizen"
# - Expected Output: "mike_kaizen"

# Test Case 3:
# - Input: "john mike aSUNCION"
# - Expected Output: "john_mike_asuncion"

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 5

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike
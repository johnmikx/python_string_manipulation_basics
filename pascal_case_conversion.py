# Prog09: Create a program that ask the user to input their fullname 
# in incorrect casing. Print the input in pascal case.

# Example:
# Input: jUAn DEla CrUZ
# Output: JuanDelaCruz

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program that converts user input to Pascal case.
# - Scope: Command-line application that accepts a string and outputs it in Pascal case.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Accept full name input from the user via command line in incorrect casing
#     - Convert the input to Pascal case (capitalize first letter of each word and remove spaces)
#     - Display the properly formatted result

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Input user's full name in incorrect casing
#     2. Convert to title case and replace spaces with no spaces
#     3. Display full name in Pascal case format

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Program to convert user input to Pascal case
full_name = input("Enter your full name in incorrect casing: ")
result = full_name.title().replace(" ", "")
print(f"Output: {result}")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1:
# - Input: "jUAn DEla CrUZ"
# - Expected Output: "JuanDelaCruz"

# Test Case 2:
# - Input: "MIKE kaizen"
# - Expected Output: "MikeKaizen"

# Test Case 3:
# - Input: "john mike aSUNCION"
# - Expected Output: "JohnMikeAsuncion"

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 5

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike
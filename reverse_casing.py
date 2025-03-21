# Prog06: Create a program that ask the user to input their fullname in 
# incorrect casing. Print each character of the input in reverse casing.

# Example:
# Input: jUAn DEla CrUZ
# Output: JuaN deLA cRuz

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program that reverses the case of each character in user input.
# - Scope: Command-line application that accepts a string and outputs it with reversed casing.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Accept full name input from the user via command line in incorrect casing
#     - Reverse the case of each character (uppercase to lowercase, lowercase to uppercase)
#     - Preserve spaces and non-alphabetical characters
#     - Display the properly formatted result

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Input user's full name in incorrect casing
#     2. For each character:
#        2.1. If character is in uppercase:
#             2.1.1. Convert to lowercase
#        2.2. Otherwise:
#             2.2.1. Convert to uppercase
#     3. Display full name with reversed casing for each character

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Program to reverse the case of each character in user input
full_name = input("Enter your full name in incorrect casing: ")
result = ""

for char in full_name:
    if char.isupper():
        result += char.lower()
    else:
        result += char.upper()

print(f"Output: {result}")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1:
# - Input: "jUAn DEla CrUZ"
# - Expected Output: "JuaN deLA cRuz"

# Test Case 2:
# - Input: "MIKE kaizen"
# - Expected Output: "mike KAIZEN"

# Test Case 3:
# - Input: "John Mike P. Asuncion"
# - Expected Output: "john mike P. aSUNCION"

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 5

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike
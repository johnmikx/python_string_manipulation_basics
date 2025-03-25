# Prog02: Create a program that ask the user to input a number (0-1000).
# Print the number in 6 digit format. Add zeros at the beginning to 
# complete the 6 digit.

# Example:
# Input: 143
# Output: 000143

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program that formats numbers as 6-digit strings with leading zeros.
# - Scope: Command-line application that accepts a number and outputs it in 6-digit format.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Accept a numeric input from the user (0-1000)
#     - Format the number as a 6-digit string
#     - Add leading zeros to complete the 6-digit format
#     - Display the properly formatted result

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Input integer number between 0 and 1000
#     2. Format the number as a string with leading zeros to make it 6 digits long
#     3. Display 6-digit string representation of the number

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Program to format a number as a 6-digit string with leading zeros
number = int(input("Enter a number (0-1000): "))
formatted_number = str(number).zfill(6)
print(f"Output: {formatted_number}")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1:
# - Input: 143
# - Expected Output: 000143

# Test Case 2:
# - Input: 0
# - Expected Output: 000000

# Test Case 3:
# - Input: 1000
# - Expected Output: 001000

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 5

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike
# Prog08: Create a program that ask the user to input their fullname. 
# Print the number of characters in the input.

# Example:
# Input: Juan Dela Cruz
# Output: 14

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program that counts the number of characters in user input.
# - Scope: Command-line application that accepts a string and outputs the character count.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Accept full name input from the user via command line
#     - Count all characters in the input, including spaces
#     - Handle multiple spaces between words correctly
#     - Display the character count

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Input user's full name
#     2. Count the total number of characters in the input string
#     3. Display number of characters in the full name

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Program to count the number of words in user input
full_name = input("Enter your full name: ")
char_count = len(full_name)
print(f"Output: {char_count}")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1:
# - Input: "Juan Dela Cruz"
# - Expected Output: 14

# Test Case 2:
# - Input: "Mike Kaizen"
# - Expected Output: 11

# Test Case 3:
# - Input: "John Mike Asuncion"
# - Expected Output: 18

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 5

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike
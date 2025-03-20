# Prog01: Create a program that ask the user to input their fullname 
# with several space characters at the beginning. 
# Print the input without the spaces in the beginning.

# Example:
# Input:         Juan Dela Cruz
# Output: Juan Dela Cruz

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program that removes leading spaces from user input.
# - Scope: Command-line application that accepts a string with leading spaces.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Accept full name input from the user via command line
#     - Remove any spaces at the beginning of the input
#     - Preserve the original text content includng the internal spaces
#     - Display the properly formatted result

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Input user's full name with potential leading spaces
#     2. Remove leading whitespace characters using string manipulation
#     3. Display full name without leading spaces

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Program to remove leading spaces from user input
full_name = input("Enter your full name with spaces at the beginning: ")
result = full_name.lstrip()
print(f"Output: {result}")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1:
# - Input: "    Juan Dela Cruz"
# - Expected Output: "Juan Dela Cruz"

# Test Case 2:
# - Input: "Juan Dela Cruz"
# - Expected Output: "Juan Dela Cruz"

# Test Case 3:
# - Input: "        John Mike P. Asuncion"
# - Expected Output: "John Mike P. Asuncion"

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 5

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike